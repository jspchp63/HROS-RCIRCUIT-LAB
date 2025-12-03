# Phase Simulation v0.1 — Summary

## Goal
Test basic Δsignal propagation across 5 PhaseNodes using RCIRCUIT v0.1 rules.

## Setup
- Nodes: 5
- Initial phases: [1.0, 1.5, 2.0, 0.5, 0.8]
- Input Δsignal: 0.3
- Noise threshold: 0.05
- Propagation steps: 10
- Engine: RCIRCUIT v0.1 (concept version)

## Findings
- Phase alignment begins after the first propagation step.
- Local coherence increases step-by-step.
- Δsignal propagation stabilizes quickly.
- Energy cost trend appears ~0.1x vs value-movement baseline.
- Supports hypothesis: **propagate phase, not values**.

## Notes
This is a conceptual, public-safe experiment,
not a full RCIRCUIT engine.

## Next Steps
- Add noise model (stochastic)
- Add Phase Scheduler v0.1
- Add coherence score tracking
- Add visualization tools (phase-over-time plot)
