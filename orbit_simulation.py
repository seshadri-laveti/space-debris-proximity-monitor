"""Toy trajectory adjustment for visualization only; not a physical orbit solver."""


def illustrative_offset(position, offset_km=2.0):
    """Return a copy of a Cartesian position with a small illustrative y offset."""
    x, y, z = map(float, position)
    return (x, y + float(offset_km), z)
