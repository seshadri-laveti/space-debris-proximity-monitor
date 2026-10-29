<div align="center">

# 🛰️ Space Debris Proximity Detection, Monitoring & Orbit-Change Simulation

### An Intelligent Space Situational Awareness and Collision-Risk Analysis Platform

**Laveti Seshadri**  
Electronics and Communication Engineering (ECE)  
Vignan's Institute of Information Technology (VIIT)  
Visakhapatnam, Andhra Pradesh, India

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)
![Platform](https://img.shields.io/badge/Platform-Cross--Platform-green)
![Project](https://img.shields.io/badge/Project-Educational%20Prototype-purple)
![Data](https://img.shields.io/badge/Data-Synthetic%20Demo-orange)
![License](https://img.shields.io/badge/License-MIT-green)

</div>

---

# 📌 1. Project Overview

Space debris is a growing challenge for satellite operators and space missions. Defunct satellites, discarded rocket stages, and fragments produced by collisions can threaten operational spacecraft.

The **Space Debris Proximity Detection, Monitoring and Orbit Change System** is an educational software project designed to demonstrate a workflow for processing satellite and debris tracking information, estimating relative proximity, identifying threshold-based alerts, and visualizing the results through a ground station dashboard.

The project explores how data processing, numerical calculations, visualization, and collision-avoidance simulation concepts can be combined in a modular software architecture.

The current prototype uses synthetic sample data to demonstrate proximity calculations and monitoring functionality. Integration with verified orbital tracking data, validated orbital propagation, uncertainty-aware collision assessment, and physically consistent avoidance maneuvers are potential future enhancements.

> **Important:** This project is an educational prototype. It does not directly detect physical debris in space, provide operational collision predictions, or control a real satellite.

---

# 🎯 2. Problem Statement

Satellites operating in Earth orbit may encounter other tracked objects. Identifying close approaches requires processing orbital information, evaluating relative motion, and determining which encounters require further investigation.

This project demonstrates a simplified software workflow that converts sample position data into proximity measurements and visual alerts.

The central engineering question is:

**How can satellite and debris tracking records be processed into understandable proximity indicators and warning information while maintaining a clear distinction between simple distance screening and scientifically validated collision-risk assessment?**

---

# 🚀 3. Project Objectives

The primary objectives are:

- Process satellite and space debris tracking records.
- Calculate relative distance between two tracked objects.
- Estimate relative velocity from time-stamped position samples.
- Identify sample encounters that cross a configurable distance threshold.
- Visualize proximity information using charts and a monitoring dashboard.
- Demonstrate the software architecture of a space situational awareness system.
- Provide a foundation for future orbital data integration and simulation.
- Support repeatable testing and research-oriented development.

## Advanced objectives

Future development may investigate:

- Integration with documented orbital tracking datasets.
- Time-of-closest-approach estimation.
- Orbital trajectory propagation.
- Collision-probability estimation using appropriate uncertainty information.
- Comparison of nominal and simulated avoidance trajectories.
- Evaluation of screening accuracy and false-alarm rates.
- Interactive three-dimensional orbital visualization.

---

# 🏗️ 4. System Architecture

The proposed system consists of several interconnected modules.

```text
              SPACE OBJECT TRACKING DATA
                         |
                         v
                DATA INPUT MODULE
                         |
                         v
              DATA PROCESSING MODULE
                         |
                         v
               PROXIMITY ANALYSIS
                         |
                         v
              RELATIVE MOTION ANALYSIS
                         |
                         v
              COLLISION-RISK SCREENING
                         |
                  +------+------+
                  |             |
                  v             v
             NOMINAL STATUS  DEMO ALERT
                  |             |
                  +------+------+
                         |
                         v
                GROUND STATION UI
                         |
                         v
               DATA VISUALIZATION
                         |
                         v
             SIMULATION AND EVALUATION
```

The architecture separates data input, numerical analysis, warning logic, and visualization.

Advanced orbital propagation, uncertainty-aware collision probability, and maneuver optimization are future extensions rather than completed capabilities of the current starter implementation.

---

# ⚙️ 5. Working Methodology

## Step 1: Tracking Data Input

The system reads sample satellite and debris position records from a structured CSV file.

The sample dataset includes:

- Time
- Satellite X, Y, and Z coordinates
- Debris X, Y, and Z coordinates

The included values are synthetic and are intended only for demonstrating the software workflow.

## Step 2: Data Processing

The numerical fields are converted into values that can be used by the analysis functions.

A more advanced implementation should validate timestamps, missing values, coordinate systems, units, object identifiers, and data quality.

## Step 3: Proximity Analysis

The system calculates the three-dimensional Euclidean separation between the satellite and debris positions.

The resulting distance is used to demonstrate how a monitoring application can identify close approaches in sample data.

## Step 4: Relative Velocity Estimation

Velocity is estimated from changes in position over time.

The difference between the estimated satellite velocity and debris velocity is used to calculate relative speed.

These estimates demonstrate basic numerical processing and do not replace validated orbital propagation.

## Step 5: Collision-Risk Screening

A configurable distance threshold determines whether the sample separation is labelled `DEMO ALERT` or `NOMINAL`.

This threshold-based rule is intended for demonstration purposes.

It does not calculate the probability of collision.

## Step 6: Dashboard Visualization

The dashboard displays sample measurements, the minimum separation, the configured threshold, and a chart showing separation over time.

## Step 7: Orbit-Change Simulation

A future extension may compare nominal and modified trajectories using an appropriate orbital dynamics model.

The current illustrative position-offset function is not a physically validated orbital maneuver model.

---

# 📐 6. Mathematical Foundations

## 6.1 Relative Position

Let the satellite position be:

\[
\mathbf{r}_s = [x_s,y_s,z_s]
\]

Let the debris position be:

\[
\mathbf{r}_d = [x_d,y_d,z_d]
\]

The relative-position vector is:

\[
\Delta\mathbf{r} = \mathbf{r}_s-\mathbf{r}_d
\]

## 6.2 Euclidean Separation

The distance between the two positions is:

\[
d = \sqrt{(x_s-x_d)^2+(y_s-y_d)^2+(z_s-z_d)^2}
\]

When all coordinates are expressed in kilometres and refer to the same epoch and coordinate frame, the result is expressed in kilometres.

## 6.3 Velocity Estimation

For consecutive time-stamped positions, velocity can be approximated using finite differences.

For an interior sample:

\[
\mathbf{v}_i \approx
\frac{\mathbf{r}_{i+1}-\mathbf{r}_{i-1}}
{t_{i+1}-t_{i-1}}
\]

This approximation estimates velocity from the sampled positions. It does not predict future orbital motion.

## 6.4 Relative Speed

If the satellite and debris velocity estimates are:

\[
\mathbf{v}_s = [v_{sx},v_{sy},v_{sz}]
\]

\[
\mathbf{v}_d = [v_{dx},v_{dy},v_{dz}]
\]

then relative speed is:

\[
v_{\mathrm{rel}} =
\sqrt{
(v_{sx}-v_{dx})^2+
(v_{sy}-v_{dy})^2+
(v_{sz}-v_{dz})^2
}
\]

With position in kilometres and time in seconds, velocity is expressed in kilometres per second.

## 6.5 Threshold-Based Alert

The current demonstration uses:

\[
\text{Status} =
\begin{cases}
\text{DEMO ALERT}, & d \leq d_{\text{threshold}}\\
\text{NOMINAL}, & d > d_{\text{threshold}}
\end{cases}
\]

The example threshold is 1 km.

It can be changed in the source code for testing the program's alert behaviour.

**Scientific distinction:** A distance threshold is not a collision probability. Real conjunction assessment requires appropriate trajectory information, time-of-closest-approach analysis, uncertainty information, and validated methods.

---

# 🖥️ 7. Dashboard Features

The browser-based dashboard provides an educational monitoring interface.

### Current features

- Summary of the number of sample records.
- Minimum separation calculated from the included sample values.
- Configured demonstration threshold.
- Nominal or demonstration-alert status.
- Relative-separation chart.
- Table of sample timestamps and calculated separations.
- Responsive layout for different screen sizes.
- Visible notice explaining that the dataset is synthetic.

### Future dashboard enhancements

- Interactive three-dimensional trajectory visualization.
- Integration with verified orbital tracking data.
- Filtering by object identifier.
- Historical close-approach plots.
- Detailed analysis reports.
- Configurable screening parameters.
- Improved uncertainty visualization.

**Current implementation note:** The browser dashboard uses sample data embedded in its JavaScript file. It does not currently load the CSV dynamically.

---

# 🛠️ 8. Technology Stack

| Technology | Purpose |
|---|---|
| Python | Numerical calculations and data processing |
| CSV | Structured sample tracking data |
| HTML5 | Dashboard structure |
| CSS3 | Dashboard styling |
| JavaScript | Browser-side calculations and visualization |
| Python unittest | Automated unit testing |
| Git | Version control |
| GitHub | Repository hosting and collaboration |

The current Python prototype uses standard-library functionality and does not require additional third-party Python packages.

---

# 📂 9. Repository Structure

```text
space-debris-proximity-monitor/
│
├── README.md
├── LICENSE
├── .gitignore
├── requirements.txt
│
├── data/
│   └── sample_data.csv
│
├── docs/
│   ├── methodology.md
│   └── system_architecture.md
│
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── debris_tracking.py
│   ├── proximity_analysis.py
│   ├── collision_risk.py
│   └── orbit_simulation.py
│
├── dashboard/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
└── tests/
    └── test_proximity.py
```

Each module has a distinct responsibility, helping keep the project organized and easier to extend.

---

# 💻 10. Installation and Execution

## Prerequisites

Install:

- Python 3.10 or newer.
- A modern web browser.
- Git, if you want to clone the repository.

Verify your Python installation:

```bash
python --version
```

## Step 1: Clone the repository

Replace `YOUR-USERNAME` with your GitHub username.

```bash
git clone https://github.com/YOUR-USERNAME/space-debris-proximity-monitor.git
```

Move into the project folder:

```bash
cd space-debris-proximity-monitor
```

Alternatively, download the ZIP from GitHub and extract it.

## Step 2: Create a virtual environment

For Windows:

```bash
python -m venv .venv
```

Activate it in Command Prompt:

```bat
.venv\Scripts\activate.bat
```

Or activate it in PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

For macOS or Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

## Step 3: Install dependencies

```bash
pip install -r requirements.txt
```

The current Python demo does not require third-party packages.

## Step 4: Run the analysis

From the project root:

```bash
python src/main.py
```

The program prints the time, calculated separation, estimated relative speed, and demonstration status for each sample.

## Step 5: Open the dashboard

Open:

```text
dashboard/index.html
```

in your browser.

The dashboard runs locally and does not require a web server.

## Step 6: Run automated tests

```bash
python -m unittest discover -s tests -v
```

The tests check basic distance calculations, relative-speed calculations, and threshold-classification behaviour.

---

# 🧪 11. Testing and Validation

Testing is necessary to verify that the implementation behaves as expected.

### Existing test coverage

- Euclidean separation using a known three-dimensional vector.
- Relative speed using known velocity vectors.
- Alert classification below the configured threshold.
- Nominal classification above the configured threshold.

### Recommended additional tests

- Empty datasets.
- Single-row datasets.
- Missing or invalid numeric values.
- Duplicate timestamps.
- Non-monotonic timestamps.
- Zero elapsed time between samples.
- Negative and zero thresholds.
- Large and small coordinate values.
- CSV and dashboard data consistency.

Unit tests demonstrate software behaviour for the tested cases. They do not establish the physical validity of an orbital model or the accuracy of real-world collision predictions.

---

# 📊 12. Data and Assumptions

The included sample CSV contains synthetic Cartesian positions.

The current implementation assumes:

1. Satellite and debris coordinates are paired at matching timestamps.
2. Position values are interpreted as kilometres.
3. Timestamps are interpreted as seconds.
4. Both objects use the same Cartesian coordinate frame.
5. Finite differences provide illustrative velocity estimates.
6. A fixed distance threshold is used for demonstration alerts.

The sample values are not verified orbital ephemerides and are not guaranteed to describe a physically consistent orbital encounter.

### Requirements for future real-data integration

Document the following when introducing an external tracking dataset:

- Source and provider.
- Retrieval date.
- Dataset licence and usage conditions.
- Object identifiers.
- Time standard and epoch.
- Coordinate reference frame.
- Position and velocity units.
- Data quality and uncertainty information.
- Any transformations or preprocessing.

Do not treat unverified sample data as evidence of actual satellite collision risk.

---

# ⚠️ 13. Current Limitations

The current implementation has the following limitations:

- It does not use physical sensors to detect space debris.
- It does not integrate a live orbital tracking API.
- It uses synthetic sample data.
- It does not implement a validated orbital propagator.
- It does not calculate a validated collision probability.
- It uses simple finite differences for velocity estimation.
- Its threshold-based alert is a demonstration, not an operational warning.
- Its illustrative position offset is not a physically validated orbit-change maneuver.
- It does not control an actual satellite.

These limitations define the current prototype's scope and should be considered when interpreting its output.

---

# 🔬 14. Research and Development Roadmap

## Phase 1: Baseline software prototype

- [x] Create a modular Python project.
- [x] Add synthetic CSV data.
- [x] Implement three-dimensional separation.
- [x] Estimate sample velocities.
- [x] Calculate relative speed.
- [x] Implement threshold-based demonstration alerts.
- [x] Create a browser dashboard.
- [x] Add basic unit tests.

## Phase 2: Data integration and validation

- [ ] Select an appropriate orbital tracking data source.
- [ ] Validate data format, units, epochs, and coordinate frames.
- [ ] Add robust handling of missing or invalid records.
- [ ] Record dataset provenance.
- [ ] Add repeatable experiments using saved input datasets.

## Phase 3: Orbital analysis

- [ ] Integrate an appropriate orbital propagation method.
- [ ] Estimate time of closest approach.
- [ ] Compare calculations with a trusted reference implementation.
- [ ] Investigate uncertainty-aware collision-risk analysis.
- [ ] Document the limitations and assumptions of each method.

## Phase 4: Orbit-change simulation

- [ ] Define a physically consistent orbital dynamics model.
- [ ] Model candidate maneuver constraints.
- [ ] Compare nominal and modified trajectories.
- [ ] Evaluate the change in predicted closest-approach distance.
- [ ] Document the assumptions and limits of the simulation.

## Phase 5: Research evaluation

- [ ] Define measurable research questions.
- [ ] Establish baseline methods.
- [ ] Create reproducible test scenarios.
- [ ] Record actual experimental results.
- [ ] Analyze errors, false alarms, and missed events.
- [ ] Prepare plots and research documentation.

---

# 📈 15. Potential Evaluation Metrics

When suitable reference data and validated implementations are available, the project can be evaluated using metrics such as:

| Evaluation area | Possible metrics |
|---|---|
| Numerical calculations | Absolute error and relative error |
| Data quality | Missing records and invalid-record rate |
| Screening performance | Precision, recall, false-alarm rate, missed-event rate |
| Processing efficiency | Processing time per record or scenario |
| Trajectory prediction | Position error at a specified future epoch |
| Maneuver simulation | Change in predicted closest-approach distance |
| Reproducibility | Ability to reproduce results using saved inputs and settings |

Performance values should be reported only after running documented experiments and comparing results against an appropriate reference.

---

# 🔐 16. Reproducibility and Responsible Use

To make future experiments reproducible:

1. Preserve the input dataset used for each experiment.
2. Document data sources, units, epochs, and coordinate frames.
3. Record the selected threshold and other configuration values.
4. Document software versions and dependencies.
5. Keep the calculation code and dashboard presentation separate.
6. Maintain automated tests.
7. Distinguish simulated results from measured or externally verified results.
8. Report limitations alongside any claimed improvement.

> **Safety disclaimer:** This repository is intended for educational and research purposes. Its outputs must not be used to make operational satellite maneuver decisions. Real collision-avoidance decisions require appropriate tracking data, validated models, uncertainty analysis, and expert review.

---

# 🤝 17. Contribution Guidelines

Contributions are welcome in areas such as:

- Data validation.
- Numerical calculation testing.
- Dashboard development.
- Visualization improvements.
- Documentation.
- Reproducible experiments.
- Orbital analysis research.

### Contribution workflow

1. Fork the repository.
2. Create a branch for your changes.
3. Make a focused improvement.
4. Add or update tests.
5. Run the test suite.
6. Update the documentation.
7. Submit a pull request describing your changes and test results.

Please do not upload passwords, API keys, private credentials, or datasets you do not have permission to distribute.

---

# 👨‍💻 18. Author

**Laveti Seshadri**

Electronics and Communication Engineering (ECE)  
Vignan's Institute of Information Technology (VIIT)  
Visakhapatnam, Andhra Pradesh, India

### Areas of interest

- Space technology.
- Internet of Things (IoT).
- Embedded systems.
- Data processing and visualization.
- Satellite monitoring concepts.
- Collision-risk analysis and orbital simulation.

**GitHub:** Add your GitHub profile URL here.

---

# 📄 19. License

This project is distributed under the MIT License.

See the [`LICENSE`](LICENSE) file for details.

---

<div align="center">

### 🛰️ Space Debris Proximity Monitoring System

**Designed and documented by Laveti Seshadri**

*Educational prototype for space situational awareness, proximity analysis, and orbital simulation research.*

</div>
