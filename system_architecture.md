# System Architecture

```text
Tracking data (CSV / verified source)
                 |
                 v
         Input and validation
                 |
                 v
        Relative proximity math
                 |
                 v
        Demo threshold classifier
                 |
                 v
        Console report / dashboard
                 |
                 v
     Optional illustrative maneuver view
```

The current starter repository includes a CSV reader, Cartesian separation calculation, finite-difference velocity estimate, a threshold-based demo label, unit tests, and a static browser dashboard. It does not include direct sensor-based detection of debris, a live operational data feed, or real satellite control.
