# ActiveTrust: IEEE-Style Peer-Review Report and Q1 Submission Roadmap

**Manuscripts reviewed:** `ActiveTrust_Final_Paper.pdf` and `ActiveTrust_Q1_WithFigures-1.pdf`  
**Review perspective:** IEEE journal reviewer in wireless-network security, trust management, and reproducible simulation research  
**Overall recommendation:** **Major revision / do not submit to a selective Q1 journal yet**

## 1. Executive assessment

The ActiveTrust manuscript presents a potentially publishable idea: proactively sending authenticated, data-sized probes through energy-aware routes, converting packet-forwarding behaviour into early evidence against black-hole nodes, and then using trust-filtered routing for data delivery. The manuscript is readable, has a clear system narrative, includes algorithms, reports ablation results, and attempts to address both detection speed and energy cost. The arithmetic behind several headline claims is internally consistent: the stated 81.1% latency reduction, 18.9% lifetime extension, 18.3% AUC improvement, and `M = 44` for `P_det = 0.99`, `p = 0.10` are numerically correct.

However, the current evidence does not yet support the manuscript’s strongest claims. The central detection-probability equation is used as if independently sampled routes were available, but the proposed routes are generated on one finite, correlated graph, are energy-biased, and are explicitly confined to a non-hotspot subgraph. More seriously, the manuscript does not yet explain how an end-to-end probe failure is attributed to a particular relay. Without a precise observation/localisation mechanism, the EMA trust score cannot be reconstructed from the described protocol, and the claimed false-positive and detection-rate results are difficult to audit.

The experimental section also needs a substantially stronger design. Fifty simulation runs are useful, but run count alone does not establish statistical validity. The manuscript needs exact attack procedures, raw per-run outputs, confidence intervals for differences, corrected multiple-comparison testing, effect sizes, a clearly defined ROC protocol, parameter sensitivity, realistic wireless-error scenarios, and stronger security baselines. The statement that all advantages are significant at `p < 0.001` is not sufficient and currently reads as overconfident because the paper does not report the test statistic, degrees of freedom, multiplicity correction, or raw observations.

The **Q1 draft is the better structural base** because it removes the severe out-of-order sections found in the final draft. Nevertheless, both PDFs retain visible float/caption problems, including a stray or duplicated figure-caption line before the proper topology caption, and both contain technical cross-reference inconsistencies. I would not send either version to an IEEE Q1 journal without a full scientific revision and a clean LaTeX rebuild.

## 2. Publication-readiness scorecard

| Dimension | Current assessment | Q1 readiness | Required action |
|---|---|---:|---|
| Problem importance | Relevant and technically meaningful | **Good** | Narrow the application claims and state the exact deployment setting |
| Core idea | Proactive probing plus energy-aware routing is promising | **Potentially strong** | Formalise the protocol and distinguish it from prior active probing, watchdog, and trust-routing work |
| Novelty evidence | Current related work is too short and makes an absolute gap claim | **Weak-to-moderate** | Build a systematic comparison matrix with verified primary sources |
| Mathematical correctness | Probe-count bound and route-domain definitions are under-specified | **Weak** | Replace the independence shortcut with graph/path-coverage analysis and clarify sink/hotspot handling |
| Security analysis | Mainly descriptive; no rigorous guarantees for adaptive, colluding, or selective attackers | **Weak** | Add a formal adversary model, propositions, attack cases, and explicit limitations |
| Protocol reproducibility | Algorithms are incomplete at the observation and route-repair level | **Weak** | Provide executable pseudocode, state transitions, packet formats, and failure handling |
| Experimental design | Good first simulation but too narrow for a selective journal | **Moderate** | Expand scenarios, baselines, sensitivity, link errors, scale, and adaptive attacks |
| Statistical analysis | 50 runs and CIs are positive, but inference is incomplete | **Weak-to-moderate** | Report paired design, exact tests, corrected p-values, effect sizes, and AUC uncertainty |
| IEEE presentation | Generally recognisable but not production-clean | **Moderate** | Rebuild with the official target template and repair captions, references, numbering, and floats |
| Reproducibility package | User indicates Overleaf/Excel materials, but those source files were not supplied here | **Not assessable** | Package code, seeds, raw data, scripts, environment, and DOI-archived release |

## 3. Principal strengths

