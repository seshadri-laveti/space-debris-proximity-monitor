"""Simple Cartesian relative-proximity calculations for educational use."""
import math


def separation_km(satellite_position, debris_position):
    """Return Euclidean separation in km for two 3D Cartesian positions."""
    return math.sqrt(sum((float(a) - float(b)) ** 2
                         for a, b in zip(satellite_position, debris_position)))


def relative_speed_km_s(satellite_velocity, debris_velocity):
    """Return relative speed magnitude in km/s for two 3D velocity vectors."""
    return math.sqrt(sum((float(a) - float(b)) ** 2
                         for a, b in zip(satellite_velocity, debris_velocity)))


def estimate_velocity(rows, prefix):
    """Estimate sample Cartesian velocity using consecutive rows and time in seconds.

    Returns one velocity vector per row; the first row uses the next sample.
    This is a simple finite-difference demo, not an orbital propagation method.
    """
    if len(rows) < 2:
        return [(0.0, 0.0, 0.0) for _ in rows]

    positions = [
        (float(r[f"{prefix}_x_km"]), float(r[f"{prefix}_y_km"]),
         float(r[f"{prefix}_z_km"]))
        for r in rows
    ]
    times = [float(r["time_s"]) for r in rows]
    velocities = []
    for i in range(len(rows)):
        left, right = (0, 1) if i == 0 else ((len(rows)-2, len(rows)-1) if i == len(rows)-1 else (i-1, i+1))
        dt = times[right] - times[left]
        if dt == 0:
            velocities.append((0.0, 0.0, 0.0))
        else:
            velocities.append(tuple((positions[right][j] - positions[left][j]) / dt for j in range(3)))
    return velocities
