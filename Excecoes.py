
strIdade = input("Digite sua idade: ")

try:
    intIdade = int(strIdade)
    print("Você tem {} idade".format(intIdade))
except ValueError:
    print("Era pra ter digitado em decimal, animal!")
    
