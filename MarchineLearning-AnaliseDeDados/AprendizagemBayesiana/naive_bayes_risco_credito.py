#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 16 15:20:51 2019

@author: KUMAKO
"""

import pandas as pd 

base = pd.read_csv("risco-credito.csv")
previsores = base.iloc[:,0:4].values
classe = base.iloc[:,4].values

from sklearn.preprocessing import LabelEncoder
labelencoder =LabelEncoder()
previsores[:,0] = labelencoder.fit_transform(previsores[:,0])
previsores[:,1] = labelencoder.fit_transform(previsores[:,1])
previsores[:,2] = labelencoder.fit_transform(previsores[:,2])
previsores[:,3] = labelencoder.fit_transform(previsores[:,3])

from sklearn.naive_bayes import GaussianNB
classificador = GaussianNB()
#chamar fit para treinar o algoritmo
classificador.fit(previsores,classe)

#historico boa , divida alta, garantias nenhuma, renda >35
#resultado =classificador.predict([[0,0,1,2]])
#historia ruim , divida alta , garantias adequada , renda <15
#chamar predict para prever
resultado =classificador.predict([[0,0,1,2],[3,0,0,0]])
#alguns prints
print(classificador.classes_)
print(classificador.class_count_)
print(classificador.class_prior_)