The manuscript has a coherent problem-to-solution story. It identifies a real weakness of purely passive trust estimation—delayed evidence—and proposes to create controlled traffic that forces a forwarding decision before sensitive data routes are selected. That is a stronger conceptual framing than simply adding another trust score to a conventional routing protocol.

The paper also attempts to integrate three concerns that are often evaluated separately: detection latency, packet delivery, and energy balance. The use of a base station for global trust computation is realistic for gateway-centric WSN deployments, and the explicit acknowledgement that the design does not fit BS-free or fully distributed networks is helpful. The ablation study is directionally valuable because it tries to isolate probe indistinguishability, non-hotspot confinement, adaptive probe count, EMA trust, and route repair.

The reported values are presented consistently in the abstract, results, and conclusion. The arithmetic checks performed on the PDFs confirm the following values:

| Claim | Calculation from manuscript values | Assessment |
|---|---:|---|
| Detection-latency reduction | `(44.6 − 8.4) / 44.6 = 81.17%` | Consistent with 81.1% |
| Lifetime extension | `(371 − 312) / 312 = 18.91%` | Consistent with 18.9% |
| AUC improvement | `(0.983 − 0.831) / 0.831 = 18.29%` | Consistent with 18.3% |
| PDR advantage vs. PassiveTrust | `94.3 − 75.8 = 18.5` percentage points | Consistent |
| Probe count | `ceil(log(0.01)/log(0.90)) = 44` | Arithmetic is correct under the stated model |

These strengths justify a serious revision rather than abandonment of the idea. The main issue is not that the concept is uninteresting; it is that the current manuscript presents simulation claims as if the formal protocol and statistical evidence were already closed.

## 4. Major technical concerns requiring resolution

### 4.1 The detection-probability equation is not valid for the implemented route generator without a graph-coverage derivation

Equation (3),

\[
M \geq \left\lceil \frac{\log(1-P_{det})}{\log(1-p)} \right\rceil,
\]

is the familiar independent-trial expression. In this manuscript, however, `M` is the number of routes generated on one finite graph. Routes are not independent Bernoulli trials: they share nodes and edges, are selected by a maximum-bottleneck-energy procedure, and are influenced by prior energy deductions. The probability that a probe intersects a black-hole node depends on the actual route set and the adversarial placement, not only on the global fraction `p = f/N`.

There is an additional domain problem. The algorithm constructs `G' = G[V']` after removing the hotspot set, then calls `MaxMinEnergyPath(G', s_k, S)`. If the sink is represented as a graph vertex and belongs to the hotspot region—as the text suggests because the sink is at `(100,100)` and the hotspot is defined by distance to the sink—then `S` is not in `V'`, and the path call is undefined. If the sink is an external base-station endpoint, the paper must define the gateway/egress edges and explain whether the final hop is allowed to use hotspot nodes. The present language that routes are “exclusively” non-hotspot while also terminating at the sink is not sufficiently precise.

A stronger formulation should define the route set `R`, black-hole set `B`, and the route-intersection indicator:

\[
I_k(B)=\mathbf{1}[r_k\cap B\neq\varnothing].
\]

Under a pure black-hole attacker that drops every probe traversing it, the conditional detection event is determined by `\max_k I_k(B)`. For random attacker placement, estimate

\[
P_{det}(R)=\Pr_{B\sim \mathcal{D}_f}\left[\bigcup_{k=1}^{M}(r_k\cap B\neq\varnothing)\right]
\]

by Monte Carlo over the actual graph and route generator. If routes are intentionally diversified, quantify route overlap, node coverage, edge coverage, and the fraction of nodes reachable by at least one probe. Equation (3) can be retained only as a heuristic upper-level design rule, clearly labelled as such, not as a guarantee.

### 4.2 Non-hotspot confinement may make hotspot black holes invisible

The paper defines the hotspot region as nodes close to the sink and says probes are confined to non-hotspot nodes. If black holes are uniformly assigned over all `N` nodes, then a black hole in the excluded hotspot region cannot be traversed by a detection route and cannot be exposed by that route. In that case, using `p = f/N` in the detection formula overstates the effective sampling fraction. The paper must either restrict the attack domain to the probe-reachable subgraph, allow a precisely defined sink-access segment, or provide a separate detection guarantee for hotspot adversaries.

