import json
from pathlib import Path

def test_report_exists():
    """The agent produced a report file."""
    assert Path("/app/report.json").exists(), "no report.json found"

def test_report_content():
    """The report file contains correct and accurate JSON data."""
    with open("/app/report.json") as f:
        data = json.load(f)
    
    # Values mapped directly to the provided access.log fixture
    assert data.get("total_requests") == 6, f"Expected 6 total_requests, got {data.get('total_requests')}"
    assert data.get("unique_ips") == 3, f"Expected 3 unique_ips, got {data.get('unique_ips')}"
    assert data.get("top_path") == "/index.html", f"Expected top_path to be '/index.html', got {data.get('top_path')}"