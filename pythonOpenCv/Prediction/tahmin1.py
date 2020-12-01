import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

veriler = pd.read_csv("satislar.csv")

print(veriler)

aylar = veriler[["Aylar"]]
print(aylar)

satislar = veriler[["Satislar"]]
print(satislar)

satislar2 = veriler.iloc[:,0:1].values
print(satislar2)

#Verilerin ölçeklenmesi

x_train, x_test, y_train, y_test = train_test_split(aylar, satislar, test_size=0.33, random_state=5)

sc = StandardScaler()

X_train = sc.fit_transform(x_train)
X_test = sc.fit_transform(x_test)

Y_train = sc.fit_transform(y_train)
Y_test = sc.fit_transform(y_test)

#model inşası (Lineer regression)

lr = LinearRegression()
lr.fit(x_train, x_train)

tahmin = lr.predict(x_test)

cizim = plt.plot(x_train, y_train)