This point is central because the manuscript’s strongest novelty claim is that energy balancing and high detection probability are achieved simultaneously. The paper must show the trade-off explicitly. Report results for at least: all-node attacks, non-hotspot-only attacks, hotspot-only attacks, attacks concentrated on high-betweenness nodes, and attacks placed on probe-route intersections.

### 4.3 The protocol does not yet explain how a failed multi-hop probe identifies the malicious node

The trust score uses `c_i^+` and `c_i^-` for each node, but the described mechanism mainly reports probe delivery or failure. An end-to-end failure establishes that a route failed; it does not, by itself, identify which relay dropped the packet. A route with six relays and one failed probe has multiple possible causes: a malicious drop, a collision, a channel error, a queue overflow, a retransmission limit, or a downstream node failure.

The authors must specify one of the following mechanisms and include its cost:

| Possible mechanism | What must be specified |
|---|---|
| Per-hop ACK/sequence tracing | ACK semantics, timeout thresholds, energy cost, and false-positive behaviour |
| Watchdog observation | Which node watches which relay, how overhearing works under 802.15.4, and how hotspot overhead is avoided |
| Authenticated hop receipts | Packet format, keying, replay protection, and whether receipts reveal probe identity |
| Route-level blame assignment | A probabilistic attribution model and an analysis of its error rate |
| BS-side simulator oracle | Acceptable only as an experimental oracle; it cannot be presented as an implementable protocol without a deployable equivalent |

The manuscript currently claims that the adversary’s forwarding behaviour is the primary signal but does not define the observation operator that turns that behaviour into a per-node trust update. This is a major reproducibility and validity issue.

### 4.4 “Indistinguishable” is currently a design assertion, not a formal security property

Padding probes to the data-packet size and placing the MAC at the same offset provide **syntactic similarity**, but they do not automatically provide traffic-analysis resistance. A local adversary may observe the route beacon, route identifier, timing, packet-generation frequency, nonce usage, MAC verification behaviour, retransmission patterns, or the fact that the BS sends a known number of probes per epoch. The manuscript also states that the group key is held only by the BS and sink, which means ordinary forwarding nodes cannot verify the MAC; the protocol must explain why this is operationally safe and how the sink reports success.

The authors should define the adversary’s observable transcript and state exactly which observations are excluded. A useful minimum is to evaluate three attacker classes: a content-blind dropper, an attacker that recognises probes from metadata, and an adaptive attacker that forwards probes but drops application data. The current “w/o probe indistinguishability” ablation is not enough unless the implementation of the adversary is given in detail and the full protocol is tested against an attacker that learns from route announcements.

### 4.5 The use of the Byzantine bound `f < N/3` is not justified by the protocol

The manuscript invokes the classical `f < N/3` threshold but does not implement consensus, quorum agreement, or a distributed Byzantine fault-tolerant protocol. A centralised base station, trusted sink, and route-level trust filter constitute a different model. Black-hole forwarding is a packet-delivery attack, not automatically a Byzantine-consensus problem. The bound should either be removed from the threat model or replaced with an explicit assumption such as “the evaluation considers `f/N ∈ {0.05, 0.10, 0.20, 0.30}` compromised nodes.” If the authors retain Byzantine terminology, they must define the property being guaranteed and prove it under the stated communication and trust assumptions.

### 4.6 Security analysis is missing where a Q1 reviewer will expect it

The paper needs a dedicated security/correctness section rather than relying only on the threat-model paragraph. At minimum, it should analyse the following claims:

| Claim to analyse | Required result |
|---|---|
| Probe authenticity | Why a non-BS node cannot forge an accepted probe or alter its route identity without detection |
| Replay resistance | Why nonce reuse, delayed probes, and duplicate delivery do not inflate trust |
| Selective forwarding | Detection behaviour when the attacker drops data but forwards probes |
| On–off attacks | Detection under alternating good/bad epochs and the effect of `α_T` and `K_lock` |
| Collusion | What can and cannot be detected when multiple relays coordinate |
| False positives | Probability of locking an honest node under packet loss and retransmissions |
| Route repair safety | Whether a route repair can reintroduce a node with low trust or create loops |
| Hotspot adversaries | Whether the claimed guarantee applies to nodes excluded from probe routes |

The correct outcome may be a bounded guarantee rather than universal security. A narrower, provable claim is preferable to “near-certain exposure regardless of adversary behavioural history.”

