# [LP-A02] Escreva um programa em python que pergunte ao usuário a velocidade de um carro.
#Caso ultrapasse 80 km/h, exiba uma mensagem dizendo que o usuário foi multado e o valor da multa,
#cobrando R$20,00 por cada km que exceder 80 km/h.

velocidade = float(input("Por favor, informe a velocidade do carro!: "))
multa = (velocidade - 80) * 20
if velocidade > 80:
    print("Velocidade excedida! Você foi multado. O valor da multa será: R$",format(multa))
else:
    print("Velocidade não excedida!")