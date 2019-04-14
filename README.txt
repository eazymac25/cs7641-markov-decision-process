# CS7641-Markov-Decision-Process
Georgia Tech CS 7641 - Randomized Optimization: Markov Decision Process

Author: Kyle MacNeney

GA Tech ID: kmacneney3

Author Email: kyle.macneney@gmail.com

Repository: https://github.com/eazymac25/cs7641-markov-decision-process

**NOTE: Written in markdown**

Happily taken from https://github.com/cmaron/CS-7641-assignments/tree/master/assignment4

## Description
This contains Markov Decision Process (MDP) Experiments for the following:
- Frozen Lake (8x8) Slippery
- Frozen Lake (15x15) Not slippery
- Frozen Lake (15x15) Slippery
- Frozen Lake (20x20) Slippery
- Windy Cliff (4x12)

The package allows for solving any of these environments via:
- Policy Iteration
- Value Iteration
- Q-Learning

## Pre-requisites
1. Install Python 3.5 (easiest via Anaconda)
2. Install git

## Installation Instructions
1. Clone or download the repository
    ```bash
    git clone https://github.com/eazymac25/cs7641-markov-decision-process.git
    ```
2. cd into the root of the downloaded repository
    ```bash
    cd cs7641-markov-decision-process
    ```
3. Install all requirements listed in `requirements.txt`
    ```bash
    pip install -r requirements.txt
    ```

## Directory Structure
```
|-- environments
    |-- cliff_walking.py
    |-- frozen_lake.py
|-- experiments
    |-- base.py (abstract base class for experiments)
    |-- plotting.py (plotting utils)
    |-- policy_iteration.py
    |-- q_learner.py
    |-- value_iteration.py
|-- output
    |-- images (all the board iterations for all experiments)
    |-- PI (policy iteration output)
    |-- Q (q-learning output)
    |-- report (where all plots for all experiments are stored)
    |-- VI (value iteration output)
|-- solvers
    |-- base.py (abstract base class for solvers)
    |-- policy_iteration.py
    |-- q_learning.py
    |-- value_iteration.py
|-- README.md
|-- README.txt
|-- README-original.md (original readme from the original repo)
|-- requirements.txt
|-- run_experiment.py (command line tool for running experiments)
```

## Running Experiments

First move into root of repository

### Run Individual Experiments

**Note:** `--vebose` runs full logging and `--plot` plots all figures

1. Value Iteration
    ```bash
    python run_experiment.py --value [--verbose] [--plot]
    ```
2. Policy Iteration
    ```bash
    python run_experiment.py --policy [--verbose] [--plot]
    ```
3. Q-learning
    ```bash
    python run_experiment.py --q [--verbose] [--plot]
    ```

### Run All Experiments
```bash
python run_experiment.py --all [--verbose] [--plot]
```

### Plotting
```bash
python run_experiment.py --plot
```