### 4.7 The experimental baselines are not yet strong enough for a selective security journal

AODV and DSR are useful generic baselines, but they are not sufficient by themselves for a paper whose contribution is secure trust-based routing. The custom `PassiveTrust` baseline is not defined with enough detail to establish fairness. The authors should add at least two security-oriented baselines from the verified recent literature, preferably one watchdog/reputation method and one selective-forwarding or active-detection method. Each baseline must use the same topology, traffic, energy model, attack placement, random seeds, simulation duration, and route-repair budget.

The paper also needs to explain whether ActiveTrust and each baseline receive the same information. If ActiveTrust uses a base-station view of exact probe outcomes while PassiveTrust uses only noisy forwarding observations, that may be a legitimate design difference, but it must be stated and evaluated as an architectural trade-off rather than presented as an apples-to-apples algorithmic comparison.

### 4.8 Statistical reporting is incomplete and overstates what `p < 0.001` establishes

The current text says that Welch’s t-test rules out chance findings. That interpretation is too strong. A small p-value rejects a specified null under the test assumptions; it does not establish that the implementation is correct, that the effect is practically important, or that all unreported comparisons are robust. The paper also makes many comparisons across methods, attack densities, metrics, and ablations, so multiplicity must be addressed.

The revised paper should report the following:

| Required item | Recommended implementation |
|---|---|
| Unit of analysis | Treat each random seed as one independent run; avoid treating packets or epochs as independent replicates |
| Pairing | Use identical seeds/topologies across methods when possible and analyse paired differences |
| Effect sizes | Report absolute PDR difference, relative change, Cohen’s *d* or Hedges’ *g*, and a nonparametric effect size where appropriate |
| Multiple comparisons | Apply Holm or Benjamini–Hochberg correction and state the family of tests |
| P-values | Report exact values or bounded values with test statistic and degrees of freedom |
| Non-normal metrics | Use bootstrap confidence intervals or permutation tests for PDR, lifetime, latency, and energy overhead if assumptions are doubtful |
| ROC/AUC | State whether curves are pooled, macro-averaged, or seed-averaged; provide bootstrap CI and a paired AUC comparison |
| Missing/failed runs | Report all excluded runs and the exclusion rule before analysis |

Table IV claims 95% confidence intervals in its caption but presents only point estimates. That inconsistency must be corrected.

### 4.9 The parameter and scenario space is too narrow for the external claims

The paper evaluates one network size, one field size, one radio range, one static topology model, one main traffic setting, one fixed forgetting factor, one trust threshold, and one nominal energy configuration. The threats-to-validity section acknowledges some limitations, but the conclusion still makes broad industrial and safety-critical claims.

At minimum, add a sensitivity matrix covering `N`, node density, sink position, initial-energy heterogeneity, packet-generation rate, channel error rate, MAC retransmission limit, `α_T`, `τ`, `K_lock`, `P_det`, `M_max`, hotspot radius, and route-overlap constraints. Include static and imperfect-link scenarios. Mobility can remain out of scope if stated clearly, but then avoid general claims about mobile IoT.

The manuscript reports collusion detection, on–off resistance, and a “binary clarity” advantage, yet the setup does not define the corresponding attacker algorithms. These results are not credible until the attack state machine, timing, selection rule, and ground-truth labels are published.

## 5. Version comparison and recommended base

### 5.1 Comparison of the two supplied PDFs

| Aspect | `ActiveTrust_Final_Paper.pdf` | `ActiveTrust_Q1_WithFigures-1.pdf` | Recommendation |
|---|---|---|---|
| Scientific content | Contains the full scientific core plus additional late sections | Contains the same core results and a cleaner ending | Use Q1 draft as base, then restore useful material in the correct locations |
| Section order | Severe defect: `X. Conclusion` is followed by `XIII. Sensitivity Analysis`, `XII. Practical Deployment Considerations`, and `XI. Computational Complexity Analysis` | Ends cleanly after `X. Conclusion` and references | Keep Q1 order; integrate complexity and deployment before conclusion |
| Figures/captions | Stray/duplicated topology-caption evidence | Same early-page caption problem remains | Rebuild all floats with one `figure` environment per figure and automatic `\label`/`\ref` |
| Cross-references | Algorithm 2 refers to “Eq. (7)” while the visible cost equation is numbered (6) | Same inconsistency | Fix before any submission |
| References heading | Looks normal in extracted text | Extracted text shows a leading punctuation artifact near `. REFERENCES` | Recompile from clean source and inspect the final PDF |
| Layout | Large whitespace and split algorithm | Similar whitespace and split algorithm | Improve float placement, but do not manually distort IEEE margins |
| Scientific interpretation | Additional text after the conclusion makes the structure look unfinished | Cleaner, but omits some useful complexity/deployment content | Merge the missing content into dedicated pre-conclusion sections |

