import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from sklearn.linear_model import LinearRegression


def load_data():
    df = pd.read_csv("/home/ibab/PycharmProjects/ML-Lab/simulated_data_multiple_linear_regression_for_ML.csv")
    x = df.drop(columns=["disease_score", "disease_score_fluct"]).to_numpy()
    y1 = df["disease_score"].to_numpy().reshape(-1, 1)
    y2 = df["disease_score_fluct"].to_numpy().reshape(-1, 1)

    x = (x - np.mean(x, axis=0)) / np.std(x, axis=0)
    x_mod = np.c_[np.ones(x.shape[0]), x]

    return x_mod, y1, y2


def initialize_parameters(n_features):
    np.random.seed(42)
    theta = np.random.uniform(low=-0.1, high=0.1, size=n_features)
    return theta.reshape(-1, 1)


def hypothesis(x_mod, theta):
    return x_mod.dot(theta)


def cost(h_t, y):
    m = len(y)
    loss = h_t - y
    cost_f = (1 / (2 * m)) * np.sum(loss ** 2)
    return cost_f


def gradient(x_mod, y, theta):
    m = len(y)
    grad_f = (1 / m) * x_mod.T.dot(x_mod.dot(theta) - y)
    return grad_f


def update_parameters(theta, grad_f, alpha):
    new_theta = theta - alpha * grad_f
    return new_theta


def normal_equation(x_mod, y2):
    return np.linalg.inv(x_mod.T.dot(x_mod)).dot(x_mod.T.dot(y2))


def main():
    x_mod, y1, y2 = load_data()
    x_train, x_test, y_train, y_test = train_test_split(x_mod, y2, test_size=0.3, random_state=42)

    # Save data to CSV files
    pd.DataFrame(x_train).to_csv('x_train.csv', index=False, header=False)
    pd.DataFrame(x_test).to_csv('x_test.csv', index=False, header=False)
    pd.DataFrame(y_train).to_csv('y_train.csv', index=False, header=False)
    pd.DataFrame(y_test).to_csv('y_test.csv', index=False, header=False)

    n_features = x_train.shape[1]
    theta = initialize_parameters(n_features)

    alpha = 0.01
    num_iterations = 1000
    costs = []

    # Normal Equation
    nor_eq_theta = normal_equation(x_mod, y2)
    print(f"Normal Equation Coefficients:\n{nor_eq_theta}")

    # Scikit-learn Linear Regression
    model = LinearRegression()
    model.fit(x_train, y_train)
    y_pred_sklearn = model.predict(x_test)
    r2_sklearn = r2_score(y_test, y_pred_sklearn)
    print(f"R2 Score (Scikit-learn): {r2_sklearn}")

    # Gradient Descent
    for i in range(num_iterations):
        h_t = hypothesis(x_train, theta)
        cost_f = cost(h_t, y_train)
        costs.append(cost_f)
        grad_f = gradient(x_train, y_train, theta)
        theta = update_parameters(theta, grad_f, alpha)
        if i % 100 == 0:
            print(f"Iter {i}, Cost: {cost_f}")

    # Final Test Cost for Gradient Descent
    final_cost = cost(hypothesis(x_test, theta), y_test)
    print(f"Final Test Cost (Gradient Descent): {final_cost}")

    # Predictions from all methods
    y_pred_gd = hypothesis(x_test, theta)
    y_pred_ne = hypothesis(x_test, nor_eq_theta)

    # Plotting the predictions from all methods
    plt.figure(figsize=(15, 5))

    # Gradient Descent vs True values
    plt.subplot(1, 3, 1)
    plt.scatter(y_test, y_pred_gd, color='blue', label='Gradient Descent')
    plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'k--', lw=2)
    plt.title("Gradient Descent: Predicted vs True")
    plt.xlabel("True Disease Fluctuation")
    plt.ylabel("Predicted Disease Fluctuation")
    plt.legend()

    # Scikit-learn vs True values
    plt.subplot(1, 3, 2)
    plt.scatter(y_test, y_pred_sklearn, color='green', label='Scikit-learn')
    plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'k--', lw=2)
    plt.title("Scikit-learn: Predicted vs True")
    plt.xlabel("True Disease Fluctuation")
    plt.ylabel("Predicted Disease Fluctuation")
    plt.legend()

    # Normal Equation vs True values
    plt.subplot(1, 3, 3)
    plt.scatter(y_test, y_pred_ne, color='red', label='Normal Equation')
    plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'k--', lw=2)
    plt.title("Normal Equation: Predicted vs True")
    plt.xlabel("True Disease Fluctuation")
    plt.ylabel("Predicted Disease Fluctuation")
    plt.legend()

    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    main()
