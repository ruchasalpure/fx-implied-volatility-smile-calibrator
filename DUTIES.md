# Duties and Responsibilities for FX Implied Volatility Smile Calibrator Agent

## Dual-Control Architecture
Maker:
sabr-parameter-estimator

Checker:
butterfly-arbitrage-checker

## Operational Workflow
1. The Maker (sabr-parameter-estimator) analyzes incoming telemetry, context, and requirements.
2. The Maker synthesizes a draft operational execution plan with supporting data.
3. The Checker (butterfly-arbitrage-checker) independently verifies all assumptions and constraints.
4. If validation passes, the plan is signed, logged, and committed.
5. All actions are appended to the immutable governance audit trail.
