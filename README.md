#  Portfolio Optimization using Modern Portfolio Theory (MPT)

## Overview
This project implements **Modern Portfolio Theory (MPT)** to construct an optimal portfolio of assets that maximizes returns while minimizing risk.

The system uses historical stock data and applies **convex optimization (CVXPY)** to determine the best allocation of capital across assets.

---

##  What Problem Does This Solve?
Investors face a trade-off between **risk and return**. Instead of selecting individual stocks, this project:
- Builds a diversified portfolio
- Quantifies risk mathematically
- Optimizes allocation for the best risk-adjusted return

---

##  Key Financial Concepts

### 1️. Expected Return
The expected return of a portfolio is the weighted average of individual asset returns:

R_p = w^T μ

Where:
- w = weights of assets  
- μ = expected returns vector  

---

### 2️.Portfolio Risk (Volatility)
Risk is measured using variance (or standard deviation):

σ_p = sqrt(w^T Σ w)

Where:
- Σ = covariance matrix  
- Captures how assets move together  

---

### 3️.Covariance Matrix
- Measures relationship between asset returns  
- Helps reduce risk through diversification  

---

### 4️. Sharpe Ratio
Measures **risk-adjusted return**:

Sharpe Ratio = (R_p - R_f) / σ_p

Where:
- R_f = risk-free rate  
- Higher Sharpe Ratio ⇒ better portfolio  

---

### 5️.Efficient Frontier
- Set of optimal portfolios  
- Each point gives maximum return for a given risk level  

---

##  Optimization Formulation

We solve the following optimization problem:

Maximize:
R_p - λ * σ_p^2

Subject to:
- sum(w_i) = 1  (full investment)
- w_i ≥ 0       (no short selling)

---

##  Tech Stack
- Python  
- NumPy  
- Pandas  
- Matplotlib  
- CVXPY  
- Yahoo Finance API  

---
## Project Structure

```
portfolio-optimization
├── data
├── src
│   ├── data_loader.py
│   ├── optimizer.py
│   └── utils.py
├── main.py
├── requirements.txt
└── README.md
```

##  How to Run

### 1. Clone the repository

### 2. Create virtual environment

### 3. Install dependencies

### 4. Run the project

---

##  Output
- Optimal asset weights  
- Expected portfolio return  
- Portfolio risk (volatility)  
- Efficient frontier visualization  

---

##  Key Highlights
✔ Implements real-world financial theory  
✔ Uses convex optimization (CVXPY)  
✔ Works on real market data  
✔ Visualizes efficient frontier  

---

##  Future Improvements
- Include dynamic risk-free rate  
- Add sector/industry constraints  
- Deploy as a Streamlit dashboard  
- Include transaction costs  

---

##  Author
Nikhil Pandey  
IIT Patna  

---