import json
from pathlib import Path


def test_total_requests():
    """Verifies criterion 1: total_requests is the correct count of log lines."""
    data = json.loads(Path("/app/report.json").read_text())
    assert data["total_requests"] == 6


def test_unique_ips():
    """Verifies criterion 2: unique_ips is the number of distinct IPs."""
    data = json.loads(Path("/app/report.json").read_text())
    assert data["unique_ips"] == 3


def test_top_path():
    """Verifies criterion 3: top_path is the most requested URL."""
    data = json.loads(Path("/app/report.json").read_text())
    assert data["top_path"] == "/index.html"
