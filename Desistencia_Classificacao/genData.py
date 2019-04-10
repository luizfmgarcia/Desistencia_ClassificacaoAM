#from objects import *
from ioData import *
import numpy as np
# Curso, PeriodoCurso, NumFaltas, NumReprovacoes, Idade, Trabalha, Sexo, NumFilhos, DistCasa, DistTrabalho, NumAmigos, Psicologico, RendaFamiliar, Bolsa      
#==============================================================================================================            

def genData():
    
    QTDE_CONTINUA = 1000
    QTDE_DESISTE = 1000
    
    # % Desistencia dos cursos
    # Humanas (0) 15%; Exatas (1) 30%; Engenharias (2) 45%; Licenciaturas (3) 10%;
    cursos = range(0, 4)
    prob_desiste = [0.15, 0.30, 0.45, 0.1]
    prob_continua = [0.85, 0.7, 0.55, 0.9]
    curso_desiste = np.random.choice(cursos, QTDE_DESISTE, p=prob_desiste)
    curso_continua = np.random.choice(cursos, QTDE_CONTINUA, p=prob_continua)
    
    # % Desistencia dependendo do periodo de estudo
    # Matutino (0) 5%; Vespertino (1) 10%; Noturno 20%;
    periodos = range(0, 3)
    prob_desiste = [0.05, 0.1, 0.2]
    prob_continua = [0.95, 0.9, 0.8]
    periodo_desiste = np.random.choice(periodos, QTDE_DESISTE, p=prob_desiste)
    periodo_continua = np.random.choice(periodos, QTDE_CONTINUA, p=prob_continua)
    
    # % de faltas em todas as aulas do curso
    # Quem falta mais tende a desistir mais facilmente
    faltas_desiste = np.random.normal(40, 20, QTDE_DESISTE)
    faltas_continua = np.random.normal(10, 10, QTDE_CONTINUA)
    
    # Numero de reprovacoes no curso
    # Quem reproma mais tende a desistir mais facilmente
    reprovacoes_desiste = np.random.uniform(0, 25, QTDE_DESISTE)
    reprovacoes_continua = np.random.uniform(0, 10, QTDE_CONTINUA)
    
    # Idade dos alunos (entre 17 - 60) maior parte entre 18 e 25
    
    # Trabalha (1) - Matutino e vespertino sao muito poucos
    
    # Sexo Feminino (0) Masculino (1) 50% cada
    
    # Num Filhos - maior parte nao possui
    
    # DistCasa, 
    
    # DistTrabalho, 
    
    # NumAmigos, 
    
    # Psicologico, 
    
    # RendaFamiliar, 
    
    # Bolsista
    
def genData1():        
    
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
