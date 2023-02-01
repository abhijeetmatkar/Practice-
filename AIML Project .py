#!/usr/bin/env python
# coding: utf-8

# In[ ]:


ML Introduction: Linear Regression Algorithm
# Simple Linear regresssion 1 Input + 1 Output


# In[1]:


# Lets have a data first
# In ML, input must be in 2D format
X = [[1],[2],[3],[4],[5]]
y = [3,4,2,4,5]


# In[2]:


# Import LinearRegression class
from sklearn.linear_model import LinearRegression


# In[3]:


# Create an object of LR
model = LinearRegression()


# In[5]:


# Model Training
# fit method is used to perform training of algorithm
model.fit(X,y)


# In[6]:


# Model Prediction
# use predict method to get pedcition using new input
model.predict([[3]])


# In[7]:


model.predict([[5]])


# In[ ]:


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