### 5.2 Recommended final IEEE structure

Use the following order in the source manuscript:

1. **Introduction** — problem, limitations of existing work, research questions, contributions.
2. **Related Work and Positioning** — security routing, trust/watchdog methods, active probing, energy-aware routing, and a comparison table.
3. **System and Threat Model** — graph, energy, communication, BS assumptions, attacker capabilities, excluded attacks, and notation.
4. **ActiveTrust Protocol** — epoch state machine, probe packet, route generation, probe delivery observation, trust update, locking, and route repair.
5. **Security and Correctness Analysis** — authenticity, replay resistance, detection coverage, false positives, selective forwarding, collusion limits, and complexity.
6. **Experimental Methodology** — simulator version/commit, topology generation, traffic, attack algorithms, baselines, parameters, seeds, metrics, and statistical protocol.
7. **Results and Discussion** — PDR, detection, ROC, energy/lifetime, ablations, sensitivity, scale, and interpretation.
8. **Limitations and Reproducibility** — BS dependence, link model, route independence, missing testbed validation, and artifact link.
9. **Conclusion**.
10. **References**.

Do not place a sensitivity section, deployment section, or complexity section after the conclusion. The information can remain, but it must be integrated into the correct scientific locations.

## 6. Concrete revision plan before submission

### Priority A: validity blockers

| ID | Revision | Acceptance criterion |
|---|---|---|
| A1 | Redefine the probe-coverage model and replace or qualify Eq. (3) | A reviewer can compute detection probability from the route set and attack placement without assuming independent routes |
| A2 | Resolve sink/hotspot graph inconsistency | `G'`, the sink endpoint, final-hop policy, and route domain are formally defined and executable |
| A3 | Define per-node blame attribution | A failed probe has a reproducible mapping to `c_i^+`/`c_i^-`, including channel-loss cases |
| A4 | Define adaptive attacker algorithms | Pure BHA, selective forwarding, on–off, probe-aware, and colluding attacks are fully specified |
| A5 | Add security/correctness analysis | At least bounded propositions and explicit non-guarantees are included |
| A6 | Verify every reference | Each citation has a real DOI/URL, correct venue metadata, and is relevant; remove any unverified records |

### Priority B: Q1-level empirical strengthening

| ID | Revision | Acceptance criterion |
|---|---|---|
| B1 | Add strong security baselines | At least two relevant secure-routing/trust/active-detection baselines are implemented or rigorously justified as unavailable |
| B2 | Add parameter sensitivity | Sweeps for `α_T`, `τ`, `P_det`, `M_max`, hotspot radius, and route overlap are reported |
| B3 | Add wireless realism | Results under packet loss, asymmetric links, queue contention, retransmission limits, and varied traffic rates are included |
| B4 | Add scale and placement tests | Multiple `N`/density values, sink positions, hotspot-only attacks, and high-betweenness attacks are evaluated |
| B5 | Rework statistics | Paired seeds, corrected multiplicity, exact tests, effect sizes, and AUC confidence intervals are reported |
| B6 | Release reproducibility artifacts | Code, seeds, raw logs, scripts, parameter files, and environment are archived with a persistent identifier |

### Priority C: presentation and IEEE compliance

| ID | Revision | Acceptance criterion |
|---|---|---|
| C1 | Rebuild from the official target-journal template | Margins, typography, headings, captions, and author block match the selected journal’s current instructions [2] |
| C2 | Repair all figure and algorithm floats | No duplicate caption text, stale figure numbers, broken labels, or excessive blank space |
| C3 | Correct equation and figure references | Every `\ref` points to the intended object; no “Eq. (7)” when the formula is Eq. (6) |
| C4 | Make tables self-contained | Every table includes metric definition, unit, uncertainty type, sample size, and statistical note |
| C5 | Tighten claims | Replace “regardless of adversary behavioural history” and “near-certain” with claims supported by the tested threat model |
| C6 | Improve related work | Add recent, verified primary studies and explain precisely how ActiveTrust differs |

