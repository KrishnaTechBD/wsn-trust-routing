"""Canonical raw-run schema for ActiveTrust experiments."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable

REQUIRED_COLUMNS = [
    "seed", "method", "N", "field_width_m", "field_height_m", "bha_fraction",
    "bha_count", "attack_model", "attack_placement", "traffic_rate_packets_per_s",
    "packet_size_bytes", "epoch_duration_s", "alpha_T", "tau", "K_lock", "d_h_m",
    "p_hat", "M", "M_max", "w_h", "w_e", "channel_model", "packet_error_rate",
    "mac_retransmissions", "queue_size", "simulation_duration_s", "pdr_percent",
    "throughput_packets_per_s", "mean_delay_ms", "detection_rate_percent",
    "precision_percent", "recall_percent", "false_positive_rate_percent",
    "false_negative_rate_percent", "first_detection_epoch", "detection_latency_s",
    "auc", "probe_packets", "probe_bytes", "probe_tx_energy_j", "probe_rx_energy_j",
    "energy_overhead_percent_per_epoch", "first_node_death_epoch",
    "half_node_death_epoch", "benign_false_locks", "failed_run", "exclusion_reason",
]

IDENTITY_COLUMNS = ["seed", "method", "N", "bha_fraction", "attack_model", "attack_placement"]
PERCENT_COLUMNS = [
    "bha_fraction", "pdr_percent", "detection_rate_percent", "precision_percent",
    "recall_percent", "false_positive_rate_percent", "false_negative_rate_percent",
    "energy_overhead_percent_per_epoch", "packet_error_rate",
]
NONNEGATIVE_COLUMNS = [
    "seed", "N", "bha_count", "traffic_rate_packets_per_s", "packet_size_bytes",
    "epoch_duration_s", "alpha_T", "tau", "K_lock", "d_h_m", "p_hat", "M", "M_max",
    "w_h", "w_e", "mac_retransmissions", "queue_size", "simulation_duration_s",
    "throughput_packets_per_s", "mean_delay_ms", "first_detection_epoch",
    "detection_latency_s", "auc", "probe_packets", "probe_bytes", "probe_tx_energy_j",
    "probe_rx_energy_j", "first_node_death_epoch", "half_node_death_epoch",
    "benign_false_locks",
]

@dataclass(frozen=True)
class ValidationIssue:
    severity: str
    row: int | None
    column: str | None
    message: str


def missing_columns(columns: Iterable[str]) -> list[str]:
    present = set(columns)
    return [column for column in REQUIRED_COLUMNS if column not in present]
