ML Introduction: Linear Regression Algorithm
 In ML, input must be in 2D format
X = [[1],[2],[3],[4],[5]]
y = [3,4,2,4,5]
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X,y)
model.predict([[3]])
model.predict([[5]])
