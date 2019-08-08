# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#importando a biblioteca pandas
import pandas as pd
#
base = pd.read_csv('credit-data.csv')
#ver descricao dos dados 
base.describe()
#localizar  idades < 0 
base.loc[base['age']<0]
#apagar a coluna
base.drop ('age',1,inplace=True)

#apagar somente os 3 registros com problemas 
base.drop(base[base.age < 0].index, inplace=True)

#Preencher os valores manualmente 
#prenncher os valores com a media

base.mean()  #traz a media de todas as colunas

base.age.mean() #traz a media da coluna age
base['age'].mean() #traz a media da coluna age
#busca a media da coluna age
base.age[base.age>0].mean()
#traz a media da coluna age para os lugares com idade < 0
base.loc[base.age<0,'age'] = 40.92 
#verifica se há alguma idade null
pd.isnull(base['age']) 
#verifica se há alguma idade null e se houver, traz como objeto
base.loc[pd.isnull(base['age'])]

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






