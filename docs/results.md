# Results, by research stage

[← Project overview](../README.md)

## Original isolated A/B/C study

| Joint success | Original evaluator | Retrospective sensitivity evaluator |
|---|---:|---:|
| A: Direct | 58/90 | 65/90 |
| B: Handoff-Only | 56/90 | 63/90 |
| C: Source-Anchored | 61/90 | 67/90 |

With original scoring, the full-sample A-minus-B contrast was +2.2 percentage points (95% task-bootstrap CI [−6.7,+12.2]); C-minus-B was +5.6 points ([−2.2,+14.4]). Neither established an average advantage. Revised scoring produced +2.2 and +4.4 points, also imprecise.

Original B failure conditional on A success was 9/58 (15.5% pooled); its task-equal-weight summary was 24.6%. These are **different weighting schemes**, and neither is the average A-minus-B success difference. Opposite-direction discordance included seven A-fail/B-pass pairs, compared with nine A-pass/B-fail pairs.

C succeeded on 5/9 selected A-pass/B-fail pairs. That conditional success proportion cannot establish the benefit of source attachment over an ordinary retry or the cause of an individual success.

## Retrospective evaluator sensitivity

All 270 archived isolated-study patches were uniformly rescored. Functional flags did not change. Twenty-three constraint flags changed: 21 fail-to-pass and two pass-to-fail. Three pairs left the conditional A-pass/B-fail subset and three different pairs entered.

The score revision was post-collection and developed with prior knowledge of selected failures. It does not replace the original analysis or constitute independent confirmation.

## Prospective B0/B1/C follow-up

| Endpoint | B0 | B1 | C | C−B1: task-weighted difference, 95% CI |
|---|---:|---:|---:|---|
| **Revised joint — primary** | **63/90** | **66/90** | **66/90** | **0.0 pp [−7.8,+8.9]** |
| Functional | 73/90 | 77/90 | 77/90 | 0.0 pp [−8.9,+10.0] |
| Constraint | 71/90 | 71/90 | 71/90 | 0.0 pp [−4.4,+4.4] |
| Original-evaluator joint | 54/90 | 58/90 | 58/90 | 0.0 pp [−6.7,+8.9] |

Intervals use 100,000 task-bootstrap resamples over 30 task clusters. Equal total successes do not establish equality of outcomes on each handoff, equal patches, or equivalence.

The B0-failure secondary subset contained 27 handoffs from 11 tasks. B1 succeeded on 3/27; C on 4/27. The equal-task-weight difference was +4.5 pp (95% CI [−27.3,+36.4]); the pooled difference is instead 1/27. These are not interchangeable estimands.

Same-handoff B0/B1 joint discordance was three B0-fail/B1-pass pairs and zero B0-pass/B1-fail pairs.

Empty-handoff joint successes were 1/7,1/7,4/7 in B0/B1/C; nonempty successes were 62/83,65/83,62/83. Presence was not randomized, the small cells are descriptive, and the seven empty handoffs represent only five tasks.

## Interpretation boundaries

- The follow-up did not establish an average source-anchoring advantage over independent retry. It did not prove no effect or equivalence.
- Textual preservation is not evidence that a handoff was actionable or that a failure was purely downstream execution.
- Two-model label agreement is not independent human validation; the author check covered 15 targeted cases with prior label/outcome exposure.
- The task bank is reused, the sample is balanced rather than naturally weighted, and the requested model is one mutable alias. Task/repository dependencies and finite test coverage limit generalization.
- The follow-up has no new Direct arm, so it does not re-estimate an average Direct-versus-Delegated effect.
- The project is about reliability and evaluation methodology, not a demonstrated general safety guarantee.
