# Import/Export Data Methods

#from objects import *
import csv
import os
import sys
import shutil
import numpy as np
   
#==============================================================================================================            
    
# Get all data to work
def getData(): 
    X = []
    y = [] # ultima coluna
    # Read the data and fill respective vectors
    first = True
    currentDir = os.getcwd()
    newDir = currentDir + os.sep + 'DatabaseCSV' + os.sep
    outName = newDir + 'dataBase.csv'
    with open(outName) as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';')
        for row in spamreader:
            # Removing the first line of the archieve
            if(first==True):
                first=False
            else:
                novo_row = row[:-1]
                for i in range(len(novo_row)):
                    novo_row[i] = float(row[i])
                X.append(novo_row)
                y.append(float(row[-1]))
    csvfile.close()     
    print ("Data Obtained!")
    
    return np.array(X), np.array(y)
        
#==============================================================================================================             

def outDataBase(X, y):
    print("Exporting database....",)
    
    # (Re)Creating Database file and director
    currentDir = os.getcwd()
    newDir = currentDir + os.sep + 'DatabaseCSV' + os.sep
    if not os.path.exists(newDir):
        os.makedirs(newDir)
    else:
        shutil.rmtree(newDir)
        os.makedirs(newDir)
    
    # this code starts the 'dataBase.csv' with the titles
    outName = newDir + 'dataBase.csv'                
    with open(outName, 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=';')
        spamwriter.writerow(['CursoHumana', 'CursoExata', 'CursoBiologica', 'CursoEngenharia', 'CursoLicenciatura', 'TurnoAulasMatutino', 'TurnoAulasVespertino', 'TurnoAulasNoturno', 'CursandoPeriodo', 'PerFaltas', 'NumReprovacoes', 'PerConvivencia', 'PerStress', 'SexoFeminino', 'SexoMasculino', 'Idade', 'PossuiFilhos', 'RendaFamiliar', 'Trabalha', 'Bolsista', 'DistTrabalho', 'DistCasa', 'y'])
        i=0
        for i in range(y.size):
            row = np.append(X[i], y[i])
            spamwriter.writerow(row)
    csvfile.close()
    print ("Data Exported!")
        
#=============================================================================================================

def outResult(scaler, scores, clf, X_transformed, X, y, falso_positivo, falso_negativo, indices_falsosPN):
    print("Exporting result....",)
    
    # (Re)Creating Database file and director
    currentDir = os.getcwd()
    newDir = currentDir + os.sep + 'ResultCSV' + os.sep
    if not os.path.exists(newDir):
        os.makedirs(newDir)
    else:
        shutil.rmtree(newDir)
        os.makedirs(newDir)
    
    # this code starts the 'dataBase.csv' with the titles
    outName = newDir + 'result.csv'                
    with open(outName, 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=';', quoting=csv.QUOTE_MINIMAL)
    
        spamwriter.writerow(["Normalizacao dos objetos"])
        spamwriter.writerow(["Valor medio encontrado para cada caracteristica na base de treinamento do Scaler: "])
        spamwriter.writerow(scaler.mean_)
        spamwriter.writerow([])
        spamwriter.writerow(["Variancia de cada caracteristica: "])
        spamwriter.writerow(scaler.var_)
        spamwriter.writerow([])
        spamwriter.writerow(["Dimensionamento relativo a cada caracteristica: "])
        spamwriter.writerow(scaler.scale_)
        spamwriter.writerow([])
    
        spamwriter.writerow(["Classificador: "])
        spamwriter.writerow([str(clf)])
        spamwriter.writerow([])
        
        spamwriter.writerow(["Score do modelo aplicado a essa base: "])
        spamwriter.writerow([clf.score(X, y)])
        spamwriter.writerow(["Media e Desvio Padrao (Validacao Cruzada de 10 pastas): "])
        spamwriter.writerow([scores.mean(), scores.std()])
        spamwriter.writerow([])
        
        spamwriter.writerow(["Numero de vetores de suporte para cada classe: "])
        spamwriter.writerow(clf.n_support_)
        spamwriter.writerow([])
        spamwriter.writerow(["Indices dos vetores de suporte: "])
        spamwriter.writerow(clf.support_)
        spamwriter.writerow([])
        
        spamwriter.writerow(["Coeficientes na funcao de decisao dual: "])
        for row in clf.dual_coef_:
            spamwriter.writerow(row)
        spamwriter.writerow([])
        
        spamwriter.writerow(["Pesos atribuidos as caracteristicas (coeficientes no problema primal): "])
        for row in clf.coef_:
            spamwriter.writerow(row)
        spamwriter.writerow([])
        
        spamwriter.writerow(["Constantes na funcao de decisao: "])
        spamwriter.writerow(clf.intercept_)
        spamwriter.writerow([])
        
        spamwriter.writerow(["Numero de Falsos Positivos que a base de treinamento possui: "])
        spamwriter.writerow([falso_positivo])
        spamwriter.writerow(["Numero de Falsos Negativos que a base de treinamento possui: "])
        spamwriter.writerow([falso_negativo])
        spamwriter.writerow(["Indices destes objetos 'erroneamente' classificados pelo modelo aprendido: "])
        spamwriter.writerow([indices_falsosPN])
        spamwriter.writerow([])
    
        spamwriter.writerow(["Resultados dos objetos de entrada para o modelo aprendido:"])
        spamwriter.writerow(clf.decision_function(X))
        spamwriter.writerow([])
            
        spamwriter.writerow(["Objetos transformados:"])
        for row in X_transformed:
            spamwriter.writerow(row)
        spamwriter.writerow([])
        
    csvfile.close()  
    print ("Result Saved!")

#=============================================================================================================
