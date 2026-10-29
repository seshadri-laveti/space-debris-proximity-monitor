"""Run the sample space-debris proximity analysis."""
from pathlib import Path
from debris_tracking import load_tracking_csv
from proximity_analysis import separation_km, estimate_velocity, relative_speed_km_s
from collision_risk import classify_proximity

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "sample_data.csv"
DEMO_THRESHOLD_KM = 1.0


def main():
    rows = load_tracking_csv(DATA)
    sat_vel = estimate_velocity(rows, "sat")
    debris_vel = estimate_velocity(rows, "debris")

    print("SPACE DEBRIS PROXIMITY MONITOR — EDUCATIONAL DEMO")
    print("Input data: synthetic sample coordinates; not operational tracking data.")
    print(f"Demo threshold: {DEMO_THRESHOLD_KM:.2f} km")
    print("-" * 72)
    for i, row in enumerate(rows):
        sat = (row["sat_x_km"], row["sat_y_km"], row["sat_z_km"])
        debris = (row["debris_x_km"], row["debris_y_km"], row["debris_z_km"])
        distance = separation_km(sat, debris)
        rel_speed = relative_speed_km_s(sat_vel[i], debris_vel[i])
        status = classify_proximity(distance, DEMO_THRESHOLD_KM)
        print(f"t={float(row['time_s']):6.1f} s | separation={distance:8.3f} km "
              f"| relative_speed={rel_speed:8.5f} km/s | {status}")


if __name__ == "__main__":
    main()
