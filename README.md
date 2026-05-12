
# Coronary Artery Disease Prediction Model

**Author:** Amir A. Seid | **Published:** April 2026

A machine learning framework for predicting Coronary Artery Disease (CAD) severity using the UCI Heart Disease Dataset, built in R.

---

## 📁 Project Structure

``` 

|-- scripts/ # Data cleaning and preprocessing (Python 3.14)
    |-- R
  	   |-- plumber.R # The API 
  	   |-- run.R # to host plumber.R
  	   |-- source.R # full analysis
	   
	    |--Python # preprocessing works I have done on my machine.

|-- model/ # PPO model and MICE imputation (R 4.5.2)

|-- data/ # Merged UCI Heart Disease datasets
    |-- raw # just as they are before my pandas' cleaning
    |-- processed
|-- report/
	   |-- Brief report
   	|-- Heart_failure.pdf
	   |-- Heart_failure.qmd
```
---

## Dataset

- **Source:** UCI Heart Disease Repository (Cleveland, Hungary, Switzerland, VA Long Beach)

- **Observations:** 920 patient records merged across all four databases

- **Target Variable:** `num` — CAD severity (0 = healthy, 1–4 = disease stages)

---

## Methodology

- **Data Cleaning:** Missing values encoded as `-9` and `?` handled; `0` treated as missing in cholesterol

- **Imputation:** MICE with specialized logistic regressions (logistic, POLR, POLYREG)

- **Model:** Partial Proportional Odds (PPO) — chosen after `age`, `sex`, and `exang` failed the Brant Parallel Lines Assumption test

- **Pooling:** Rubin's Rules applied across imputed datasets

---

## Results
| Metric | Score | Clinical Note |
| :--- | :--- | :--- |
| Binary Accuracy | 84.2% | High proficiency |
| Sensitivity | 83% | Diagnostic screening focus |
| Systemic Bias | 0.17 | 51.5% reduction via weighting |

> A Bayesian-inspired weighting strategy was applied to reduce systemic bias by 51.5% and prioritize sensitivity — because it is better to flag a healthy patient as sick than to miss a true diagnosis.

---

## API

A **Plumber API** is included for anyone who wants to build a web application on top of the model. It accepts patient feature inputs and returns a CAD severity prediction.

``` r 

`# Run the API locally`

`library(plumber)`

`pr("api/plumber.R") |> pr_run(port = 8000)`

``` 

---

## Requirements

- R 4.5.2 — modeling and analysis

 - R packages: `mice`, `VGAM`, `plumber` 

---

## Report

Full methodology and results available in [`Heart_failure.pdf`](Heart_failure.pdf)
