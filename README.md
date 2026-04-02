# WSN Trust-Based Routing

![Python Version](https://img.shields.io/badge/python-3.9%2B-blue.svg) ![License](https://img.shields.io/badge/license-MIT-green.svg)

This project proposes an energy-aware trust-based routing protocol for wireless sensor networks that isolates malicious nodes while maintaining network longevity.

## Quickstart

Clone this repository and install dependencies:

```bash
git clone <REPO_URL_PLACEHOLDER>
cd wsn-trust-routing
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Project Structure

- `src/`: Core implementation code.
- `notebooks/`: Jupyter notebooks for exploration and experiments.
- `results/`: Figures, tables, and saved model artifacts.
- `configs/`: YAML/JSON configuration files for reproducible experiments.
- `docs/`: Documentation, protocol descriptions, replication guide.
- `scripts/`: Helper scripts for setup, data download, and automation.
- `tests/`: Unit and smoke tests.

Refer to the `/docs` folder for detailed methodology and replication instructions.

ore Algorithm

The trust-based routing algorithm computes a composite trust score for each node 
𝑛
n using a combination of direct and indirect trust, with exponential decay to capture trust staleness:

𝑇
(
𝑛
)
=
𝛼
⋅
𝐷
𝑇
(
𝑛
)
  
+
  
𝛽
⋅
𝐼
𝑇
(
𝑛
)
⋅
𝑒
−
𝜆
𝑡

**T(n) = α⋅DT(n)+β⋅IT(n)⋅e −λt**

| Symbol    | Definition                                                              | Value         |
| --------- | ----------------------------------------------------------------------- | ------------- |
| (T(n))    | Composite trust score for node (n)                                      | Derived value |
| (DT(n))   | Direct trust of node (n) based on its own forwarding behaviour          | Derived value |
| (IT(n))   | Indirect trust of node (n), aggregated from neighbours’ recommendations | Derived value |
| (t)       | Time since last trust update (simulation rounds)                        | —             |
| (\alpha)  | Weight of direct trust                                                  | 0.6           |
| (\beta)   | Weight of indirect trust                                                | 0.4           |
| (\lambda) | Decay constant controlling how quickly trust becomes stale              | 0.05          |

