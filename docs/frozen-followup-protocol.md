# Prospective follow-up v1: source anchoring versus an independent retry

Status: prepared for local pre-execution freeze after offline integration testing. This is not a public preregistration. No outcome from a new live model run has been inspected in drafting this protocol. Prior exploratory work and retrospective evaluator revisions are disclosed.

## Population, scope and fixed design

Use exactly the original 30 tasks and 90 frozen Planner handoffs (three per task), including empty handoffs. No task/handoff selection based on prior or new failure. This is a prospective follow-up on a previously studied handoff bank, with equal-stratum sampling; it is not an independent task sample or a new Planner-generation experiment.

For each block execute three fresh Developers: B0 handoff only (screen), B1 byte-identical handoff-only prompt (independent retry), C same handoff plus original issue/constraint. No trajectories, patches or outcomes from B0 or any old run are passed to B1 or C. Independent means fresh context/repository executions, not guaranteed independent provider random seeds. All three runs occur regardless of B0 result; their order is randomized within blocks and block order randomized by the frozen schedule seed. This controls chronological effects without expanding condition count after observing outcomes.

Total fixed target: 270 fresh Developer executions. There are 30 task clusters, not 270 independent tasks. The study does not produce a new contemporaneous A-versus-B estimate. Small effects may remain unresolved at this task count. No sample-size expansion, endpoint switching or early success/futility stopping based on scientific outcomes.

## Primary endpoint and estimand

Primary endpoint: joint success under the frozen post-collection sensitivity evaluator v1, defined as both functional and constraint suites passing. Its rules were validated on 30 gold, 30 empty, 30 benchmark-labeled noncompliant and 20 controlled transformation cases before this follow-up; ten tasks have revised rules, twenty retain finite original proxies. The original benchmark endpoint is a prespecified secondary robustness outcome, always reported alongside the revised endpoint.

Primary estimand: within each of the 30 tasks average C minus B1 binary joint success over its three handoff blocks, then average equally across tasks. Report counts and difference with percentile 95% task-bootstrap interval using 100,000 resamples and the frozen analysis seed. No equivalence claim or implication that a CI crossing zero establishes no effect. This estimates performance under the registered scaffold/budgets on the fixed bank, not universal semantic compliance.

## Secondary estimands

Select blocks using only B0 joint failure under the primary evaluator; compare independent C versus B1 success within those blocks. Average within contributing tasks then equally across those tasks; report contributing task/block counts, pooled counts and task-bootstrap interval conditional on the realized eligible-task set. Fewer than five contributing tasks: descriptive point estimate/counts only; zero: not estimable. No new runs triggered by subset size. This separates source attachment from successful fresh retry in a screen-selected population; it does not identify the cause of an individual prior failure.

Also report B0/B1 bidirectional discordance, separate functional/constraint contrasts, original-evaluator joint contrast, cost/steps/limit exits, and descriptive empty/nonempty cells. The code in analyze_followup.py is frozen; amendment 001 in the previous sensitivity phase is not hidden or treated as preregistration here. Only the stated joint contrast is primary.

## Inputs, model and resources

Reuse the frozen B/C prompt structures and byte-identical handoffs. Replace the original descriptive instance-ID line with 'Benchmark instance identifier: withheld' in all roles. Retain real IDs only internally for Docker/evaluator routing. Local code/tests can still reveal task information; neither B nor empty handoffs create an information-free environment.

Developer requested alias deepseek-flash via the official direct endpoint. Current documentation identifies this alias as V4.1-Flash; do not assert it is the same backend as the historical experiment. Pin the first nonempty returned model identifier and stop if any later identifier differs. Alias identity alone does not prove an immutable backend. Temperature 0, high reasoning, response max 8192 tokens, context soft limit 65536, 30 soft / 40 absolute steps, one iteration, fresh contexts, no subagents; same tools/budgets in all roles. Preserve the original launcher and hardened no-network containers (4 GiB, 2 CPU, 512 PIDs, dropped capabilities, no new privileges). Agent/evaluator images and runtime sources are hashed before calls.

The host API gateway is separate from agent containers. Agents receive only an ephemeral local gateway credential, never the real provider credential. Hidden evaluator artifacts remain unavailable during implementation. Original and revised evaluator executions use isolated containers and fresh repository copies.

## Cost accounting and stopping

Hard user cap USD 50 across this new experiment, including uncertain and invalid attempts. Rates frozen at official peak uncached USD 0.30/M input, USD 1.20/M output. Before every upstream request durably reserve the full provider context ceiling 1,048,576 input tokens plus 8192 output/reasoning tokens. Settlement uses reported total prompt/completion tokens at uncached peak rates, ignoring discounts, so accounting conservatively upper-bounds expected billed cost under the documented contract. Lack of usage, impossible usage, upstream timeout/error, or returned model change stops the study. Uncertain calls keep their full reservation; do not silently refund or automatically repeat them. SQLite transactions protect concurrent reservations and restarts.

This preserves original per-run token/step budgets rather than adding a prompt-length-dependent dollar cap per run. It does not guarantee all 270 runs complete for USD 50. If the ledger cannot reserve the next full request, stop, mark the experiment incomplete and preserve all attempts; do not analyze a completed prefix as the full experiment. Price/endpoint changes require stopping and documented amendment before any further call. Scope is a contractual cost bound, not protection against unannounced provider billing changes.

Scientific failures, empty patches and registered resource-limit exits are not retried. Invalid infrastructure attempts are archived with explicit cause; automatic retries at study level are disabled. Any retry requires a recorded disposition and remains in the same cumulative ledger. A rate/error or budget stop is not turned into scientific success/failure to complete the sample. Run output and ledger state are reconciled on resume; unresolved in-flight charges block continuation.

## Validation, freeze and reporting

Offline guard tests include concurrency, crash/persistence, unknown billing, model drift, unauthorized local clients and duplicate settlement. A complete three-role smoke block uses only a local mock model, separate smoke data/ledger and no provider calls. Smoke outcomes never enter scientific analysis. Freeze only after these checks pass. Confirm price card, freeze files/schedule/image IDs, then execute sequentially with persistent accounting. The analysis refuses incomplete/mock studies. Logs, invalid attempts, manifests and amendments retained; never overwrite the original study.

A result unfavorable to the hypothesis or with a wide interval is reported as such. The eventual contribution and any additional controlled omission/restoration intervention depend on these findings, not a desired positive claim. Public release remains deferred pending scientific review, artifact consistency and final PDF validation.
