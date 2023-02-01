ML Introduction: Linear Regression Algorithm
 In ML, input must be in 2D format
X = [[1],[2],[3],[4],[5]]
y = [3,4,2,4,5]
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X,y)
model.predict([[3]])
model.predict([[5]])
"""
ML project -  ML Project Flow
1. Loading dataset
2. Identify X(independant variable/s),y(Output)
3. Data analysis[EDA:Exploratory Data Analysis]
4. Feature selection process: select important feature amongs all
5. Feature Engineering: creating a new features/columns from available one
6. Splitting Data into Training segment and Testing segment(OPTIONAL)
7. Model Training
8. Model Testing
9. Performance checking using metrics
10. Evaluate your performance and try to improve if needed 
using Hyperparamter tuning
"""

