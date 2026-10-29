import unittest
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from proximity_analysis import separation_km, relative_speed_km_s
from collision_risk import classify_proximity


class ProximityTests(unittest.TestCase):
    def test_separation(self):
        self.assertAlmostEqual(separation_km((0, 0, 0), (3, 4, 0)), 5.0)

    def test_relative_speed(self):
        self.assertAlmostEqual(relative_speed_km_s((1, 0, 0), (4, 0, 0)), 3.0)

    def test_threshold_alert(self):
        self.assertEqual(classify_proximity(0.5, 1.0), "DEMO ALERT")
        self.assertEqual(classify_proximity(2.0, 1.0), "NOMINAL")


if __name__ == "__main__":
    unittest.main()
