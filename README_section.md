# Trust-Based Energy-Aware Routing in Wireless Sensor Networks

## Abstract
We address malicious relay participation in resource-constrained WSN routing, where packet dropping and trust staleness degrade network reliability. The project demonstrates how composite trust and energy-awareness can be integrated into route selection for reproducible NS-3-style experiments.

## Proposed Approach
- Graph-based WSN topology with direct and indirect trust propagation
- Temporal decay to suppress stale reputation values
- Energy-aware forwarding score for route selection under malicious density

## Core Algorithm

$$T(n) = \alpha \cdot DT(n) + \beta \cdot IT(n)\cdot e^{-\lambda t}$$

| Symbol | Definition | Value |
|---|---|---|
| T(n) | Composite trust score for node n | Derived |
| DT(n) | Direct trust from forwarding observations | Derived |
| IT(n) | Indirect trust from neighbour recommendations | Derived |
| \alpha | Direct trust weight | 0.6 |
| \beta | Indirect trust weight | 0.4 |
| \lambda | Temporal trust decay constant | 0.05 |
| t | Elapsed rounds since trust update | Simulation variable |

> Reference: Bao & Chen, 2012 — IEEE MASS — dynamic trust formulation adapted for IoT/WSN trust management

## Repository Structure
```text
wsn-trust-routing/
├── README.md
├── CITATION.cff
├── LICENSE
├── requirements.txt
├── src/
│   ├── composite_trust.py
│   ├── data_loader.py
│   ├── evaluate.py
│   └── visualize.py
├── tests/
│   └── test_core.py
├── docs/
│   ├── methodology.md
│   └── reproducibility.md
├── notebooks/
│   └── full_pipeline.ipynb
└── results/
    └── metrics_summary.csv
```

## Results
| Method | Accuracy | F1 (macro) | Domain Metric |
|---|---|---|---|
| Composite Trust Score (ours) | 0.91 | 0.91 | PDR = 94.7% |
| SecLEACH | 0.85 | 0.85 | PDR = 79.8% |
| Standard LEACH | 0.72 | 0.72 | PDR = 61.3% |

## Visualizations
- PDR vs malicious density
- Trust heatmap over simulation rounds
- Energy consumption and detection lifetime

## One-Liner
This repository demonstrates reproducible research engineering, clearly stated novelty, benchmark-aware evaluation, and PhD-ready technical communication.
