"""Portable reproduction of prespecified contrasts from derived outcome labels."""
import collections,csv,json,random,statistics
from pathlib import Path
H=Path(__file__).resolve().parents[1];rows=list(csv.DictReader((H/'data/outcomes.csv').open()));expected=json.loads((H/'data/expected-results.json').read_text());blocks=collections.defaultdict(dict);tasks=collections.defaultdict(list)
for r in rows:
 blocks[r['handoff']][r['role']]=r;blocks[r['handoff']]['task']=r['task']
assert len(rows)==270 and len(blocks)==90
for b in blocks.values():
 assert all(k in b for k in ['B0','B1','C']);tasks[b['task']].append(b)
assert len(tasks)==30 and all(len(v)==3 for v in tasks.values())
def interval(values,tag):
 if len(values)<5:return None
 rng=random.Random('anchoring-followup-v1-bootstrap-'+tag);draws=sorted(statistics.mean(rng.choices(values,k=len(values))) for _ in range(100000))
 def q(p):
  x=(len(draws)-1)*p;i=int(x);return draws[i]+(draws[min(i+1,len(draws)-1)]-draws[i])*(x-i)
 return [q(.025),q(.975)]
def contrast(field):
 v=[statistics.mean(int(b['C'][field])-int(b['B1'][field]) for b in bs) for task,bs in sorted(tasks.items())]
 return dict(task_mean_difference=statistics.mean(v),task_bootstrap_95_ci=interval(v,field),tasks=len(v))
assert contrast('joint')==expected['primary']
for f in ['functional','constraint','original_joint']:assert contrast(f)==expected['secondary_full_sample'][f]
v=[];selected=[]
for task,bs in sorted(tasks.items()):
 eligible=[b for b in bs if not int(b['B0']['joint'])];selected.extend(eligible)
 if eligible:v.append(statistics.mean(int(b['C']['joint'])-int(b['B1']['joint']) for b in eligible))
s=expected['secondary_screened'];assert len(selected)==s['blocks'] and len(v)==s['tasks'];assert statistics.mean(v)==s['task_mean_C_minus_B1'];assert interval(v,'screened')==s['task_bootstrap_95_ci']
for role in ['B0','B1','C']:
 for f,n in expected['counts'][role].items():assert sum(int(r[f]) for r in rows if r['role']==role)==n
assert sum(int(b['B0']['joint']) and not int(b['B1']['joint']) for b in blocks.values())==expected['same_handoff_repeat_discordance']['B0_pass_B1_fail']
assert sum(not int(b['B0']['joint']) and int(b['B1']['joint']) for b in blocks.values())==expected['same_handoff_repeat_discordance']['B0_fail_B1_pass']
account=list(csv.DictReader((H/'data/accounting.csv').open()));assert all(r['status']=='settled' for r in account);total=sum(int(r['charge_nusd']) for r in account)
assert total==expected['budget']['accounted_nusd'] and total<=expected['budget']['cap_nusd']
print('All primary and secondary contrasts, task-bootstrap intervals, counts, discordance and accounting reproduce exactly. No API calls.')
