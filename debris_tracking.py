"""Input helpers for the sample space-debris monitoring demo."""
import csv
from pathlib import Path


def load_tracking_csv(path):
    """Load rows from a CSV file and return dictionaries."""
    path = Path(path)
    with path.open("r", newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))
