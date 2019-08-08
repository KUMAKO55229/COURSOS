# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd 
base = pd.read_csv('census.csv')
previsores = base.iloc[:,0:14].values
classe = base.iloc[:,14].values

from sklearn.preprocessing import LabelEncoder , OneHotEncoder
labelencoder_previsores = LabelEncoder()
#Labels = labelencoder_previsores.fit_transform(previsores[:,1])

#Transformando variaveis categoricas
previsores[:,1] = labelencoder_previsores.fit_transform(previsores[:,1])
previsores[:,3] = labelencoder_previsores.fit_transform(previsores[:,3])
previsores[:,5] = labelencoder_previsores.fit_transform(previsores[:,5])
previsores[:,6] = labelencoder_previsores.fit_transform(previsores[:,6])
previsores[:,7] = labelencoder_previsores.fit_transform(previsores[:,7])
previsores[:,8] = labelencoder_previsores.fit_transform(previsores[:,8])
previsores[:,9] = labelencoder_previsores.fit_transform(previsores[:,9])
previsores[:,13] = labelencoder_previsores.fit_transform(previsores[:,13])

#transformaando em variaveis dummy com OneHotEncoder
onehotencoder = OneHotEncoder(categorical_features=[1,3,5,6,7,8,9,13])
previsores = onehotencoder.fit_transform(previsores).toarray()
labelencoder_classe = LabelEncoder()
classe = labelencoder_classe.fit_transform(classe)

#Escalonando
from sklearn.preprocessing import StandardScaler 
scaler = StandardScaler()
previsores = scaler.fit_transform(previsores)


#from sklearn.cross_validation import train_test_split 
from sklearn.model_selection import train_test_split 
prvisores_treinamento, previsores_teste, classe_treinamento, classe_teste = train_test_split(previsores,classe,test_size=0.25, random_state=0)

