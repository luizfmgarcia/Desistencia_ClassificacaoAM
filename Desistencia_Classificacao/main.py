#from objects import *
import genData
import ioData
import numpy as np
from sklearn import svm
from sklearn.model_selection import cross_val_score
import matplotlib.pyplot as plt        

#==============================================================================================================            

class main:

    QTDE_DESISTE = 3000        
    QTDE_CONTINUA = 3000
    
    print("Podemos prever, baseando em alguns dados de um certo aluno universitario, se ele ira, muito provavelmete, continuar (1) ou desistir (0) do curso em algum momento proximo?")
    escolha = input('Para tal, voce gostaria de ciar uma nova base de dados (s/n)? Se já há uma base, ela será apagada caso sim: ')
    
    if(escolha=='s'):
        # Estas duas linhas criam e salvam a base de dados caso ainda nao exista uma
        # Isto apaga o que ja existe na pasta do projeto
        X, y = genData.genData(QTDE_DESISTE, QTDE_CONTINUA)
        ioData.outDataBase(X, y)
        print("Base criada e guardada!")
    else:
        # Aqui voce recupera a base dados existente em CSV na pasta do projeto
        X, y = ioData.getData()
    
    # Algoritmos de classificacao    
    C = 100.0  # SVM regularization parameter
    clf = svm.SVC(kernel='linear', C=C, probability=True)
    clf.fit(X, y)
        
    # Apresentando e Salvando o resultado
    scores = cross_val_score(clf, X, y, cv =10)    
    
    print("Classificador: ", clf)
    print("Media e Desvio Padrão do modelo gerado: ", scores.mean(), scores.std())    
    print("Numero de vetores de suporte para cada classe: ", clf.n_support_)
    print("Indices dos vetores de suporte: ", clf.support_)
    print("Constantes na função de decisão: ", clf.dual_coef_)
    print(clf.coef_, clf.intercept_)
    print(clf.decision_function(X))
    
    ioData.outResult(scores.mean(), scores.std(), clf)
    
    # Testando o modelo gerado para novas entradas
    escolha = input('Voce quer testar um novo aluno?(s/n): ')
    while(escolha=='s'):
        dados = input('Valores (separados por virgulas): ')
        novo_X = dados.split(';')
        i = 0
        for i in range(len(novo_X)):
            novo_X[i] = float(novo_X[i])
        print("Classificação, Prob. por classe e Valor resultante do modelo: ", clf.predict([novo_X]), clf1.predict_proba([novo_X]), clf1.decision_function([novo_X]))
        escolha = input('Voce quer testar um novo aluno?(s/n): ')    
        
#==============================================================================================================
        