"""Threshold-based close-approach flag for demonstration only."""


def classify_proximity(distance_km, threshold_km=1.0):
    """Return a simple label based on distance, not a true collision probability."""
    return "DEMO ALERT" if float(distance_km) <= float(threshold_km) else "NOMINAL"
