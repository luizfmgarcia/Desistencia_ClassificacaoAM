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
    X = [] #row 0 to 13
    y = [] #row 14
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
        spamwriter.writerow(['Curso', 'TurnoAulas', 'CursandoPeriodo', 'PerFaltas', 'NumReprovacoes', 'Convivio', 'Psicologico', 'Sexo', 'Idade', 'PossuiFilhos', 'RendaFamiliar', 'Trabalha', 'Bolsista', 'DistTrabalho', 'DistCasa', 'y'])
        i=0
        for i in range(y.size):
            row = np.append(X[i], y[i])
            spamwriter.writerow(row)
    csvfile.close()
    print ("Data Exported!")
        
#=============================================================================================================

def outResult(mean, std):
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
        #spamwriter.writerow(['', ''])
        row = np.append(mean, std)
        spamwriter.writerow(row)
    csvfile.close()  
    print ("Result Saved!")

#=============================================================================================================
