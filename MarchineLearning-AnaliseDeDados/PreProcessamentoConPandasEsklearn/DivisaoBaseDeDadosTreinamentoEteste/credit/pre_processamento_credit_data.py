# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#importando a biblioteca pandas
import pandas as pd

base = pd.read_csv('credit-data.csv')

#traz a media da coluna age para os lugares com idade < 0
base.loc[base.age<0,'age'] = 40.92 

#aqui fizermos separacao de atributos preditivos e atributos default
previsores = base.iloc[:,1:4].values 
classe = base.iloc[:,4].values 

#trabalhando com valores faltantes 
#trocando os vazios pelas medias
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values='NaN', strategy='mean', axis=0)
imputer = imputer.fit(previsores[:,0:3])
previsores[:,0:3] = imputer.transform(previsores[:,0:3])

#escalonamento 
from sklearn.preprocessing import StandardScaler
scaler =StandardScaler()
previsores = scaler.fit_transform(previsores)

#from sklearn.cross_validation import train_test_split 
from sklearn.model_selection import train_test_split 
prvisores_treinamento, previsores_teste, classe_treinamento, classe_teste = train_test_split(previsores,classe,test_size=0.25, random_state=0)





