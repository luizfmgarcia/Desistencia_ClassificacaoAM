#from objects import *
from genData import *
from ioData import *
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score        
#==============================================================================================================            

class main: 
    # Use estas duas linhas para criar e salvar a base de dados caso ainda nao exista uma
    # Isto apaga o que ja existe na pasta do projeto
    X, y = genData()
    outDataBase(X, y)
    
    # Aqui voce recupera a base dados existente em CSV na pasta do projeto
    X, y = getData()
    
    # Algoritmo de classificacao    
    clf = KNeighborsClassifier(n_neighbors=1)
    scores = cross_val_score(clf, X, y, cv =10)
    
    print(scores.mean(), scores.std()) # 94 ,5 + - 3 ,04%
    
    # Apresentando e Salvando o resultado
    outResult(scores.mean())
#==============================================================================================================