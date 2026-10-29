# Methodology

## Scope

This repository contains a small educational software demonstration. Its included CSV values are synthetic Cartesian positions for showing the data flow only. They are not validated satellite ephemerides and should not be interpreted as a physically consistent orbit.

## Calculation

For positions **r_sat** and **r_debris**, separation is calculated as:

`d = sqrt((x_sat-x_debris)^2 + (y_sat-y_debris)^2 + (z_sat-z_debris)^2)`

A finite-difference estimate of velocity is calculated from consecutive position samples and timestamps. Relative speed is the magnitude of the difference between the two velocity vectors.

The warning is a configurable distance threshold for demonstration. It is not collision probability. A real analysis would require suitable orbital data, consistent coordinate frames and epochs, uncertainty information, and validated propagation and screening methods.

## Validation plan

1. Verify distance calculations using hand-calculated vectors.
2. Verify relative velocity using simple vectors.
3. Test both sides of the configured threshold.
4. Compare results with a trusted independent implementation before using real data.
5. Record dataset source, units, coordinate frame, epoch, assumptions, and known limitations.
