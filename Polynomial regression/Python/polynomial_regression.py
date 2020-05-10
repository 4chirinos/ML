# -*- coding: utf-8 -*-
"""polynomial_regression

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Gukf4sIWOLAY2hi_7E3qrebnstTfo8WH
"""

# Polynomial regression

import numpy
import pandas
from matplotlib import pyplot
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

# Import dataset
dataset = pandas.read_csv('Position_Salaries.csv')

# Linear regression
# Taking independent variables or features
X = dataset.iloc[:, 1:-1].values
# Taking dependent variables
y = dataset.iloc[:, -1].values
# Creating linear regressor
linear_regressor = LinearRegression()
linear_regressor.fit(X, y)

# Polynomial regression with degree = 2
# Creating polynomial variables or features
polynomial_features = PolynomialFeatures(degree=2)
X_polynomial = polynomial_features.fit_transform(X)
# Polynomial regression
polynomial_regressor = LinearRegression()
polynomial_regressor.fit(X_polynomial, y)

# Visualising linear model estimation
pyplot.scatter(X, y, color='red')
pyplot.plot(X, linear_regressor.predict(X), color='blue')
pyplot.title('Salary vs Position level (Linear regression)')
pyplot.xlabel('Position level')
pyplot.ylabel('Salary')
pyplot.show()

# Visualising polynomial model estimation
pyplot.scatter(X, y, color='red')
pyplot.plot(X, polynomial_regressor.predict(X_polynomial), color='blue')
pyplot.title('Salary vs Position level (Polynomial degree = 2)')
pyplot.xlabel('Position level')
pyplot.ylabel('Salary')
pyplot.show()

# Polynomial regression with degree = 3
# Creating polynomial variables or features
polynomial_features = PolynomialFeatures(degree=3)
X_polynomial = polynomial_features.fit_transform(X)
# Polynomial regression
polynomial_regressor = LinearRegression()
polynomial_regressor.fit(X_polynomial, y)

# Visualising polynomial model estimation
pyplot.scatter(X, y, color='red')
pyplot.plot(X, polynomial_regressor.predict(X_polynomial), color='blue')
pyplot.title('Salary vs Position level (Polynomial degree = 3)')
pyplot.xlabel('Position level')
pyplot.ylabel('Salary')
pyplot.show()

# Polynomial regression with degree = 4
# Creating polynomial variables or features
polynomial_features = PolynomialFeatures(degree=4)
X_polynomial = polynomial_features.fit_transform(X)
# Polynomial regression
polynomial_regressor = LinearRegression()
polynomial_regressor.fit(X_polynomial, y)

# Visualising polynomial model estimation
pyplot.scatter(X, y, color='red')
pyplot.plot(X, polynomial_regressor.predict(X_polynomial), color='blue')
pyplot.title('Salary vs Position level (Polynomial degree = 4)')
pyplot.xlabel('Position level')
pyplot.ylabel('Salary')
pyplot.show()

# Polynomial regression with degree = 5
# Creating polynomial variables or features
polynomial_features = PolynomialFeatures(degree=5)
X_polynomial = polynomial_features.fit_transform(X)
# Polynomial regression
polynomial_regressor = LinearRegression()
polynomial_regressor.fit(X_polynomial, y)

# Visualising polynomial model estimation
pyplot.scatter(X, y, color='red')
pyplot.plot(X, polynomial_regressor.predict(X_polynomial), color='blue')
pyplot.title('Salary vs Position level (Polynomial degree = 5)')
pyplot.xlabel('Position level')
pyplot.ylabel('Salary')
pyplot.show()