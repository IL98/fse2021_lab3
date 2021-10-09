from useful_package import hyperbola, polynom_3

import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error


SEED=42

X = np.random.uniform(1.1, 100, (100, 1))

y_a = hyperbola(X)
y_b = polynom_3(X)
y = np.hstack((y_a, y_b))


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=30, random_state=SEED)


regr = RandomForestRegressor(random_state=SEED)
regr.fit(X_train, y_train)


y_pred = reg.predict(X_test)

mse = mean_squared_error(y_pred, y_test, multioutput='raw_values')
mse_dict = {"hyperbola": mse[0], "polynom_3": mse[1]}

