#Faça um Programa que pergunte em que turno você estuda.
#Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
print("Em que turno você estuda? ")
pergunta = input("Digite M para matutino, V para Vespertino ou N para Noturno")
#Criando a menssagem que será exibida;
if (pergunta in 'M'):
    print("Bom Dia!")
elif (pergunta in 'V'):
    print("Boa Tarde!")
elif (pergunta in 'N'):
    print("Boa Noite!")
else:
    print("Valor Inválido!")
