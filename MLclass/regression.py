import math
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import Pipeline
import numpy as np

x = np.linspace(-2*math.pi, 4*math.pi, 40)
x = x.reshape(-1, 1)
y = np.sin(x)
plt.scatter(x, y)   # 오리지널 데이터 플롯

lr = LinearRegression()
# polynomial feature를 사용하여 x의 차원을 올린다.
poly_feat = PolynomialFeatures(degree=3)

pipeline = Pipeline([("polynomial_features", poly_feat),
                         ("linear_regression", lr)])
pipeline.fit(x, y)


x_test = np.linspace(-2*math.pi, 4*math.pi, 40)
x_test = x_test.reshape(-1, 1)
plt.plot(x_test, pipeline.predict(x_test))
#plt.plot(x_test, pipeline.predict(x_test[:, np.newaxis]))
plt.show()
