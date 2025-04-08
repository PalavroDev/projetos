# o re serve para criar padroes em strings e validar as mesma
# fullmatch serve para procurar se ha strings satisfazendo exatamente igual o padrao
# serach procura a string em algum parte do codigo e retorna apenas a primeira (findall acha todos)
# declarando var = re.compile("padrao desejado")
# o . representa qualquer caracter menos \n (newline)
# o ponto final é \.
# [] um conjunto de possibilidades, pode se colocar mais de uma das função abaixo para ser retornada
# ^ inicio da string
# $ final da string
# [^] é diferente de um caracter
# \w representa alfanumericos
# \W nao e alfanumerico
# \s caracter vazio
# \S caracter nao vazio
# \d numeros de 0 a 9
# \D nao numeros de 0 a 9
# + 1 ou mais vezes o padrao e atendido / é analisado caracter individualmente
# * 0 ou mais vezes o padrao e atendido
# ? 0 ou 1 vez
# {x} x vezes o padrao se repete
# {x,y} x minimo de vezes que aparece, y max de vezes

import re


email = input('Email:')
padrao = re.compile('[\w]+@[\w]+\.com[\.a-zA-Z]{0,4}')
y = re.match(padrao, email)
print(y)
