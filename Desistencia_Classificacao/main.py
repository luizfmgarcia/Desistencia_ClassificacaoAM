#from objects import *
import genData
import ioData
from sklearn import svm
from sklearn.model_selection import cross_val_score        
#==============================================================================================================            

class main:
    
    print("Podemos prever, baseando em alguns dados de um certo aluno universitario, se ele ira, muito provavelmete, desistir do curso em algum tempo proximo?")
    escolha = input('Para tal, voce gostaria de ciar uma nova base de dados (s/n)? Se já há uma base, ela será apagada caso sim: ')
    
    if(escolha=='s'):
        # Estas duas linhas criam e salvam a base de dados caso ainda nao exista uma
        # Isto apaga o que ja existe na pasta do projeto
        X, y = genData.genData()
        ioData.outDataBase(X, y)
        print("Base criada e guardada!")
    else:
        # Aqui voce recupera a base dados existente em CSV na pasta do projeto
        X, y = ioData.getData()
    
    # Algoritmo de classificacao    
    clf = svm.SVC(gamma='scale')
    clf.fit(X, y)
    
    # Apresentando e Salvando o resultado
    scores = cross_val_score(clf, X, y, cv =10)
    print(clf, scores.mean(), scores.std())
    ioData.outResult(scores.mean(), scores.std(), clf)
    
    # Testando o modelo gerado para novas entradas
    escolha = input('Voce quer testar um novo aluno?(s/n): ')
    while(escolha=='s'):
        dados = input('Valores (separados por virgulas): ')
        novo_X = dados.split(';')
        i = 0
        for i in range(len(novo_X)):
            novo_X[i] = float(novo_X[i])
        print(clf.predict([novo_X]))
        escolha = input('Voce quer testar um novo aluno?(s/n): ')    
        
#==============================================================================================================
