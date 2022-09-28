from sklearn.linear_model import Ridge, Lasso
X, y = load_boston(return_X_y=True)

# L1 regularisation where alpha is a hyperparameter which determines how important either L! or L2 regularisation is
lasso_regression_model = Lasso(alpha=0.1)
lasso_regression_model.fit(X,y)

# L2 regularisation where alpha is a hyperparameter which determines how important either L! or L2 regularisation is
lasso_regression_model = Ridge(alpha=0.1)
lasso_regression_model.fit(X,y)

# simple regression model determines optimal parameters at the end, but models which train iteratively (e.g. SGD regression) provide this periodically so we can implement early stopping

 