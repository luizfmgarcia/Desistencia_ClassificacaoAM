#from objects import *
from genData import *
from ioData import *
from sklearn import svm
from sklearn.model_selection import cross_val_score        
#==============================================================================================================            

class main: 
    # Use estas duas linhas para criar e salvar a base de dados caso ainda nao exista uma
    # Isto apaga o que ja existe na pasta do projeto
    X, y = genData1()
    outDataBase(X, y)
    
    # Aqui voce recupera a base dados existente em CSV na pasta do projeto
    X, y = getData()
    
    # Algoritmo de classificacao    
    clf = svm.SVC(gamma='scale')
    clf.fit(X, y)
    
    # Apresentando e Salvando o resultado
    scores = cross_val_score(clf, X, y, cv =10)
    print(scores.mean(), scores.std())
    outResult(scores.mean())
    
    # Testando o modelo gerado
    
#==============================================================================================================
