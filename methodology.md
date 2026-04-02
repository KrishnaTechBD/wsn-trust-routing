# Methodology

## Problem Formulation
We formulate the central task for **Trust-Based Energy-Aware Routing in Wireless Sensor Networks** through the governing equation below.

$$T(n) = \alpha \cdot DT(n) + \beta \cdot IT(n)\cdot e^{-\lambda t}$$

## Variable Definitions
| Symbol | Definition | Value |
|---|---|---|
| T(n) | Composite trust score for node n | Derived |
| DT(n) | Direct trust from forwarding observations | Derived |
| IT(n) | Indirect trust from neighbour recommendations | Derived |
| \alpha | Direct trust weight | 0.6 |
| \beta | Indirect trust weight | 0.4 |
| \lambda | Temporal trust decay constant | 0.05 |
| t | Elapsed rounds since trust update | Simulation variable |

## Evaluation Logic
The repository is framed around benchmark-aware comparison, reproducible parameterization, and professor-friendly reporting.
