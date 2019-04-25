#from objects import *
import genData
import ioData
import numpy as np
from sklearn import svm
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import StandardScaler 

#==============================================================================================================            

class main:

    QTDE_DESISTE = 3000        
    QTDE_CONTINUA = 3000
    
    print("Podemos prever, baseando em alguns dados de um certo aluno universitario, se ele ira, muito provavelmete, continuar (1) ou desistir (0) do curso em algum momento proximo?")
    escolha = input('Para tal, voce gostaria de ciar uma nova base de dados (s/n)? Se já há uma base, ela será apagada caso sim: ')
    
    #=================================================
    
    if(escolha=='s'):
        # Estas duas linhas criam e salvam uma nova base de dados
        # Necessarias caso ainda nao exista uma
        # Isto apaga o que ja existe na pasta do projeto
        X, y = genData.genData(QTDE_DESISTE, QTDE_CONTINUA)
        ioData.outDataBase(X, y)
        print("Base criada e guardada!")
    else:
        # Aqui voce recupera a base dados existente em CSV na pasta do projeto
        X, y = ioData.getData()
    
    #=================================================
    
    # Normalizando os dados
    X_treino_escalar, y_treino_escalar = genData.genData(int(QTDE_DESISTE/4), int(QTDE_CONTINUA/4))
    scaler = StandardScaler()
    scaler.fit(X)
    
    #=================================================
    
    # Algoritmo de classificacao, e seu score na base de treinamento
    X_transformed = scaler.transform(X)
    clf = svm.SVC(kernel='linear', C=1.0, probability=True)
    clf.fit(X_transformed, y)
    scores = cross_val_score(clf, X_transformed, y, cv =10)
    
    # Calculando falsos positivos e falsos negativos    
    zerosX, unsX = np.split(X_transformed, 2)
    result_zeros = clf.predict(zerosX)
    result_uns = clf.predict(unsX)
    falso_positivo = np.count_nonzero(result_zeros)
    falso_negativo = result_uns.size-np.count_nonzero(result_uns)
    
    #=================================================    

    # Apresentando e Salvando o resultado
    print()
    print("Base para treinamento possui (objetos) para cada classe: ", QTDE_CONTINUA)    
    print()
    print("Classificador: ", clf)
    print()
    print("Score do modelo aplicado à essa base: ", clf.score(X_transformed, y))
    print("Media e Desvio Padrão (Validação Cruzada): ", scores.mean(), scores.std())    
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
    print("Resultados dos objetos de entrada para o modelo aprendido", clf.decision_function(X_transformed))
    print()
    print("Numero de Falsos Positivos que a base de treinamento possui: ", falso_positivo)
    print("Numero de Falsos Negativos que a base de treinamento possui: ", falso_negativo)
    print()
    ioData.outResult(scores, clf, X_transformed, X, y, falso_positivo, falso_negativo)
    print()
    
    #=================================================
    
    # Testando o modelo com novos dados
    teste = 1000
    X_test, y_test = genData.genData(int(teste/2), int(teste/2))
    X_test_transformed = scaler.transform(X_test_transformed)
    scores_test = cross_val_score(clf, X_test_transformed, y_test, cv =10)
    zerosX_test, unsX_test = np.split(X_test_transformed, 2)
    result_zeros_test = clf.predict(zerosX_test)
    result_uns_test = clf.predict(unsX_test)
    falso_positivo_test = np.count_nonzero(result_zeros_test)
    falso_negativo_test = result_uns_new.size-np.count_nonzero(result_uns_test)
    print("Nova base para testes possui (objetos) para cada classe: ", int(teste/2))
    print("Score do modelo aplicado à essa base: ", clf.score(X_test_transformed, y_test))
    print("Media e Desvio Padrão (Validação Cruzada): ", scores_test.mean(), scores_test.std())
    print("Numero de Falsos Positivos que a nova base de teste possui: ", falso_positivo_test)
    print("Numero de Falsos Negativos que a nova base de teste possui: ", falso_negativo_test)
    
    #=================================================
    
    # Testando o modelo gerado para novas entradas
    escolha = input('Voce quer testar um novo aluno?(s/n): ')
    while(escolha=='s'):
        dados = input('Valores (separados por virgulas): ')
        novo_X = dados.split(';')
        i = 0
        for i in range(len(novo_X)):
            novo_X[i] = float(novo_X[i])
        aluno = scaler.transform(novo_X)    
        print("Classificação, Prob. por classe e Valor resultante do modelo: ", clf.predict([aluno]), clf1.predict_proba([aluno]), clf1.decision_function([aluno]))
        escolha = input('Voce quer testar um novo aluno?(s/n): ')    
        
#==============================================================================================================
        