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
    
    #=================================================
    
    if(escolha=='s'):
        # Estas duas linhas criam e salvam a base de dados caso ainda nao exista uma
        # Isto apaga o que ja existe na pasta do projeto
        X, y = genData.genData(QTDE_DESISTE, QTDE_CONTINUA)
        ioData.outDataBase(X, y)
        print("Base criada e guardada!")
    else:
        # Aqui voce recupera a base dados existente em CSV na pasta do projeto
        X, y = ioData.getData()
    
    #=================================================
    
    # Algoritmo de classificacao, e seu score na base de treinamento
    clf = svm.SVC(kernel='linear', C=1.0, probability=True)
    clf.fit(X, y)
    scores = cross_val_score(clf, X, y, cv =10)
    
    # Calculando falsos positivos e falsos negativos    
    zerosX, unsX = np.split(X, 2)
    result_zeros = clf.predict(zerosX)
    result_uns = clf.predict(unsX)
    falso_positivo = np.count_nonzero(result_zeros)
    falso_negativo = result_uns.size-np.count_nonzero(result_uns)
    
    #=================================================    

    # Apresentando e Salvando o resultado    
    print()
    print("Classificador: ", clf)
    print()
    print("Media e Desvio Padrão do modelo gerado: ", scores.mean(), scores.std())    
    print()
    print("Numero de vetores de suporte para cada classe: ", clf.n_support_)
    print()
    print("Indices dos vetores de suporte: ", clf.support_)
    print()
    print("Coeficientes na função de decisão dual: ", clf.dual_coef_)
    print()
    print("Pesos atribuídos às características (coeficientes no problema primal): ", clf.coef_)
    print()
    print("Constantes na função de decisão: ", clf.intercept_)
    print()
    print("Resultados dos objetos de entrada para o modelo aprendido", clf.decision_function(X))
    print()
    print("Numero de Falsos Positivos que a base de treinamento possui: ", falso_positivo)
    print("Numero de Falsos Negativos que a base de treinamento possui: ", falso_negativo)
    print()
    ioData.outResult(scores.mean(), scores.std(), clf, X, falso_positivo, falso_negativo)
    print()
    
    #=================================================
    
    # Testando o modelo com novos dados
    teste = 1000
    X_new, y_new = genData.genData(int(teste/2), int(teste/2))
    scores_new = cross_val_score(clf, X_new, y_new, cv =10)
    zerosX_new, unsX_new = np.split(X_new, 2)
    result_zeros_new = clf.predict(zerosX_new)
    result_uns_new = clf.predict(unsX_new)
    falso_positivo_new = np.count_nonzero(result_zeros_new)
    falso_negativo_new = result_uns_new.size-np.count_nonzero(result_uns_new)
    print("Nova base para testes possui (objetos) para cada classe: ", int(teste/2))
    print("Numero de Falsos Positivos que a nova base de teste possui: ", falso_positivo_new)
    print("Numero de Falsos Negativos que a nova base de teste possui: ", falso_negativo_new)
    print("Media e Desvio Padrão da nova Base para o modelo gerado: ", scores_new.mean(), scores_new.std())
    
    #=================================================
    
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
        