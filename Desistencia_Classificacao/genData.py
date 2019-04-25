import numpy as np

# 'CursoHumana', 'CursoExata', 'CursoBiologica', 'CursoEngenharia', 'CursoLicenciatura', 'TurnoAulasMatutino', 'TurnoAulasVespertino', 'TurnoAulasNoturno', 'CursandoPeriodo', 'PerFaltas', 'NumReprovacoes', 'PerConvivencia', 'PerStress', 'SexoFeminino', 'SexoMasculino', 'Idade', 'PossuiFilhos', 'RendaFamiliar', 'Trabalha', 'Bolsista', 'DistTrabalho', 'DistCasa'

#==============================================================================================================            

def genData(QTDE_DESISTE, QTDE_CONTINUA):
    
    # Cursos:
    # Humanas(0); Exatas(1); Biologicas(2); Engenharias(3); Licenciaturas(4);
    # exatas e engenharias - maiores desistencias
    vetores_desiste = [np.array(None), np.array(None), np.array(None), np.array(None), np.array(None)]
    vetores_continua = [np.array(None), np.array(None), np.array(None), np.array(None), np.array(None)]
    cursos = range(0, 5)
    prob_desiste = [0.1, 0.3, 0.15, 0.35, 0.1]
    prob_continua = [0.25, 0.2, 0.2, 0.1, 0.25]
    
    i = 0
    for i in range(QTDE_DESISTE): 
        curso_desiste = np.random.choice(cursos, 1, p=prob_desiste)
        curso_continua = np.random.choice(cursos, 1, p=prob_continua)
        j=0
        for j in range(len(cursos)):
            if(j == curso_desiste):
                vetores_desiste[j] = np.append(vetores_desiste[j], 1)
            else:
                vetores_desiste[j]= np.append(vetores_desiste[j], 0)
            if(j == curso_continua):
                vetores_continua[j]= np.append(vetores_continua[j], 1)
            else:
                vetores_continua[j]= np.append(vetores_continua[j], 0)
                
    curso0_desiste = np.delete(vetores_desiste[0], 0)
    curso1_desiste = np.delete(vetores_desiste[1], 0)
    curso2_desiste = np.delete(vetores_desiste[2], 0)
    curso3_desiste = np.delete(vetores_desiste[3], 0)
    curso4_desiste = np.delete(vetores_desiste[4], 0)
    
    curso0_continua = np.delete(vetores_continua[0], 0)
    curso1_continua = np.delete(vetores_continua[1], 0)
    curso2_continua = np.delete(vetores_continua[2], 0)
    curso3_continua = np.delete(vetores_continua[3], 0)
    curso4_continua = np.delete(vetores_continua[4], 0)
    
    #=========================================================
    
    # Turno que as aulas ocorrem:
    # Matutino(0); Vespertino(1); Noturno(2);
    # um pouco maior o numero de desistencias no noturno pelo: cansaço, menos tempo de estudo, etc
    vetores_desiste = [np.array(None), np.array(None), np.array(None)]
    vetores_continua = [np.array(None), np.array(None), np.array(None)]
    turnos = range(0, 3)
    prob_desiste = [0.3, 0.3, 0.4]
    prob_continua = [0.35, 0.35, 0.3]
    
    i = 0
    for i in range(QTDE_DESISTE): 
        turnos_desiste = np.random.choice(turnos, 1, p=prob_desiste)
        turnos_continua = np.random.choice(turnos, 1, p=prob_continua)
        j=0
        for j in range(len(turnos)):
            if(j == turnos_desiste):
                vetores_desiste[j] = np.append(vetores_desiste[j], 1)
            else:
                vetores_desiste[j] = np.append(vetores_desiste[j], 0)
            if(j == turnos_continua):
                vetores_continua[j] = np.append(vetores_continua[j], 1)
            else:
                vetores_continua[j] = np.append(vetores_continua[j], 0)
                
    turno0_desiste = np.delete(vetores_desiste[0], 0)
    turno1_desiste = np.delete(vetores_desiste[1], 0)
    turno2_desiste = np.delete(vetores_desiste[2], 0)
    
    turno0_continua = np.delete(vetores_continua[0], 0)
    turno1_continua = np.delete(vetores_continua[1], 0)
    turno2_continua = np.delete(vetores_continua[2], 0)
    
    #=========================================================
    
    # Periodo do curso que o aluno esta matriculado/cursando atualmente (Mês):
    # Primeiros_6Meses(0) 1 a 6; Entre_6Meses_2Anos(1) 7 a 24; Entre_2Anos_DuracaoTotalCurso(2) 25 a 48;
    # maior prob de desistir no inicio do curso
    periodos = range(0, 3)
    prob_desiste = [0.7, 0.2, 0.1]
    prob_continua = [0.1, 0.2, 0.7]
    periodo_desiste = np.array(None)
    periodo_continua = np.array(None)
    
    i = 0
    for i in range(QTDE_CONTINUA):
        desiste = np.random.choice(periodos, 1, p=prob_desiste)
        if(desiste == 0):
            periodo_desiste = np.append(periodo_desiste, np.random.uniform(1, 6, 1))
        elif(desiste == 1):
            periodo_desiste = np.append(periodo_desiste, np.random.uniform(7, 24, 1))
        elif(desiste == 2):
            periodo_desiste = np.append(periodo_desiste, np.random.uniform(25, 48, 1))
        
        continua = np.random.choice(periodos, 1, p=prob_continua)
        if(continua == 0):
            periodo_continua = np.append(periodo_continua, np.random.uniform(1, 6, 1))
        elif(continua == 1):
            periodo_continua = np.append(periodo_continua, np.random.uniform(7, 24, 1))
        elif(continua == 2):
            periodo_continua = np.append(periodo_continua, np.random.uniform(25, 48, 1))   
    
    periodo_desiste = np.delete(periodo_desiste, 0).astype('int32')
    periodo_continua = np.delete(periodo_continua, 0).astype('int32')
    
    #=========================================================
    
    # Faltas(% de 0 a 100): 
    # A % representa a relacao do numero faltas ao numero total de aulas cursadas ate agora pelo aluno
    # quem falta mais tende a desistir mais facilmente
    faltas_desiste = np.absolute(np.round(np.random.normal(30, 15, QTDE_DESISTE), 2))
    faltas_continua = np.absolute(np.round(np.random.normal(10, 5, QTDE_CONTINUA), 2))
    
    #=========================================================
    
    # Reprovacoes no curso (escalar):
    # quem reprova mais tende a desistir mais facilmente
    reprovacoes_desiste = np.random.uniform(0, 15, QTDE_DESISTE).astype('int32')
    reprovacoes_continua = np.absolute(np.random.normal(5, 2, QTDE_CONTINUA)).astype('int32')
    
    #=========================================================
    
    # Convivencia(% de 0 a 100):
    # Pessimo convivio pode facilitar na decisao de desistencia
    # nivel mais baixo (pessimo) 0 / nivel alto (otimo) 100
    convivio_desiste = np.array(None)
    convivio_continua = np.array(None)
    
    i = 0
    for i in range(QTDE_CONTINUA):
        desiste = np.absolute(np.round(np.random.normal(30, 15, 1), 2))
        continua = np.absolute(np.round(np.random.normal(70, 15, 1), 2))
        if(desiste>100.0):
            desiste = 100.0
        if(continua>100.0):
            continua = 100.0
        convivio_desiste = np.append(convivio_desiste, desiste)
        convivio_continua = np.append(convivio_continua, continua)
        
    convivio_desiste = np.delete(convivio_desiste, 0)
    convivio_continua = np.delete(convivio_continua, 0)
    
    #=========================================================
    
    # Nivel de Stress(% de 0 a 100):
    # baixo stress 0 / alto stress 100 
    # quem esta com mais stress tende mais a desistir
    stress_desiste = np.array(None)
    stress_continua = np.array(None)
    
    i = 0
    for i in range(QTDE_CONTINUA):
        desiste = np.absolute(np.round(np.random.normal(70, 15, 1), 2))
        continua = np.absolute(np.round(np.random.normal(30, 15, 1), 2))
        if(desiste>100):
            desiste = 100
        if(continua>100):
            continua = 100
        stress_desiste = np.append(stress_desiste, desiste)
        stress_continua = np.append(stress_continua, continua)
        
    stress_desiste = np.delete(stress_desiste, 0)
    stress_continua = np.delete(stress_continua, 0) 
    
    #=========================================================                                       
    
    # Sexo:
    # Feminino(0); Masculino(1)
    # mulheres sao mais responsaveis
    vetores_desiste = [np.array(None), np.array(None)]
    vetores_continua = [np.array(None), np.array(None)]
    sexos = range(0, 2)
    prob_desiste = [0.48, 0.52]
    prob_continua = [0.52, 0.48]
    
    i = 0
    for i in range(QTDE_DESISTE): 
        sexos_desiste = np.random.choice(sexos, 1, p=prob_desiste)
        sexos_continua = np.random.choice(sexos, 1, p=prob_continua)
        j=0
        for j in range(len(sexos)):
            if(j == sexos_desiste):
                vetores_desiste[j] = np.append(vetores_desiste[j], 1)
            else:
                vetores_desiste[j] = np.append(vetores_desiste[j], 0)
            if(j == sexos_continua):
                vetores_continua[j] = np.append(vetores_continua[j], 1)
            else:
                vetores_continua[j] = np.append(vetores_continua[j], 0)
                
    sexo0_desiste = np.delete(vetores_desiste[0], 0)
    sexo1_desiste = np.delete(vetores_desiste[1], 0)
    
    sexo0_continua = np.delete(vetores_continua[0], 0)
    sexo1_continua = np.delete(vetores_continua[1], 0)
    
    #=========================================================
    
    # Idade dos alunos (entre 17 - 60):
    # maior parte entre 17 e 30 (80%);
    # maior desistencia entre os jovens ate 23 anos (ainda indecisos e em tempo de mudar de curso)
    idade_desiste1 = np.absolute(np.random.normal(20, 3, int(QTDE_DESISTE*0.7)))
    idade_desiste2 = np.random.uniform(24, 35, int(QTDE_DESISTE*0.2))
    idade_desiste3 = np.random.uniform(36, 60, int(QTDE_DESISTE*0.1))
    idade_desiste = np.append(idade_desiste1, idade_desiste2)
    idade_desiste = np.append(idade_desiste, idade_desiste3).astype('int32')
    #idade_desiste = idade_desiste.astype('int32')
    #while(idade_desiste.size < QTDE_DESISTE):
    #    idade_desiste = np.append(idade_desiste, np.random.normal(20, 3, int(QTDE_DESISTE*0.8)))
    
    idade_continua1 = np.absolute(np.random.normal(20, 3, int(QTDE_CONTINUA*0.2)))
    idade_continua2 = np.random.uniform(24, 35, int(QTDE_CONTINUA*0.5))
    idade_continua3 = np.random.uniform(36, 60, int(QTDE_CONTINUA*0.3))
    idade_continua = np.append(idade_continua1, idade_continua2)
    idade_continua = np.append(idade_continua, idade_continua3).astype('int32')
    #idade_continua = idade_continua.astype('int32')
    #while(idade_continua.size < QTDE_CONTINUA):
    #    idade_continua = np.append(idade_continua, np.random.uniform(24, 35, int(QTDE_CONTINUA*0.5)))  
    
    #=========================================================
    
    # Filhos:
    # Nao-Possui(0); Possui(1)
    # maior parte nao possui e ha maior prob entre os mais velhos (acima 30 anos)
    # quem possui filho e tem mais de 30, a principio, e mais responsavel - menor desistencia
    # se tem menos de 30 pode acabar obtando por desistir mais facilmente
    filhos_desiste = np.array(None)
    i = 0
    for idade in idade_desiste:
        if(idade<30):
            resultado = np.random.rand(1) < 0.1
            if(resultado):
                filhos_desiste = np.append(filhos_desiste, 1)
            else:
                filhos_desiste = np.append(filhos_desiste, 0)
        if(idade>=30):    
            resultado = np.random.rand(1) < 0.05
            if(resultado):
                filhos_desiste = np.append(filhos_desiste, 1)
            else: 
                filhos_desiste = np.append(filhos_desiste, 0)
    filhos_desiste = np.delete(filhos_desiste, 0)
    
    filhos_continua = np.array(None)        
    for idade in idade_continua:
        if(idade<30):
            resultado = np.random.rand(1) < 0.05
            if(resultado):
                filhos_continua = np.append(filhos_continua, 1)
            else:
                filhos_continua = np.append(filhos_continua, 0)
        if(idade>=30):    
            resultado = np.random.rand(1) < 0.15
            if(resultado):
                filhos_continua = np.append(filhos_continua, 1)
            else:
                filhos_continua = np.append(filhos_continua, 0)
    filhos_continua = np.delete(filhos_continua, 0)
    
    #=========================================================    
    
    # RendaFamiliar(Numero de Salarios Minimos):
    # Baixa(0) 1 a 3; Media(1) 4 a 7; Alta(2) 8 a 12;
    # ha mais pessoas de renda media nas universidades
    # quem possui renda alta tende mais a desistir pela comodidade
    # quem possui renda mais baixa tende mais a desistir pela dificuldade de se manter estudando
    rendaFamiliar = range(0, 3)
    prob_desiste = [0.3, 0.4, 0.3]
    prob_continua = [0.25, 0.5, 0.25]
    rendaFamiliar_desiste = np.array(None)
    rendaFamiliar_continua = np.array(None)
    
    i = 0
    for i in range(QTDE_CONTINUA):
        desiste = np.random.choice(rendaFamiliar, 1, p=prob_desiste)
        if(desiste == 0):
            rendaFamiliar_desiste = np.append(rendaFamiliar_desiste, np.random.uniform(1, 3, 1))
        elif(desiste == 1):
            rendaFamiliar_desiste = np.append(rendaFamiliar_desiste, np.random.uniform(4, 7, 1))
        elif(desiste == 2):
            rendaFamiliar_desiste = np.append(rendaFamiliar_desiste, np.random.uniform(8, 12, 1))
        
        continua = np.random.choice(rendaFamiliar, 1, p=prob_continua)
        if(continua == 0):
            rendaFamiliar_continua = np.append(rendaFamiliar_continua, np.random.uniform(1, 3, 1))
        elif(continua == 1):
            rendaFamiliar_continua = np.append(rendaFamiliar_continua, np.random.uniform(4, 7, 1))
        elif(continua == 2):
            rendaFamiliar_continua = np.append(rendaFamiliar_continua, np.random.uniform(8, 12, 1))
    
    rendaFamiliar_desiste = np.delete(rendaFamiliar_desiste, 0).astype('int32')
    rendaFamiliar_continua = np.delete(rendaFamiliar_continua, 0).astype('int32')  
    
    #=========================================================    

    # Nao-Trabalha(0) ou Trabalha(1)
    # matutino e vespertino sao muito poucos os que trabalham;
    # quem trabalha tende a desistir menos por almejar melhores posicoes na empresa
    trabalha_desiste = np.array(None)
    i = 0
    for i in range(QTDE_DESISTE):
        if(turno2_desiste[i]==1): # noturno
            resultado = np.random.rand(1) < 0.1
            if(resultado): 
                trabalha_desiste = np.append(trabalha_desiste, 1)
            else: 
                trabalha_desiste = np.append(trabalha_desiste, 0)
        else: # matutino e vespertino   
            resultado = np.random.rand(1) < 0.01
            if(resultado): 
                trabalha_desiste = np.append(trabalha_desiste, 1)
            else: 
                trabalha_desiste = np.append(trabalha_desiste, 0)
    trabalha_desiste = np.delete(trabalha_desiste, 0)
    
    trabalha_continua = np.array(None)        
    i = 0
    for i in range(QTDE_CONTINUA):
        if(turno2_continua[i]==1): # noturno
            resultado = np.random.rand(1) < 0.8
            if(resultado): 
                trabalha_continua = np.append(trabalha_continua, 1)
            else: 
                trabalha_continua = np.append(trabalha_continua, 0)
        else: # matutino e vespertino  
            resultado = np.random.rand(1) < 0.1
            if(resultado): 
                trabalha_continua = np.append(trabalha_continua, 1)
            else: 
                trabalha_continua = np.append(trabalha_continua, 0) 
    trabalha_continua = np.delete(trabalha_continua, 0)
    
    #=========================================================    

    # Bolsista(algum beneficio/auxilio financeiro)(1), Nao_Bolsista(0)
    # Quem ganha um auxilio tende a se manter estudando
    # Quem ja trabalha (possui renda) minima prob. de receber auxilios
    bolsista_desiste = np.array(None)
    for trabalha in trabalha_desiste:
        if(trabalha):
            resultado = np.random.rand(1) < 0.05
            if(resultado):
                bolsista_desiste = np.append(bolsista_desiste, 1)
            else:
                bolsista_desiste = np.append(bolsista_desiste, 0)
        else:  
            resultado = np.random.rand(1) < 0.1
            if(resultado):
                bolsista_desiste = np.append(bolsista_desiste, 1)
            else:
                bolsista_desiste = np.append(bolsista_desiste, 0)
    bolsista_desiste = np.delete(bolsista_desiste, 0)
    
    bolsista_continua = np.array(None)        
    for trabalha in trabalha_continua:
        if(trabalha):
            resultado = np.random.rand(1) < 0.2
            if(resultado):
                bolsista_continua = np.append(bolsista_continua, 1)
            else:
                bolsista_continua = np.append(bolsista_continua, 0)
        else:  
            resultado = np.random.rand(1) < 0.8
            if(resultado):
                bolsista_continua = np.append(bolsista_continua, 1)
            else:
                bolsista_continua = np.append(bolsista_continua, 0) 
    bolsista_continua = np.delete(bolsista_continua, 0)
    
    #=========================================================    

    # DistTrabalho (Km):
    # distancia 0 pra quem nao trabalha
    # quem trabalha mais longe tende a desistir mais facilmente (pelo cansaço, stress do transito etc)
    distTrab_desiste = np.array(None)
    for trabalha in trabalha_desiste:
        if(trabalha):
            distTrab_desiste = np.append(distTrab_desiste, np.absolute(np.round(np.random.normal(25, 5, 1), 2)))    
        else:
            distTrab_desiste = np.append(distTrab_desiste, 0)
    distTrab_desiste = np.delete(distTrab_desiste, 0)
    
    distTrab_continua = np.array(None)        
    for trabalha in trabalha_continua:
        if(trabalha):
            distTrab_continua = np.append(distTrab_continua, np.round(np.random.uniform(0, 20, 1), 2))    
        else:  
            distTrab_continua = np.append(distTrab_continua, 0) 
    distTrab_continua = np.delete(distTrab_continua, 0)

    #=========================================================    
    
    # DistCasa (Km):
    # quem mora mais longe tende a desistir mais facilmente (pelo cansaço, stress do transito etc)
    distCasa_desiste = np.absolute(np.round(np.random.normal(25, 5, QTDE_DESISTE), 2))
    distCasa_continua = np.round(np.random.uniform(0, 20, QTDE_CONTINUA), 2)   

    #=========================================================    
 
    # Juntando tudo
    X_desiste = np.vstack([curso0_desiste, curso1_desiste, curso2_desiste, curso3_desiste, curso4_desiste, turno0_desiste, turno1_desiste, turno2_desiste, periodo_desiste, faltas_desiste, reprovacoes_desiste, convivio_desiste, stress_desiste, sexo0_desiste, sexo1_desiste, idade_desiste, filhos_desiste, rendaFamiliar_desiste, trabalha_desiste, bolsista_desiste, distTrab_desiste, distCasa_desiste]).T
    X_continua = np.vstack([curso0_continua, curso1_continua, curso2_continua, curso3_continua, curso4_continua, turno0_continua, turno1_continua, turno2_continua, periodo_continua, faltas_continua, reprovacoes_continua, convivio_continua, stress_continua, sexo0_continua, sexo1_continua, idade_continua, filhos_continua, rendaFamiliar_continua, trabalha_continua, bolsista_continua, distTrab_continua, distCasa_continua]).T
    X = np.vstack([X_desiste, X_continua]) # primeiro as desistencias, depois as continuidades
    y = np.array([0]*QTDE_DESISTE + [1]*QTDE_CONTINUA) # desiste = 0; continua = 1

    return X, y

#==============================================================================================================  
