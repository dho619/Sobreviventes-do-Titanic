import pandas as pd

def separar_por_idade(data, nome_index):
    age_convertida = []
    for idade in data[nome_index]:
       if idade > 60:
           age_convertida.append('Idoso')
       elif idade > 18:
           age_convertida.append('Adulto')
       elif idade > 12:
           age_convertida.append('Adolescente')
       elif idade > 1:
           age_convertida.append('Crianca')
       else:
           age_convertida.append('Bebe')

    return age_convertida

titanic_data = pd.read_csv('titanic_data.csv')#local do arquivo de amostra dos dados
titanic_data['Age_convertida'] = separar_por_idade(titanic_data, 'Age') #Adicionando nova coluna, com idade convertida
sobreviventes =  titanic_data['Survived'].sum()


grupo_classes = titanic_data.groupby('Pclass')
total_por_classe = grupo_classes['Survived'].sum() / sobreviventes

'''
INFORMACOES COLETADAS:
    1ª Classe teve 136(39.77%) dos sobreviventes sendo 216(24.24%) dos 891 passageiros da amostra! Sobreviveu 62.96% deles.
    2ª Classe teve  87(25.44%) dos sobreviventes sendo 184(20.65%) dos 891 passageiros da amostra! Sobreviveu 47.28% deles.
    3ª Classe teve 119(34.79%) dos sobreviventes sendo 491(55.11%) dos 891 passageiros da amostra! Sobreviveu 24.24% deles.
    
   Os dados de que 34.79% por cento dos sobrevivente era de classe baixa pode enganar, pensando que eles tiveram mais
   chance que a classe media, mas quando olhado o total deles, percebesse que menos 1/4 sobreviveu, mas como eram maioria,
   aparentam ser muitos dos sobreviventes!
'''

grupo_por_sexo = titanic_data.groupby('Sex')
total_por_sexo = grupo_por_sexo['Survived'].sum() / sobreviventes

'''
INFORMACOES COLETADAS:
    Sexo Feminino  233(68.13%) dos sobreviventes sendo 314(35.24%) dos 891 passageiros da amostra! Sobreviveu 74.20% delas.
    Sexo Masculino 109(31.87%) dos sobreviventes sendo 577(64.76%) dos 891 passageiros da amostra! Sobreviveu 18.91% deles
    
    Igualdade nessas horas, as feministas não quer ashashshas
'''

grupo_por_idade = titanic_data.groupby('Age_convertida')
total_idade = grupo_por_idade['Survived'].sum() / sobreviventes

'''
INFORMACOES COLETADAS:
    Bebes         64(18.71%) dos sobreviventes sendo 191(21.44%) dos 891 passageiros da amostra! Sobreviveu 33.51% deles.
    Criancas      28(08.19%) dos sobreviventes sendo  55(06.17%) dos 891 passageiros da amostra! Sobreviveu 50.91% deles.
    Adolescentes  30(08.77%) dos sobreviventes sendo  70(07.86%) dos 891 passageiros da amostra! Sobreviveu 42.86% deles.
    Adultos      215(62.77%) dos sobreviventes sendo 553(62.07%) dos 891 passageiros da amostra! Sobreviveu 38.88% deles.
    Idosos         5(01.46%) dos sobreviventes sendo  22(02.47%) dos 891 passageiros da amostra! Sobreviveu 22.73% deles.

    Tinha bastante bebes, e 2/3 deles morreram o.O
'''
