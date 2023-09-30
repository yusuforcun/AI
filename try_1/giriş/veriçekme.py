import pandas as pd


veriler = pd.read_csv('veriler.csv')
print(veriler)

boy_kilo = veriler[['boy','kilo']]
print(boy_kilo)