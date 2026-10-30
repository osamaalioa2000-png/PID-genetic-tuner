# PID Genetic Tuner

A lightweight Python project that uses a genetic algorithm to tune the gains of a PID controller for a simulated system. The project evolves candidate PID parameters (`Kp`, `Ki`, and `Kd`) and evaluates them using a fitness function based on overshoot, settling time, and tracking error.

## Overview

This repository demonstrates how a simple evolutionary optimizer can be used to find PID gains that improve control performance in a basic simulated dynamic system. It includes:

- A generic genetic algorithm framework
- A PID fitness simulation
- A demo script that plots the system response before and after evolution
- Generated comparison images in the `results/` folder

## Features

- Genetic algorithm optimization for PID tuning
- Tournament selection and mutation-based evolution
- Customizable chromosome structure with 3 genes per individual
- Simulated control response for a target value of 10
- Visualization of population performance across generations

## Repository Structure

```text
PID-genetic-tuner/
├── main.py                  # Demo script for running the PID tuner
├── requirements.txt         # Python dependencies
├── setup.py                # Basic package setup definition
├── src/
│   ├── __init__.py
│   ├── fitness_sim.py      # PID fitness simulation logic
│   └── ga_framework.py     # Genetic algorithm implementation
├── results/
│   ├── before_after_evolution.png
│   ├── first_generation.png
│   └── last_generation.png
├── .gitignore
└── README.md
```

## Installation

Clone the repository and install the required dependencies:

```bash
git clone https://github.com/osamaalioa2000-png/PID-genetic-tuner.git
cd PID-genetic-tuner
python -m venv .venv
source .venv/bin/activate   # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

You can also install the package in editable mode:

```bash
pip install -e .
```

## Usage

Run the main demo script:

```bash
python main.py
```

This will:

1. Initialize a population of PID candidates
2. Simulate the system response for each configuration
3. Run the genetic algorithm for several generations
4. Display a plot comparing the first-generation and evolved responses

The generated plots are saved in the `results/` directory.

## How It Works

Each chromosome represents a PID configuration:

```python
[Kp, Ki, Kd]
```

The fitness function simulates a simple mass-spring-like system and computes a score based on:

- overshoot
- settling time
- final tracking error

The algorithm evolves the population by selecting strong candidates and mutating/crossing over their genes to improve the fitness score over generations.

## Dependencies

- `numpy`
- `matplotlib`

## Example Output

The project includes example output plots in the `results/` directory:

- `results/first_generation.png`
- `results/last_generation.png`
- `results/before_after_evolution.png`

These visualizations help compare early candidate responses with the tuned controller behavior after evolution.

## License

This repository does not currently include a license file. If you plan to share or distribute it publicly, consider adding an appropriate open-source license.

## Author

Created for experimentation with genetic algorithms and PID controller tuning.