## 7. Recommended result presentation

The revised results section should begin with a compact experimental matrix, not with the headline numbers. Then present the evidence in the following order:

| Subsection | Main question | Required evidence |
|---|---|---|
| Detection coverage | Does ActiveTrust actually reach black-hole nodes? | Route/node/edge coverage, hotspot versus non-hotspot placement, Monte Carlo detection probability |
| Detection correctness | Does it identify the responsible node without harming benign nodes? | Precision, recall, FPR, FNR, confusion matrices, false-lock rate under link loss |
| Data delivery | Does early detection improve application traffic? | PDR, delay, throughput, route length, delivery CIs across attack densities |
| Cost | What does probing consume? | Probe packets, bytes, transmissions, receive cost, energy denominator, per-node energy distribution |
| Lifetime | Does the energy policy prevent hotspot depletion? | First-node and half-node death, residual-energy curves, hotspot/non-hotspot lifetime comparison |
| Adversarial adaptation | Does the method survive smarter attackers? | Probe-aware, selective, on–off, colluding, and route-aware attack results |
| Ablation and sensitivity | Which design choices matter and how brittle are they? | Component ablations plus parameter sweeps, with uncertainty and corrected testing |

The paper should show per-node energy distributions and route-overlap statistics. A single network-lifetime number cannot establish that non-hotspot confinement balances energy; the reviewer needs to see whether probe traffic merely moves depletion to a different set of nodes.

## 8. Reproducibility and Overleaf package checklist

The supplied PDFs allow review of the rendered paper, but the following source materials were not available in this session: `main.tex`, figure source files, the dataset Excel workbook, simulator code, raw run outputs, seed files, the cover letter, and the bibliography source. Therefore, I could not verify whether the visible formatting defects originate in the LaTeX source, an Office/PDF conversion step, or a stale figure asset.

For the next submission, the artifact directory should contain:

```text
activetrust-artifact/
├── README.md
├── LICENSE
├── paper/
│   ├── main.tex
│   ├── references.bib
│   ├── figures/
│   └── tables/
├── simulator/
│   ├── ns-3.40-commit.txt
│   ├── patches/
│   ├── build-instructions.md
│   └── source/
├── experiments/
│   ├── configs/
│   ├── seeds/
│   ├── attack-models/
│   ├── run-scripts/
│   └── raw-results/
├── analysis/
│   ├── statistical-tests/
│   ├── figure-generation/
│   └── table-generation/
└── environment/
    ├── Dockerfile or environment.yml
    └── version-manifest.txt
```

The Excel workbook should be treated as a convenience output, not the primary data source. Store raw results in CSV/JSON with one row per run, configuration, seed, method, metric, and attack condition. The README should map every paper table and figure to one command and identify the expected output checksum. IEEE encourages authors to share data, code, and other research outputs, and identifies repositories such as figshare, Zenodo, and Dryad for data and Code Ocean for executable computational artifacts [3].

## 9. IEEE Q1 submission guideline for the next cycle

### 9.1 Select the journal by contribution fit, not by the word “Q1” alone

“Q1” is not a universal IEEE designation; it is a journal ranking that depends on the database, subject category, and reporting year. Before submission, verify the current quartile in the database required by your institution and read the target journal’s latest Guide for Authors. Build a shortlist of no more than three realistic venues and score each against scope, article type, page limits, open-access requirements, review speed, and recent papers on secure WSN/IoT routing.

Potential journal families to investigate are IEEE Transactions on Dependable and Secure Computing, IEEE Transactions on Information Forensics and Security, IEEE Transactions on Network and Service Management, IEEE Internet of Things Journal, and IEEE Transactions on Mobile Computing. This is a **fit shortlist, not a claim that every venue is Q1 in every category or year**. The present manuscript is most naturally positioned as a secure-networking and dependable-routing paper; it is not yet sufficiently cryptographic for a pure information-forensics positioning unless the security analysis is materially strengthened.

### 9.2 Prepare the manuscript package

Use the official IEEE template selector and the exact template required by the chosen journal. IEEE states that its templates help place article elements correctly and guide stylistic details such as author lists, abbreviations, and acronyms [2]. Do not manually alter margins, font sizes, column widths, or reference spacing to force a page count. Use automatic equation, figure, table, and section references throughout.

