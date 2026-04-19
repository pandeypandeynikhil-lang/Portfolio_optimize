import numpy as np
import cvxpy as cp

def optimize_portfolio(returns):
    mu = returns.mean().values
    Sigma = returns.cov().values

    n = len(mu)

    w = cp.Variable(n)

    portfolio_return = mu @ w
    portfolio_risk = cp.quad_form(w, Sigma)

    objective = cp.Maximize(portfolio_return - 0.5 * portfolio_risk)

    constraints = [
        cp.sum(w) == 1,
        w >= 0
    ]

    problem = cp.Problem(objective, constraints)
    problem.solve()

    weights = w.value
    ret = mu @ weights
    risk = np.sqrt(weights.T @ Sigma @ weights)

    return weights, ret, risk