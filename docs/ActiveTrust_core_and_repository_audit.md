# ActiveTrust Core-Work and GitHub Repository Audit

## Executive conclusion

The public repository at [KrishnaTechBD/wsn-trust-routing](https://github.com/KrishnaTechBD/wsn-trust-routing) does not currently contain the implementation or dataset required to verify the ActiveTrust paper. The full Git history was inspected through commit `4843a0337a86592875cc39dcf897aa109d7f4cd6`; no historical commit contains the promised `src/`, `tests/`, `notebooks/`, `data/`, `results/`, NS-3 code, raw output, or figure-generation files.

The repository is therefore a **documentation scaffold/project placeholder**, whereas the paper describes a distinct NS-3.40 protocol with proactive probes, adaptive probe-count computation, MaxMinEnergyPath route generation, EMA trust updates, trust-filtered Dijkstra routing, ablation experiments, ROC analysis, and 50-run statistical evaluation. It is not scientifically defensible to regenerate the paper’s “updated dataset” from the public repository alone. The updated dataset deliverable in this package is consequently a **dataset specification and provenance audit**, not a fabricated replacement dataset.

## 1. Paper core versus repository core

| Dimension | ActiveTrust paper | Public repository | Fidelity assessment |
|---|---|---|---|
| Research problem | Proactive black-hole detection in WSN routing | Generic trust-based energy-aware routing | Different framing |
| Trust model | Per-node delivery ratio plus EMA, with threshold and lock-out | Composite direct/indirect trust with exponential temporal decay | Mathematical mismatch |
| Probe mechanism | Data-sized authenticated probes, adaptive `M`, non-hotspot routes | Not implemented or tracked | Missing |
| Route generation | MaxMinEnergyPath over non-hotspot graph | Not implemented or tracked | Missing |
| Secure routing | Trust-filtered Dijkstra with route repair | Not implemented or tracked | Missing |
| Simulator | NS-3.40 with WSN energy and 802.15.4 settings | No NS-3 code or dependency | Not reproducible |
| Baselines | AODV, DSR, PassiveTrust | README names SecLEACH and Standard LEACH | Baseline mismatch |
| Metrics | PDR, detection latency, recall/FPR, AUC, energy overhead, lifetime, ablation | README reports accuracy/F1/PDR only | Metric mismatch |
| Dataset | 50 independent runs across several BHA densities and configurations | No dataset; `data/` and `results/` ignored and absent | Missing |
| Randomness | Paper claims distinct random seeds for 50 runs | `reproducibility.md` says `SEED=42` | Reproducibility conflict |
| Figures | Eight ActiveTrust figures | No figure-generation source; eight images only recoverable from supplied PDF | Source recovery only |

## 2. Repository-specific findings

The README describes a repository structure containing `src/composite_trust.py`, `src/data_loader.py`, `src/evaluate.py`, `src/visualize.py`, tests, notebooks, and results. None of these paths is tracked in the audited repository. The file named `wsn-trust-routing` is only a text tree description, not an executable directory or source module.

The repository’s documented formula is

\[
T(n)=\alpha DT(n)+\beta IT(n)e^{-\lambda t},
\]

with `\alpha=0.6`, `\beta=0.4`, and `\lambda=0.05`. This is not the EMA formula used in the ActiveTrust paper. The README also reports a different result table: Composite Trust Score accuracy/F1 of 0.91 and PDR of 94.7%, SecLEACH PDR of 79.8%, and Standard LEACH PDR of 61.3%. These numbers cannot be used as evidence for the paper’s ActiveTrust results without a documented mapping and raw experiment provenance.

The dependency file contains only pandas, scikit-learn, matplotlib, and pytest. It does not provide NS-3, an NS-3 Python interface, a packet-level WSN simulator, or the source required to reproduce the paper’s experiments.

## 3. What can and cannot be updated from current evidence

| Deliverable | Can be produced now? | Evidence status |
|---|---:|---|
| IEEE paper structural draft | Yes | Based on supplied PDF and prior reconstruction |
| Overleaf-compatible LaTeX skeleton | Yes | Compilable; figures can be inserted from PDF-extracted assets |
| Figure package | Yes, with provenance label | Eight raster figures extracted from supplied PDF and cropped to remove embedded captions |
| Updated raw dataset | **No** | Repository contains no raw data or executable experiment pipeline |
| Updated means/CIs/p-values | **No** | Cannot recompute without per-run outputs or simulator |
| Updated ROC/AUC | **No** | No node-level decision scores or labels available |
| Updated ablation results | **No** | No ablation implementation or raw outputs available |
| Verified reference database | Partially | Existing rendered references can be transcribed, but DOI-level validation requires source/BibTeX audit |
| No-APC target shortlist | Yes, with fee caveats | Official journal pages and current SCImago indicators reviewed |

## 4. Author materials required for a scientifically updated dataset

To produce a genuine updated dataset, the authors must upload one of the following:

1. The actual NS-3.40 project with all ActiveTrust source files, configuration files, patches, and build instructions; or
2. A complete experiment archive containing one row per run and configuration, random seeds, topology files, attack-placement files, per-node trust/detection logs, per-packet or per-epoch metrics, and the exact scripts used to produce each table and figure.

At minimum, the raw data must preserve `seed`, `method`, `N`, BHA fraction, attack model, attack placement, traffic parameters, protocol parameters, PDR, detection latency, recall, false-positive rate, AUC inputs, energy overhead, and lifetime. An Excel summary alone is insufficient because it cannot establish the per-run statistical provenance.

## 5. Submission-risk conclusion

The paper may be packaged as a **structural submission draft with source-derived figures**, but it must not claim that the GitHub repository provides reproducible ActiveTrust implementation or updated experimental evidence. The repository should either be upgraded with the real implementation and dataset before submission or be described accurately as an accompanying documentation repository rather than as the artifact that generated the reported results.
