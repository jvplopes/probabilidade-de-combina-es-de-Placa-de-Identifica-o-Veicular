from itertools import product


letras = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S', 'T', 'U', 'V', 'X', 'Y', 'Z']

numeros = [0,1,2,3,4,5,6,7,8,9]

l_placa = []
para_analise = []
analisadas = []

def analise_numeros(placa):
    placas = []
    for caracter in placa:
        if caracter == "*":
            index = placa.index(caracter)
            l_caracteres = l_placa[index]
            
            if l_caracteres == ['*']:
                l_caracteres = numeros
            else:
                pass
            genComb = product(l_caracteres,
                              repeat=1)  
            for subset in genComb:
                lista = list(placa)
                lista[index] = subset[0]
                plate = ''.join(str(e) for e in lista)

                if plate in placas:
                    pass
                else:
                    placas.append(plate)
                    

    
    return placas

def analise_letras(placa):
    placas = []
    for letra in placa:
        if letra == "*":
            index = placa.index(letra)
            l_caracteres = l_placa[index]
            
            if l_caracteres == ['*']:
                l_caracteres = letras
            else:
                pass
            genComb = product(l_caracteres,
                              repeat=1) 
            for subset in genComb:
                lista = list(placa)
                lista[index] = subset[0]
                plate = ''.join(str(e) for e in lista)

                if plate in placas:
                    pass
                else:
                    placas.append(plate)
                    


    
    return placas

def init():
    n1 = input('Digite a primeira letra: ')
    l_placa.append(list(n1))
    
    n2 = input('Digite a segunda letra: ')
    l_placa.append(list(n2))
    
    n3 = input('Digite a terceira letra: ')
    l_placa.append(list(n3))
    
    n4 = input('Digite o primeiro número: ')
    l_placa.append(list(n4))
    
    n5 = input('Digite o segundo número ou letra: ')
    l_placa.append(list(n5))
    
    n6 = input('Digite o terceiro número: ')
    l_placa.append(list(n6))
    
    n7 = input('Digite o quarto número: ')
    l_placa.append(list(n7))
 

init()

def placa(l_placa):
    plate = ''
    for l in l_placa:
        
        if len(l) != 1:
            plate = plate + '*'
        else:
            plate = plate + ''.join(l)

    print('PLACA: ' + plate)
    return plate

placa = placa(l_placa)

para_analise.append(placa)

while para_analise != []:

    for placa in para_analise:
        for caracter in placa:
            if caracter == "*":
                index = placa.index(caracter)

                if caracter.isnumeric() == False:
                    resultados = analise_letras(placa)
                else:
                    resultados = analise_numeros(placa)

        for resultado in resultados:
            
            if '*' in resultado:
                para_analise.append(resultado)
            else:
                analisadas.append(resultado)
        para_analise.remove(placa)



print('Foram encontrados ' + str(len(analisadas)) + ' resultados: ')
for a in analisadas:
    print(a)

input('Pressione qualquer botão para fechar.')






