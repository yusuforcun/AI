import pandas as pd 
from sklearn.impute import SimpleImputer 
import numpy as np

veriler = pd.read_csv("veriler.csv")
imputer = SimpleImputer(missing_values=np.nan , strategy="mean")

yas = veriler.iloc[:,1:4].values
print(yas)

imputer = imputer.fit(yas[:,1:4])
yas[:,1:4] = imputer.transform(yas[:,1:4])
print(yas)