import numpy as np
import cvxpy as cp

def optimize_portfolio(returns):
    mu = returns.mean().values * 252
    Sigma = returns.cov().values * 252

    n = len(mu)
    w = cp.Variable(n)

    portfolio_return = mu @ w
    portfolio_risk = cp.quad_form(w, Sigma)

    target_return = 0.2  # adjust if needed

    objective = cp.Minimize(portfolio_risk)

    constraints = [
        cp.sum(w) == 1,
        w >= 0,
        portfolio_return >= target_return
    ]

    problem = cp.Problem(objective, constraints)
    problem.solve(solver=cp.SCS)

    weights = w.value

    print("Raw weights:", weights)  # DEBUG

    ret = mu @ weights
    risk = np.sqrt(weights.T @ Sigma @ weights)

    return weights, ret, risk