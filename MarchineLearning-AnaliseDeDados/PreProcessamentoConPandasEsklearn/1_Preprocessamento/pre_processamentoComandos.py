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
