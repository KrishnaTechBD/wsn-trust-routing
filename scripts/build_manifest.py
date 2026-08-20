#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXCLUDE = {".git", "__pycache__", ".pytest_cache", "*.egg-info"}

def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()

files = []
for path in sorted(ROOT.rglob("*")):
    if not path.is_file() or any(part in EXCLUDE for part in path.parts):
        continue
    files.append({"path": str(path.relative_to(ROOT)), "sha256": sha256(path), "bytes": path.stat().st_size})

payload = {
    "package": "ActiveTrust GitHub Refinement Pack",
    "version": "0.1.0",
    "raw_dataset_status": "pending_author_archive",
    "reported_results_status": "reported_not_regenerated",
    "files": files,
}
(ROOT / "artifacts" / "manifest.json").write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
print(f"wrote {len(files)} file records")
