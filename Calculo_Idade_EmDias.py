#Importado previamente
from datetime import date
hoje = date.today()

# Listar todos os cadastros com idade em dias
# Lista com informações
nomes = ['Gabriela Silva', 'Ana Souza', 'João Antunes']
cpfs = [24434377523, 33292296161, 22755218100]
nascimentos = ["16/01/1938", "16/01/2023", "18/12/1989"]
idade_dias = []

print("---- Listar todos os cadastros ----")
print("---- Adicionando idade em dias ----")

#  Percorre a lista, localizando cada data armazenada
for i in nascimentos:
  idadeDias = 0 #variavel criada 
  
  for ano in range(int(i[6:]), hoje.year): # percorre os anos dentro da data até o ano atual
    if (ano%4 == 0 and ano%100 != 0) or ano%400 == 0: #verifica se é bissexto
      idadeDias += 366 
    else:
      idadeDias += 365
    
  # soma dias ate o dia de hoje
  idadeDias += hoje.day
  
  for mes in range(1, hoje.month): #percorre os meses para descobrir quantidade de dias
    #avaliar se mes possui 30 ou 31 dias
    if mes == 4 or mes == 6 or mes == 9 or mes == 11:
     idadeDias += 30
    elif mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
      idadeDias +=  31
    elif mes ==2:
      if (hoje.year%4 == 0 and hoje.year%100 != 0) or hoje.year%400 == 0: #caso ano seja bissexto
        idadeDias += 29
      else: #caso ano não seja bissexto
        idadeDias +=28
  
  # subtrai dias 
  idadeDias -= int(i[:2])
  
  for mes in range(1, int(i[3:5])): #percorre os meses até o mes atual
      if mes == 4 or mes == 6 or mes == 9 or mes == 11:
        idadeDias -= 30
      elif mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
          idadeDias -= 31
      elif mes ==2:
        if (hoje.year%4 == 0 and hoje.year%100 != 0) or hoje.year%400 == 0:
          idadeDias -= 29
        else:
          idadeDias -=28

  idade_dias.append(idadeDias) # adiciona idade em dias a lista
print("-="*30)

#Percorre a lista, imprimindo separadamente cada cadastro
for n in range(len(nomes)):
    print(f"{n+1}","Nome:",nomes[n],"CPF:",cpfs[n],"Data:",nascimentos[n],"Idade:",idade_dias[n],"dias")

