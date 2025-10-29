# 📊 Network Statistical Analysis  
### *Statistical modeling of Internet network performance using MLE and Bayesian Inference*

## 🧠 Overview

This project aims to analyze and model **network performance metrics**, such as download/upload throughput, round-trip time (RTT), and packet loss, obtained from the **Measurement Lab (M-Lab)** public dataset.

The study applies two complementary statistical frameworks:

- **Maximum Likelihood Estimation (MLE)** — for parameter estimation under classical frequentist assumptions.
- **Bayesian Inference** — to incorporate prior knowledge and derive posterior and predictive distributions.

These approaches enable a robust comparison of models representing real-world Internet behavior, considering client and server heterogeneity.

# 🚀 Essential Project Information

This document contains the configuration guide and important notes for running and developing this Python project, which uses the `src/toolkit` package structure and the Poetry dependency manager.

## ⚙️ I. Quick Installation and Setup

The project uses [Poetry](https://python-poetry.org/) for virtual environment (venv) and dependency management.

### 1. Prerequisites

* **Python 3.10**
* **Poetry** (Dependency Manager)

### 2. Configuration

1.  **Clone the Project:**
    ```bash
    git clone https://github.com/barros-jv/statistical-inference-project.git
    cd your_project
    ```

2.  **Install Dependencies:**
    Poetry will **automatically create and activate the venv** and install all packages specified in `pyproject.toml`.
    ```bash
    poetry install
    ```

3.  **Run Commands:**
    Use `poetry run` to ensure that commands are executed within the project's virtual environment:
    ```bash
    # Example: Run the main script
    poetry run python src/main.py
    ```

4.  **Deactivate:**
    To exit the virtual environment and return to the regular terminal:
    ```bash
    deactivate
    ```

## 🧱 Project Structure

```bash
statistical-inference-project/
├── pyproject.toml             # Poetry project configuration
├── README.md                  # Project documentation
├── data/
│ ├── ndt_tests_corrigido.csv  # Exploratory Data Analysis
│ └── ndt_tests_tratado.csv    # Preprocessed M-Lab dataset
├── docs/                      # Project Description
├── reports/                   # Latex Report
├── notebooks/
│ ├── eda_analysis.ipynb       # Quality Data Analysis
│ ├── eda_analysis.ipynb       # Exploratory Data Analysis
│ ├── mle_modeling.ipynb       # MLE fitting and diagnostics
│ └── bayesian_inference.ipynb # Bayesian modeling and posterior analysis
├── figures/                   # Generated plots and figures
│ └── ...
└── src/                       # Packages
  └── toolkit/
    ├── __init__.py
    └── utils.py