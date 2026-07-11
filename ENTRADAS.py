#ENTRADAS = INPUT , PRINT = APARECER NA TELA
nome_cliente = input ("Insira o seu nome: ")
print(nome_cliente)
idade_cliente = int(input ("Insira sua idade: "))
print(idade_cliente)
cidade_cliente = input ("Qual a sua cidade ?")
print(cidade_cliente)
print(f"O nome do cliente é {nome_cliente}.\n Ele possui {idade_cliente} anos . \nEle mora na cidade {cidade_cliente}")
idade_futura = 1 + idade_cliente
print(idade_futura)
print(f"a idade do cliente futura sera {idade_futura}")

idade_anopassado = idade_cliente - 1
print(f"ele tinha {idade_anopassado} anos ")

salario = float(input("Digite o seu salario"))
salario_com_décimo = salario * 2
print(salario_com_décimo)


pizza = int(input ("Qual valor da pizza ? "))
Cupom = int(input ("qual valor do cupom? "))
