import numpy as np

# 'Curso', 'TurnoAulas', 'CursandoPeriodo', 'PerFaltas', 'NumReprovacoes', 'Convivio', 'Psicologico', 'Sexo', 'Idade', 'PossuiFilhos', 'RendaFamiliar', 'Trabalha', 'Bolsista', 'DistTrabalho', 'DistCasa'     

#==============================================================================================================            

def genData(QTDE_DESISTE, QTDE_CONTINUA):
    
    # Cursos:
    # Humanas(0); Exatas(1); Biologicas(2); Engenharias(3); Licenciaturas(4);
    # exatas e engenharias - maiores desistencias
    cursos = range(0, 5)
    prob_desiste = [0.1, 0.3, 0.15, 0.35, 0.1]
    prob_continua = [0.25, 0.2, 0.2, 0.1, 0.25]
    curso_desiste = np.random.choice(cursos, QTDE_DESISTE, p=prob_desiste)
    curso_continua = np.random.choice(cursos, QTDE_CONTINUA, p=prob_continua)
    
    #=========================================================
    
    # Turno que as aulas ocorrem:
    # Matutino(0); Vespertino(1); Noturno(2);
    # um pouco maior o numero de desistencias no noturno pelo cansaço, menos tempo de estudo, etc
    turnos = range(0, 3)
    prob_desiste = [0.3, 0.3, 0.4]
    prob_continua = [0.35, 0.35, 0.3]
    turnos_desiste = np.random.choice(turnos, QTDE_DESISTE, p=prob_desiste)
    turnos_continua = np.random.choice(turnos, QTDE_CONTINUA, p=prob_continua)
    
    #=========================================================
    
    # Colocar em meses....0 ao 24 e mais
    # Periodo do curso que o aluno esta matriculado/cursando atualmente:
    # Primeiros_6Meses(0); Entre_6Meses_2Anos(1); Entre_2Anos_DuracaoTotalCurso(2);
    # maior prob de desistir no inicio do curso
    periodos = range(0, 3)
    prob_desiste = [0.7, 0.2, 0.1]
    prob_continua = [0.1, 0.2, 0.7]
    periodo_desiste = np.random.choice(periodos, QTDE_DESISTE, p=prob_desiste)
    periodo_continua = np.random.choice(periodos, QTDE_CONTINUA, p=prob_continua)
    
    #=========================================================
    
    # Faltas(% de 0 a 100): 
    # A % representa a relacao do numero faltas ao numero total de aulas cursadas ate agora pelo aluno
    # quem falta mais tende a desistir mais facilmente
    faltas_desiste = np.absolute(np.round(np.random.normal(30, 15, QTDE_DESISTE), 0))
    faltas_continua = np.absolute(np.round(np.random.normal(10, 5, QTDE_CONTINUA), 0))
    
    #=========================================================
    
    # Reprovacoes no curso (escalar):
    # quem reprova mais tende a desistir mais facilmente
    reprovacoes_desiste = np.random.uniform(0, 15, QTDE_DESISTE)
    reprovacoes_continua = np.absolute(np.round(np.random.normal(5, 2, QTDE_CONTINUA), 0))
    reprovacoes_desiste = reprovacoes_desiste.astype('int32')
    reprovacoes_continua = reprovacoes_continua.astype('int32')
    
    #=========================================================
    
    # Convivio:
    # Pessimo convivio pode facilitar na decisao de desistencia
    # se sente: Otimo(0); Bom(1); Razoavel(2); Ruim(3); Pessimo(4); 
    # quem esta com psicologico fragil tende mais a desistir
    convivio = range(0, 5)
    prob_desiste = [0.05, 0.05, 0.2, 0.4, 0.3]
    prob_continua = [0.3, 0.3, 0.2, 0.1, 0.1]
    convivio_desiste = np.random.choice(convivio, QTDE_DESISTE, p=prob_desiste)
    convivio_continua = np.random.choice(convivio, QTDE_CONTINUA, p=prob_continua)
    
    #=========================================================
    
    # Psicologico:
    # se sente: Otimo(0); Bom(1); Razoavel(2); Ruim(3); Pessimo(4); 
    # quem esta com psicologico fragil tende mais a desistir
    psicologico = range(0, 5)
    prob_desiste = [0.1, 0.2, 0.2, 0.3, 0.2]
    prob_continua = [0.1, 0.3, 0.3, 0.15, 0.15]
    psicologico_desiste = np.random.choice(psicologico, QTDE_DESISTE, p=prob_desiste)
    psicologico_continua = np.random.choice(psicologico, QTDE_CONTINUA, p=prob_continua)
     
    #=========================================================                                       
    
    # Sexo:
    # Feminino(0); Masculino(1)
    # mulheres sao mais responsaveis
    sexos = range(0, 2)
    prob_desiste = [0.48, 0.52]
    prob_continua = [0.52, 0.48]
    sexos_desiste = np.random.choice(sexos, QTDE_DESISTE, p=prob_desiste)
    sexos_continua = np.random.choice(sexos, QTDE_CONTINUA, p=prob_continua)
    
    #=========================================================
    
    # Idade dos alunos (entre 17 - 60):
    # maior parte entre 17 e 30 (80%);
    # maior desistencia entre os jovens ate 23 anos (ainda indecisos e em tempo de mudar de curso)
    idade_desiste1 = np.random.normal(20, 3, int(QTDE_DESISTE*0.7))
    idade_desiste2 = np.random.uniform(24, 35, int(QTDE_DESISTE*0.2))
    idade_desiste3 = np.random.uniform(36, 60, int(QTDE_DESISTE*0.1))
    idade_desiste = np.append(idade_desiste1, idade_desiste2)
    idade_desiste = np.append(idade_desiste, idade_desiste3)
    idade_desiste = idade_desiste.astype('int32')
    #while(idade_desiste.size < QTDE_DESISTE):
    #    idade_desiste = np.append(idade_desiste, np.random.normal(20, 3, int(QTDE_DESISTE*0.8)))
    
    idade_continua1 = np.random.normal(20, 3, int(QTDE_CONTINUA*0.2))
    idade_continua2 = np.random.uniform(24, 35, int(QTDE_CONTINUA*0.5))
    idade_continua3 = np.random.uniform(36, 60, int(QTDE_CONTINUA*0.3))
    idade_continua = np.append(idade_continua1, idade_continua2)
    idade_continua = np.append(idade_continua, idade_continua3)
    idade_continua = idade_continua.astype('int32')
    #while(idade_continua.size < QTDE_CONTINUA):
    #    idade_continua = np.append(idade_continua, np.random.uniform(24, 35, int(QTDE_CONTINUA*0.5)))  
    
    #=========================================================
    
    # Filhos:
    # Nao-Possui(0); Possui(1)
    # maior parte nao possui e ha maior prob entre os mais velhos (acima 30 anos)
    # quem possui filho e tem mais de 30, a principio, e mais responsavel - menor desistencia
    # se tem menos de 30 pode acabar obtando por desistir mais facilmente
    filhos_desiste = np.array(None)
    for idade in idade_desiste:
        if(idade<30):
            resultado = np.random.rand(1) < 0.1
            if(resultado): filhos_desiste = np.append(filhos_desiste, 1)
            else: filhos_desiste = np.append(filhos_desiste, 0)
        if(idade>=30):    
            resultado = np.random.rand(1) < 0.05
            if(resultado): filhos_desiste = np.append(filhos_desiste, 1)
            else: filhos_desiste = np.append(filhos_desiste, 0)
    filhos_desiste = np.delete(filhos_desiste, 0)
    
    filhos_continua = np.array(None)        
    for idade in idade_continua:
        if(idade<30):
            resultado = np.random.rand(1) < 0.05
            if(resultado): filhos_continua = np.append(filhos_continua, 1)
            else: filhos_continua = np.append(filhos_continua, 0)
        if(idade>=30):    
            resultado = np.random.rand(1) < 0.15
            if(resultado): filhos_continua = np.append(filhos_continua, 1)
            else: filhos_continua = np.append(filhos_continua, 0)
    filhos_continua = np.delete(filhos_continua, 0)
    
    #=========================================================    
    
    # RendaFamiliar:
    # Baixa(0); Media(1); Alta(2);
    # ha mais pessoas de renda media nas universidades
    # quem possui renda alta tende mais a desistir pela comodidade
    # quem possui renda mais baixa tende mais a desistir pela dificuldade de se manter estudando
    rendaFamiliar = range(0, 3)
    prob_desiste = [0.3, 0.4, 0.3]
    prob_continua = [0.25, 0.5, 0.25]
    rendaFamiliar_desiste = np.random.choice(rendaFamiliar, QTDE_DESISTE, p=prob_desiste)
    rendaFamiliar_continua = np.random.choice(rendaFamiliar, QTDE_CONTINUA, p=prob_continua)       

    #=========================================================    

    # Nao-Trabalha(0) ou Trabalha(1)
    # matutino e vespertino sao muito poucos os que trabalham;
    # quem trabalha tende a desistir menos por almejar melhores posicoes na empresa
    trabalha_desiste = np.array(None)
    for turno in turnos_desiste:
        if(turno==2): # noturno
            resultado = np.random.rand(1) < 0.1
            if(resultado): trabalha_desiste = np.append(trabalha_desiste, 1)
            else: trabalha_desiste = np.append(trabalha_desiste, 0)
        if(turno!=2): # matutino e vespertino   
            resultado = np.random.rand(1) < 0.01
            if(resultado): trabalha_desiste = np.append(trabalha_desiste, 1)
            else: trabalha_desiste = np.append(trabalha_desiste, 0)
    trabalha_desiste = np.delete(trabalha_desiste, 0)
    
    trabalha_continua = np.array(None)        
    for turno in turnos_continua:
        if(turno==2): # noturno
            resultado = np.random.rand(1) < 0.8
            if(resultado): trabalha_continua = np.append(trabalha_continua, 1)
            else: trabalha_continua = np.append(trabalha_continua, 0)
        if(turno!=2): # matutino e vespertino  
            resultado = np.random.rand(1) < 0.1
            if(resultado): trabalha_continua = np.append(trabalha_continua, 1)
            else: trabalha_continua = np.append(trabalha_continua, 0) 
    trabalha_continua = np.delete(trabalha_continua, 0)
    
    #=========================================================    

    # Bolsista(algum beneficio/auxilio financeiro)(1), Nao_Bolsista(0)
    # Quem ganha um auxilio tende a se manter estudando
    # Quem ja trabalha (possui renda) minima prob. de receber auxilios
    bolsista_desiste = np.array(None)
    for trabalha in trabalha_desiste:
        if(trabalha):
            resultado = np.random.rand(1) < 0.05
            if(resultado): bolsista_desiste = np.append(bolsista_desiste, 1)
            else: bolsista_desiste = np.append(bolsista_desiste, 0)
        else:  
            resultado = np.random.rand(1) < 0.1
            if(resultado): bolsista_desiste = np.append(bolsista_desiste, 1)
            else: bolsista_desiste = np.append(bolsista_desiste, 0)
    bolsista_desiste = np.delete(bolsista_desiste, 0)
    
    bolsista_continua = np.array(None)        
    for trabalha in trabalha_continua:
        if(trabalha):
            resultado = np.random.rand(1) < 0.2
            if(resultado): bolsista_continua = np.append(bolsista_continua, 1)
            else: bolsista_continua = np.append(bolsista_continua, 0)
        else:  
            resultado = np.random.rand(1) < 0.8
            if(resultado): bolsista_continua = np.append(bolsista_continua, 1)
            else: bolsista_continua = np.append(bolsista_continua, 0) 
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
    X_desiste = np.vstack([curso_desiste, turnos_desiste, periodo_desiste, faltas_desiste, reprovacoes_desiste, convivio_desiste, psicologico_desiste, sexos_desiste, idade_desiste, filhos_desiste, rendaFamiliar_desiste, trabalha_desiste, bolsista_desiste, distTrab_desiste, distCasa_desiste]).T
    X_continua = np.vstack([curso_continua, turnos_continua, periodo_continua, faltas_continua, reprovacoes_continua, convivio_continua, psicologico_continua, sexos_continua, idade_continua, filhos_continua, rendaFamiliar_continua, trabalha_continua, bolsista_continua, distTrab_continua, distCasa_continua]).T
    X = np.vstack([X_desiste, X_continua]) # primeiro as desistencias, depois as continuidades
    y = np.array([0]*QTDE_DESISTE + [1]*QTDE_CONTINUA) # desiste = 0; continua = 1

    return X, y

#==============================================================================================================  
