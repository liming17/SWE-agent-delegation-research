# Experimental design

[← Project overview](../README.md)

## Scope and units

The project used 30 Python software-repair tasks from SWE-Gate. A pre-treatment eligibility procedure retained 255 of 303 released tasks with complete validation artifacts and published evaluated outcomes. Six tasks were selected from each of five published baseline-solvability strata using a fixed hash procedure, with construction-seed and repository caps.

This produced a balanced study sample, not the natural task proportions of all eligible tasks. The solvability strata were proxies from a fixed four-model panel, not intrinsic difficulty labels. The 30 tasks came from 22 repositories; task-level clustering does not prove all between-task dependence absent.

Three Planner repeats per task produced **90 fixed handoffs**, seven empty. The prospective follow-up reused all 90; it did not regenerate Planners or repair empty outputs.

## Original isolated comparison

| Condition | Developer input |
|---|---|
| A: Direct | Original issue + constraint |
| B: Handoff-Only | Frozen Planner handoff |
| C: Source-Anchored | Byte-identical handoff + original issue + constraint |

An earlier network-enabled collection was retained separately after a trajectory audit found remote-access commands. The isolated A/B/C collection contained 270 Developer executions on the frozen handoff bank. Neither differences between collections nor selected A-pass/B-fail cases identify individual causal mechanisms.

## Prospective retry control

B0 and B1 received byte-identical handoff-only prompts in fresh executions. C received the same handoff plus original requirements. All three roles ran regardless of B0 outcome. Block and within-block role order were randomized by a fixed seed. B0 results, patches and trajectories were never implementation inputs to B1 or C.

The Developer-visible descriptive task-ID line was withheld. All roles retained repository and local-test access, so an empty handoff did not create an information-free environment.

The primary endpoint was joint success under the frozen revised evaluator. The **primary estimand** averaged paired C-minus-B1 binary differences over three handoffs within each task, then equally across 30 tasks. Uncertainty used 100,000 percentile task-bootstrap resamples with the frozen analysis seed. The original evaluator was a separate secondary robustness endpoint.

Only the secondary analysis selected B0 joint failures. That comparison averaged within contributing tasks, then equally across them; its task/block denominators and much wider uncertainty were reported separately.

## Runtime configuration

All follow-up roles requested the official `deepseek-flash` alias with high reasoning and the same tools/budgets: native output maximum 8,192 tokens, context soft limit 65,536, and 30 soft/40 absolute steps. Fresh Developer and evaluator containers used no network, 4 GiB memory, two CPUs, 512-process limits, dropped capabilities and no privilege escalation. A local host gateway held the actual provider credential.

A stable alias/returned identifier does not establish an immutable backend or equality with the historical model. Temperature zero does not make runs deterministically identical. Fresh executions do not establish provider-level independent random seeds.

## Evaluator revision and preservation

The post-collection audit examined all 30 task constraints/tests. Ten rules were revised; 20 retained original finite proxies. Validation comprised 90 gold/empty/benchmark-labelled noncompliant reference evaluations and 20 controlled equivalent/violating transformations. Revised evaluator code was frozen before uniform rescoring of old patches and before prospective calls.

The revision used prior knowledge of selected failures. It is a disclosed retrospective sensitivity analysis, not independent confirmation. Original scores remain intact; revised tests are not a semantic oracle. Some constraint suites include functional checks, so the two scoring dimensions are not necessarily independent.

## Protocol discipline

The follow-up was locally frozen, **not publicly preregistered**. No outcome-driven expansion, early success stopping, new Direct arm or primary-endpoint switching was introduced. Scientific failures and valid resource-limit exits remained outcomes. Only recorded infrastructure-invalid attempts were excluded/retried; all costs stayed in the same cumulative cap.

[Results and limitations →](results.md)
