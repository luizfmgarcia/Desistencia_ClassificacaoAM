#from objects import *
from ioData import *
import numpy as np
# 'Curso', 'TurnoAulas', 'CursandoPeriodo', 'NumFaltas', 'NumReprovacoes', 'Bolsista', 'NumAmigos', 'Psicologico', 'Idade', 'Sexo', 'Trabalha', 'DistUniCasa', 'DistUniTrabalho', 'RendaFamiliar', 'NumFilhos'       
#==============================================================================================================            

def genData():
    
    QTDE_CONTINUA = 1000
    QTDE_DESISTE = 1000
    
    # Cursos
    # Exatas e engenharias - maiores desistencias
    # %desistencia: Humanas(0)10%; Exatas(1)30%; Biologicas(2)15%; Engenharias(3)35%; Licenciaturas(4)10%;
    # %continua: Humanas(0)25%; Exatas(1)20%; Biologicas(2)20%; Engenharias(3)10%; Licenciaturas(4)25%;
    cursos = range(0, 4)
    prob_desiste = [0.1, 0.30, 0.15, 0.35, 0.1]
    prob_continua = [0.25, 0.2, 0.2, 0.1, 0.25]
    curso_desiste = np.random.choice(cursos, QTDE_DESISTE, p=prob_desiste)
    curso_continua = np.random.choice(cursos, QTDE_CONTINUA, p=prob_continua)
    
    # Turno que as aulas ocorrem
    # Maires desistencias no noturno?
    # %desistencia: Matutino(0)15%; Vespertino(1)25%; Noturno(2)60%;
    # %continua: Matutino(0)50%; Vespertino(1)30%; Noturno(2)20%;
    turnos = range(0, 3)
    prob_desiste = [0.05, 0.1, 0.2]
    prob_continua = [0.95, 0.9, 0.8]
    turnos_desiste = np.random.choice(turnos, QTDE_DESISTE, p=prob_desiste)
    turnos_continua = np.random.choice(turnos, QTDE_CONTINUA, p=prob_continua)
    
    # Periodo que o aluno esta cursando atualmente
    # %desistencia: Primeiros_6Meses(0)70%; Entre_6Meses_2Anos(1)20%; Entre_2Anos_DuracaoTotalCurso(2)10%;
    periodos = range(0, 3)
    prob_desiste = [0.7, 0.2, 0.1]
    prob_continua = [0.3, 0.8, 0.9]
    periodo_desiste = np.random.choice(periodos, QTDE_DESISTE, p=prob_desiste)
    periodo_continua = np.random.choice(periodos, QTDE_CONTINUA, p=prob_continua)
    
    # Num faltas: % representa numero faltas em relacao ao total de aulas cursadas ate agora
    # quem falta mais tende a desistir mais facilmente
    faltas_desiste = np.random.normal(30, 30, QTDE_DESISTE)
    faltas_continua = np.random.normal(10, 10, QTDE_CONTINUA)
    
    # Numero de reprovacoes no curso
    # Quem reprova mais tende a desistir mais facilmente
    reprovacoes_desiste = np.random.uniform(0, 25, QTDE_DESISTE)
    reprovacoes_continua = np.random.uniform(0, 10, QTDE_CONTINUA)
    
    # Nao-Trab. (0); Trabalha (1)
    # matutino e vespertino sao muito poucos os que trabalham (5%); noturno (85%)
    # quem trabalha tende a desistir menos por almejar melhores posicoes na empresa
    # %desistencia: trabalha(10%), nao-trabalha(30%)
    trabalha_desiste = np.array()
    trabalha_continua = np.array()
    trabalha = range(0, 1)
    prob_desiste_matutino_vespertino = [0.15, 0.005]
    prob_continua_matutino_vespertino = [0.65, 0.85]
    prob_desiste_noturno = [0.35, 0.15]
    prob_continua_noturno = [0.65, 0.85]
    for aluno in turnos_desiste:
        # Matutino e Vespertino (5%)
        if(aluno==0 or aluno==1):
            trabalha_desiste.append(np.random.choice(periodos, 1, p=prob_desiste))
        # Noturno (85%)
        if(aluno==2):
            trabalha_desiste.append(np.random.normal(80,10,1))
            
    # Bolsista(algum beneficio/auxilio financeiro)(1), Nao_Bolsista(0)
    # Quem ganha um auxilio tende a se manter estudando
    # Quem ja trabalha (possui renda)
    
    # Idade dos alunos (entre 17 - 60) maior parte entre 18 e 25
    # maior desistencia entre os jovens ainda indecisos e em tempo de mudar de curso
    
    # DistTrabalho,
    
    # DistCasa 
    
    # Sexo: Feminino (0) Masculino (1) 
    # aprox. 50% cada
    
    # Num Filhos
    # maior parte nao possui e ha maior prob entre os mais velhos (acima 30 anos)
    # 
    
 
    
    # NumAmigos, 
    
    # Psicologico, 
    
    # RendaFamiliar, 

    
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
