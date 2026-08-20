# ActiveTrust repository and journal-policy findings

## Repository audit

| Item | Finding |
|---|---|
| Repository URL | https://github.com/KrishnaTechBD/wsn-trust-routing |
| Audited commit | `4843a0337a86592875cc39dcf897aa109d7f4cd6` |
| Visible history | Shallow clone shows one visible commit; GitHub page reports 8 commits total |
| Tracked implementation | No `src/`, `tests/`, `notebooks/`, `data/`, `results/`, or simulator code is tracked in the audited commit |
| Actual top-level files | README/docs, license, citation metadata, requirements, and a file named `wsn-trust-routing` containing a directory-tree description |
| `.gitignore` | Explicitly ignores `data/`, `results/`, and `logs/` |
| Dependencies | pandas 2.2.1, scikit-learn 1.4.1, matplotlib 3.8.3, pytest 7.4.4; no NS-3, no simulator binding, no notebook dependency, no LaTeX toolchain |
| Reproducibility command | `reproducibility.md` says `python src/main.py` and `pytest tests/ -v`, but those paths are absent in the tracked clone |
| Seed policy | Documentation says all randomized experiments should use `SEED=42`, which conflicts with the paper’s claim of 50 independent random seeds unless a separate experiment package exists |
| Core algorithm in repository docs | Composite trust formula `T(n)=\alpha DT(n)+\beta IT(n)e^{-\lambda t}` with `\alpha=0.6`, `\beta=0.4`, `\lambda=0.05` |
| README results | Reports a different project framing and different headline values: Composite Trust Score accuracy/F1 0.91 and PDR 94.7%; SecLEACH PDR 79.8%; Standard LEACH PDR 61.3% |
| ActiveTrust paper implementation | The repository does not contain the ActiveTrust probe-count algorithm, MaxMinEnergyPath implementation, EMA trust code, NS-3 setup, raw results, or figure-generation scripts needed to validate the supplied paper’s 94.3%, 8.4/44.6 epochs, 18.9%, and AUC 0.983 claims |

## Journal-policy findings

1. [IEEE Internet of Things Journal author guidelines](https://ieee-iotj.org/guidelines-for-authors/) state that Traditional submission requires no OA payment, while mandatory page charges apply at $175 per page beyond the first eight published pages. The page charge is therefore a possible cost even under a no-APC Traditional route.
2. The same IEEE IoT Journal page describes a hybrid model, with an OA fee listed separately from the Traditional route. The target should be treated as “no mandatory APC under Traditional submission,” not “zero possible publication cost.”
3. The official IEEE Computer Society page for TDSC was not text-extractable in the browser session; its official author-information materials should be checked directly before selection, especially page limits and overlength charges.
4. Any final shortlist must distinguish: mandatory APC, optional OA fee, mandatory overlength/page charges, color charges, and institutional agreements. “No APC” cannot safely be stated without checking the target’s current author page and submission form.

## Critical conclusion

The public GitHub repository is currently a documentation scaffold/project placeholder, not an auditable implementation of the ActiveTrust paper. It is not scientifically valid to regenerate or “update” the paper’s dataset from this repository alone. The final submission package can include a clearly labelled repository-audit report and an Overleaf structural package, but it must not invent updated experimental observations. To create a genuinely updated dataset and figures, the authors must supply the missing simulator code, raw outputs, seed/configuration files, or an authoritative experiment archive.

## Additional official journal findings

3. [IEEE Transactions on Network and Service Management policies](https://www.comsoc.org/publications/journals/ieee-tnsm/policies-guidelines) state that Traditional submission requires no OA payment, but the journal allows up to 10 free published pages and applies a mandatory US$220 charge for each page beyond 10, up to 16 pages. The OA fee listed for 2026 submissions is US$2800. TNSM is a plausible scope fit if the paper is framed around network/service management and operational routing management rather than only attack detection.
4. [IEEE Transactions on Information Forensics and Security](https://signalprocessingsociety.org/publications-resources/ieee-transactions-information-forensics-and-security/ieee-transactions) covers information security and systems applications and explicitly encourages reproducible research by publishing the code and data used to produce figures and tables. It is a plausible security-oriented target only after the paper’s threat model, security argument, and reproducibility package are substantially strengthened.

## Shortlist interpretation

The current evidence supports a **Traditional, no-OA-APC route** for IEEE IoT Journal and IEEE TNSM, but neither is zero-cost in all cases because mandatory overlength/page charges may apply. TIFS is a potential security target, but its current fee/page policy requires checking the official author-information document before submission. TDSC remains a high-fit target, but its exact current author charges must be verified from the official author-information page rather than inferred from secondary snippets.

## Full Git history audit

The repository was fetched with full history. The public history contains eight commits, but the union of all historical paths is still limited to the same documentation, metadata, dependency, and placeholder-tree files. No historical commit contains `src/`, `tests/`, `notebooks/`, `data/`, `results/`, NS-3 code, raw outputs, or figure-generation scripts. Therefore, the missing ActiveTrust implementation and dataset were not merely removed from the current branch; they are absent from the complete public Git history inspected.

## Figure assets extracted from the supplied Q1 PDF

The Q1 PDF contains eight embedded raster assets. Their internal captions use a different numbering sequence from the running paper captions:

| Extracted asset | Visual content | Embedded internal caption number | Recommended canonical LaTeX figure label |
|---|---|---:|---|
| `q1_asset-000.png` | Topology / hotspot partition / detection routes | Fig. 6 | `fig:topology` |
| `q1_asset-001.png` | ActiveTrust protocol flowchart | Fig. 7 | `fig:flowchart` |
| `q1_asset-002.png` | EMA trust convergence | Fig. 8 | `fig:trust-convergence` |
| `q1_asset-003.png` | PDR vs. BHA fraction | Fig. 1 | `fig:pdr` |
| `q1_asset-004.png` | Detection latency | Fig. 2 | `fig:detection-latency` |
| `q1_asset-005.png` | ROC curves | Fig. 4 | `fig:roc` |
| `q1_asset-006.png` | Energy overhead and network lifetime | Fig. 3 | `fig:energy-lifetime` |
| `q1_asset-007.png` | Ablation study | Fig. 5 | `fig:ablation` |

The embedded captions should be cropped or removed before the assets are inserted into LaTeX, because LaTeX will provide the canonical caption once. The flowchart also contains source-level notation such as `V\H`, `T_ack`, and `c_i^-` that should be reconciled with the manuscript’s exact notation before final submission.

## Current quartile indicators

5. [SCImago listing for IEEE TNSM](https://www.scimagojr.com/journalsearch.php?q=7200153156&tip=sid) displays **SJR 2025: 1.389, Q1**.
6. [SCImago listing for IEEE IoT Journal](https://www.scimagojr.com/journalsearch.php?q=21100338350&tip=sid) displays **SJR 2025: 2.144, Q1** and shows Q1 across the listed 2025 subject categories. The page also describes scope areas including sensor networks, resource-constrained networks, IoT security, and privacy-preserving protocols.

These are SCImago/Scopus-derived quartile indicators, not a guarantee of the authors’ institution-specific JCR quartile. The final submission decision should verify the ranking database required by the authors’ institution.

## Crop verification

The two inspected caption-free assets retain their plot/flowchart content after cropping. The flowchart still contains notation that must be checked against the paper before submission: `V\\H` should match the manuscript’s `V\\setminus H`, the timeout symbol `T_ack` is not defined in the paper, and the decision path appears to increment `c_i^-` from an end-to-end ACK failure without showing how the responsible relay is identified. These are scientific consistency issues, not merely graphics issues.
