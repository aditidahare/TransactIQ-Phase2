# TransactIQ Risk Engine

TransactIQ Risk Engine is an end-to-end credit risk prediction application built using LendingClub loan data. It predicts the probability that a borrower may default on a loan and classifies the borrower into Low, Medium, or High Risk categories through an interactive Streamlit interface.

## Project Overview

This project extends the original TransactIQ portfolio analytics idea into a machine learning based risk prediction system. The workflow includes data cleaning, exploratory data analysis, model training, model comparison, feature importance analysis, and deployment through a frontend application.

## Dataset

- Source: LendingClub accepted loans dataset
- Working sample size: 80,000 rows
- Target variable:
  - 0 = Fully Paid
  - 1 = Charged Off / Default

## Features Used

- loan_amnt
- term
- int_rate
- installment
- annual_inc
- dti
- delinq_2yrs
- revol_util
- total_acc

## Models Evaluated

- Logistic Regression
- Random Forest
- XGBoost

## Final Model

XGBoost was selected as the final model because it performed better than the other models on imbalanced tabular financial data.

## Key Results

- Random Forest AUC: 0.683
- XGBoost AUC: 0.700

XGBoost also showed much better default recall than Logistic Regression and Random Forest.

## Feature Importance Insights

The most influential features included:

- term
- int_rate
- dti
- annual_inc
- installment
- revol_util

These align well with real-world credit risk intuition.

## App Functionality

The Streamlit app allows a user to enter borrower information and returns:

- Default Probability
- Risk Category
- Recommendation

## Project Structure

```text
TransactIQ/
│
├── app/
│   ├── app.py
│   └── predict.py
│
├── data/
│   └── accepted_2007_to_2018Q4.csv
│
├── models/
│   └── credit_risk_xgb_model.pkl
│
├── notebooks/
│   └── TransactIQ_Risk_Engine.ipynb
│
├── requirements.txt
└── README.md