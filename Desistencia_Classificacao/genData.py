#from objects import *
from ioData import *
import numpy as np
# Curso, PeriodoCurso, NumFaltas, NumReprovacoes, Idade, Trabalha, Sexo, NumFilhos, DistCasa, DistTrabalho, NumAmigos, Psicologico, RendaFamiliar, Bolsa      
#==============================================================================================================            

def genData():
        
    QTDE_SUCESSO = 500
    QTDE_FRACASSO = 500
    
    # numero de horas de treino por dia
    # jogadores de sucesso tendem a treinar mais :
    horas_sucesso = np.random.normal(6, 2, QTDE_SUCESSO)
    # jogadores sem sucesso treinam menos
    horas_fracasso = np.random.uniform(0, 3, QTDE_FRACASSO)

    # chuta com os dois pes ?
    # 30% dos jogares bem sucedidos chutam com os dois pes
    pes_sucesso = np.random.rand(QTDE_SUCESSO) > 0.7
    # mas so 10% dos jogadores sem sucesso
    pes_fracasso = np.random.rand(QTDE_SUCESSO) > 0.9
    
    # 10 agentes
    agentes = range(0 , 10)
    
    # agentes 0 ,1 ,2: 15% dos sucessos
    # agentes 3 ,4 ,5 ,6: 10% dos sucessos
    # agentes 7 ,8 ,9: 5% dos sucessos
    prob_sucesso = [0.15, 0.15, 0.15, 0.1, 0.1, 0.1, 0.1, 0.05, 0.05, 0.05]
    
    agente_sucesso = np.random.choice(agentes, QTDE_SUCESSO, p=prob_sucesso)
    
    # agentes 0 ,1 ,2: 5% dos fracassos
    # agentes 3 ,4 ,5 ,6: 10% dos fracassos
    # agentes 7 ,8 ,9: 15% dos fracassos
    prob_fracasso = np.flip(prob_sucesso, 0)
    agente_fracasso = np.random.choice(agentes, QTDE_FRACASSO, p=prob_fracasso)
    
    X_sucesso = np.vstack([horas_sucesso, pes_sucesso, agente_sucesso]).T
    X_fracasso = np.vstack([horas_fracasso, pes_fracasso, agente_fracasso]).T
    
    X = np.vstack([X_fracasso, X_sucesso]) # primeiro os fracassos , depois os sucessos
    y = np.array([0]*QTDE_FRACASSO + [1]*QTDE_SUCESSO) # 500 zeros seguidos de 500 uns
    
    return X, y