The submission package should contain the clean manuscript PDF, editable LaTeX source, bibliography, vector or sufficiently high-resolution figures, supplementary material, data/code availability statement, conflict-of-interest declaration if requested, author contribution statement if requested, and a cover letter tailored to the journal. The cover letter should state the problem, the one-sentence methodological novelty, the strongest validated evidence, the scope fit, the artifact availability, and any prior related publication. It should not claim “first,” “guaranteed,” or “near-certain” unless the manuscript proves those statements.

### 9.3 Complete the ethics and originality checks

IEEE requires that submitted work be original and not simultaneously under review elsewhere. Prior related publications or submissions must be disclosed, cited, and distinguished clearly; plagiarism and unattributed reuse are unacceptable [1]. Before uploading, run a reference audit, similarity check, author-order confirmation, funding disclosure, conflict-of-interest check, and prior-publication comparison. If any version of ActiveTrust has appeared in a workshop, conference, repository, thesis, or earlier journal submission, explain exactly what is new in the present manuscript.

### 9.4 Include a reproducibility statement

Use a concise statement such as the following only if it is true:

> “The NS-3.40 implementation, configuration files, random seeds, raw per-run metrics, statistical-analysis scripts, and figure-generation scripts are available at [persistent repository URL] under [license]. The artifact includes a container/environment manifest and reproduces Tables II–IV and Figures 4–8 using the commands documented in `README.md`.”

If the code cannot be released, say why and provide the strongest permitted alternative, such as anonymised raw outputs, a detailed pseudocode supplement, or an institutional artifact review. Do not describe an Excel file alone as a reproducibility package.

### 9.5 Cover-letter positioning

The cover letter should position the paper around a **bounded, evidence-backed contribution**:

> “ActiveTrust introduces a base-station-assisted proactive probing protocol for black-hole detection in static, gateway-centric WSNs. Its contribution is the joint design of probe-based evidence, energy-aware route construction, and trust-filtered data routing, evaluated under controlled NS-3 scenarios with released seeds and analysis scripts.”

The letter should also disclose limitations: centralised BS dependence, static topology, finite network scale, route-correlation effects, and the scope of the attacker evaluation. A candid limitation statement improves credibility and prevents the editor from discovering an obvious overclaim during triage.

## 10. Final go/no-go decision

**Current decision: no-go for immediate Q1 submission.** The manuscript is not rejected as an idea; it is **not yet ready as evidence**. The minimum go/no-go gate is:

| Gate | Must be true before submission |
|---|---|
| Mathematical gate | Probe coverage is defined on the actual route set; sink/hotspot handling is executable |
| Attribution gate | The paper explains how a failed probe produces per-node evidence and quantifies false positives |
| Security gate | Adaptive, selective, on–off, and colluding attacks are defined and evaluated within explicit guarantees |
| Experimental gate | Strong baselines, sensitivity, wireless imperfections, and attack-placement tests are included |
| Statistics gate | Raw per-run data, corrected inference, effect sizes, and AUC uncertainty are reported |
| Reproducibility gate | Code/configuration/seeds/raw results/analysis scripts are archived and referenced |
| IEEE gate | Clean rebuild from the target journal template; no stale captions, wrong numbering, or out-of-order sections |
| Ethics gate | All prior work and submissions are disclosed, and every reference is verified [1] |

If the authors complete Priority A and the essential parts of Priority B, the paper could become a credible Q1 candidate. Without those changes, an editor or reviewer is likely to classify the work as an interesting simulation proposal with insufficient formal and experimental validation.

## References

[1]: https://journals.ieeeauthorcenter.ieee.org/become-an-ieee-journal-author/publishing-ethics/guidelines-and-policies/submission-and-peer-review-policies/ "IEEE Submission and Peer Review Policies"
[2]: https://journals.ieeeauthorcenter.ieee.org/create-your-ieee-journal-article/authoring-tools-and-templates/tools-for-ieee-authors/ieee-article-templates/ "IEEE Article Templates"
[3]: https://journals.ieeeauthorcenter.ieee.org/create-your-ieee-journal-article/research-reproducibility/ "IEEE Research Reproducibility"
[4]: https://ieeeauthorcenter.ieee.org/ "IEEE Author Center"
