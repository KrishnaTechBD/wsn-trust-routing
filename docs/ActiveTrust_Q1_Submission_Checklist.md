# ActiveTrust Q1 Submission Checklist

## Scientific validity gate

- [ ] Define the actual probe-observation and per-node blame mechanism that produces `c_i+` and `c_i−`.
- [ ] Resolve whether the sink is in the hotspot set and specify the exact final-hop route policy.
- [ ] Replace the independent-route interpretation of Eq. (3) with route-set coverage analysis or clearly label Eq. (3) as a heuristic.
- [ ] Evaluate black holes in all-node, hotspot-only, non-hotspot-only, high-betweenness, and route-intersection placements.
- [ ] Provide exact algorithms for pure black hole, selective-forwarding, on–off, probe-aware, and colluding attackers.
- [ ] Add bounded security/correctness analysis for authenticity, replay, false positives, route repair, and adaptive attackers.

## Experimental gate

- [ ] Add at least two verified security-oriented baselines beyond AODV/DSR and define PassiveTrust precisely.
- [ ] Use common seeds/topologies across methods where possible and report paired differences.
- [ ] Add sensitivity results for EMA factor, trust threshold, lock window, probe target, route cap, hotspot radius, and route overlap.
- [ ] Add link-loss/asymmetric-link, queue contention, traffic-rate, retransmission, density, and network-scale scenarios.
- [ ] Report raw per-run metrics, exact/bounded p-values, effect sizes, multiplicity correction, and AUC confidence intervals.
- [ ] Correct Table IV so its uncertainty claim matches the values actually shown.

## Source/reproducibility gate

- [ ] Rebuild from the official target-journal IEEE template.
- [ ] Fix duplicate/stale figure captions, equation cross-references, section numbering, and excessive blank space.
- [ ] Verify every reference with DOI/URL, venue, volume, issue, pages, year, and relevance.
- [ ] Release NS-3.40 code, commit/patch information, configuration files, seeds, raw outputs, analysis scripts, and figure-generation scripts.
- [ ] Add a README mapping every table/figure to one reproducible command and expected output.
- [ ] Archive the artifact at Zenodo, figshare, Dryad, Code Ocean, or an equivalent persistent repository.

## Submission gate

- [ ] Select the target journal based on scope and current quartile/category, not only the Q1 label.
- [ ] Check the target journal’s current page limit, article type, template, review policy, open-access terms, and supplementary-material rules.
- [ ] Submit to only one active journal target unless the venue explicitly permits otherwise.
- [ ] Disclose all prior conference, workshop, thesis, preprint, or submitted versions and explain the technical differences.
- [ ] Prepare a cover letter that states the bounded contribution, strongest validated evidence, scope fit, artifact link, and limitations.
- [ ] Perform a final author-order, funding, conflict-of-interest, similarity, reference, and PDF preflight check.

## Recommended decision

**Do not submit immediately.** Submit after the mathematical, attribution, security, statistics, reproducibility, and IEEE-format gates are all complete. Use `ActiveTrust_Q1_WithFigures-1.pdf` as the structural base, but rebuild the paper from source rather than editing the exported PDF.
