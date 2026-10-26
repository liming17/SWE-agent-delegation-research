# Reproduce the analysis without model calls

[← Project overview](../README.md)

## What is included

The curated derived-outcome package contains opaque task/handoff IDs, binary evaluator outcomes, resource summaries, expected frozen analysis output, sanitized accounting and a portable standard-library reproduction script. It excludes original task requirements, full handoffs, code patches, trajectories, real credentials and private review inputs.

From the project root:

```bash
python3 scripts/reproduce.py
```

The script verifies the primary full-bank contrast; functional, constraint and original-evaluator secondary contrasts; the B0-screened subset; task-bootstrap intervals; condition counts; B0/B1 discordance; and the conservative total charge. Bootstrap reproduction may take a little time. It should end with a message that all reported results reproduce exactly, without API calls.

## What this does not reproduce

It does not rerun Developers, regenerate Planners, execute hidden evaluators or recover provider backend snapshots. Those require the private research workspace and upstream environment. The locally frozen analysis remains the source of the expected results; the portable script is a separately checked reproduction.

Do not run historical experiment or recovery commands merely to reproduce these tables.

## Accounting and invalid attempts

The final conservative cumulative accounting was $22.7256351 against a $50 cap; no unresolved request remained. The total includes invalid and uncertain attempts and is not a provider invoice. The corrected cohort contains 270 valid Developer executions, including 12 resource-limit exits; six additional transport-invalid attempts were separately archived. Pre-output-limit-fix attempts were excluded in full regardless of outcome.

## Integrity and redistribution

The portfolio export has a `SHA256SUMS` manifest and a source/provenance inventory. Derived data are supplied for examination and analysis reproduction. This does not confer rights to upstream benchmark text or code. Author-controlled materials and upstream dependencies have separate provenance; no new redistribution license for upstream material is asserted.

The full local audit retained original outcomes, evaluator sensitivity, frozen inputs, runtime versions, hashes and disposition records. The public-facing subset is intentionally smaller than that workspace and does not include its Git history or application/interview drafts.
