import numpy as np
import matplotlib.pyplot as plt

def plot_efficient_frontier(returns):
    mu = returns.mean().values
    Sigma = returns.cov().values

    results = []

    for _ in range(5000):
        w = np.random.random(len(mu))
        w /= np.sum(w)

        ret = mu @ w
        risk = np.sqrt(w.T @ Sigma @ w)

        results.append((risk, ret))

    results = np.array(results)

    plt.scatter(results[:,0], results[:,1], s=2)
    plt.xlabel("Risk")
    plt.ylabel("Return")
    plt.title("Efficient Frontier")
    plt.show()