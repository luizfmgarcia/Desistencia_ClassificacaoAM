# Import/Export Data Methods

#from objects import *
import csv
import os
import sys
import shutil
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = (9.0, 6.0)
   
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

def graphic1(clf):
    
    top_features = 11
    feature_names = ['CursoHumana', 'CursoExata', 'CursoBiologica', 'CursoEngenharia', 'CursoLicenciatura', 'TurnoAulasMatutino', 'TurnoAulasVespertino', 'TurnoAulasNoturno', 'CursandoPeriodo', 'PerFaltas', 'NumReprovacoes', 'PerConvivencia', 'PerStress', 'SexoFeminino', 'SexoMasculino', 'Idade', 'PossuiFilhos', 'RendaFamiliar', 'Trabalha', 'Bolsista', 'DistTrabalho', 'DistCasa']
    coef = clf.coef_.ravel()
    top_positive_coefficients = np.argsort(coef)[-top_features:]
    top_negative_coefficients = np.argsort(coef)[:top_features]
    top_coefficients = np.hstack([top_negative_coefficients, top_positive_coefficients])
    # create plot
    plt.figure(figsize=(15, 5))
    colors = ['red' if c < 0 else 'blue' for c in coef[top_coefficients]]
    plt.bar(np.arange(2*top_features), coef[top_coefficients], color=colors)
    feature_names = np.array(feature_names)
    plt.xticks(np.arange(0, 2*top_features), feature_names[top_coefficients], rotation=60, ha='right')
    
    plt.title("Features Weights on learned SVM Model")
    plt.grid(True)
    plt.xlabel("Features")
    plt.ylabel("Weight")
    plt.show()

#=============================================================================================================
    
def make_meshgrid(x, y, h=.02):
    x_min, x_max = x.min() - 1, x.max() + 1
    y_min, y_max = y.min() - 1, y.max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
    return xx, yy

def plot_contours(ax, clf, xx, yy, **params):
    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    out = ax.contourf(xx, yy, Z, **params)
    return out

def graphic2(X, y, clf):
    
    fig, ax = plt.subplots()
    # title for the plots
    title = ('Decision surface of linear SVC ')
    # Set-up grid for plotting.
    X0, X1 = X[:, 0], X[:, 1]
    xx, yy = make_meshgrid(X0, X1)
    
    plot_contours(ax, clf, xx, yy, cmap=plt.cm.coolwarm, alpha=0.8)
    ax.scatter(X0, X1, c=y, cmap=plt.cm.coolwarm, s=20, edgecolors='k')
    ax.set_ylabel('PC2')
    ax.set_xlabel('PC1')
    ax.set_xticks(())
    ax.set_yticks(())
    ax.set_title('Decison surface using the PCA transformed/projected features')
    ax.legend()
    plt.show()

#=============================================================================================================

def graphic3(X, y, clf):

    plt.scatter(X[:, 0], X[:, 1], c=y, s=20, cmap=plt.cm.Paired)

    # plot the decision function
    ax = plt.gca()
    xlim = ax.get_xlim()
    ylim = ax.get_ylim()
    
    # create grid to evaluate model
    xx = np.linspace(xlim[0], xlim[1], 20)
    yy = np.linspace(ylim[0], ylim[1], 20)
    YY, XX = np.meshgrid(yy, xx)
    xy = np.vstack([XX.ravel(), YY.ravel()]).T
    Z = clf.decision_function(xy).reshape(XX.shape)
    
    # plot decision boundary and margins
    ax.contour(XX, YY, Z, colors='k', levels=[-1, 0, 1], alpha=0.5, linestyles=['--', '-', '--'])
    # plot support vectors
    ax.scatter(clf.support_vectors_[:, 0], clf.support_vectors_[:, 1], s=200, linewidth=1, facecolors='none', edgecolors='k')
    ax.set_title('Maximum margin separating hyperplane')
    plt.show()

#=============================================================================================================

def graphic4(X, y, svm):
    plt.rcParams['figure.figsize'] = (36.0, 24.0)
    # we create an instance of SVM and fit out data. We do not scale our
    # data since we want to plot the support vectors
    C = 100.0  # SVM regularization parameter
    models = (svm.SVC(kernel='linear', C=C), svm.LinearSVC(C=C), svm.SVC(kernel='rbf', gamma=0.7, C=C), svm.SVC(kernel='poly', degree=3, C=C))
    models = (clf.fit(X, y) for clf in models)
    
    # title for the plots
    titles = ('SVC with linear kernel','LinearSVC (linear kernel)', 'SVC with RBF kernel', 'SVC with polynomial (degree 3) kernel')
    
    # Set-up 2x2 grid for plotting.
    #fig, sub = plt.subplots(2, 2)
    #plt.subplots_adjust(wspace=0.4, hspace=0.4)
    plt.rcParams['figure.figsize'] = (9.0, 6.0)
    X0, X1 = X[:, 0], X[:, 1]
    xx, yy = make_meshgrid(X0, X1)
    
    for clf, title in zip(models, titles):
    #for clf, title, ax in zip(models, titles, sub.flatten()):
        ax = plt.gca()
        plot_contours(ax, clf, xx, yy, cmap=plt.cm.coolwarm, alpha=0.8)
        ax.scatter(X0, X1, c=y, cmap=plt.cm.coolwarm, s=20, edgecolors='k')
        ax.set_xlim(xx.min(), xx.max())
        ax.set_ylim(yy.min(), yy.max())
        ax.set_xticks(())
        ax.set_yticks(())
        ax.set_title(title)
        plt.show()    