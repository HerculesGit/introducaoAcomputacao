
# Execoes






#infile = open("a/example.txt", 'r') # indica que o arquivo aberto será para leitura
                                    # temos r, w, a, r+
                                    # leitura, gravação, acréscimo, leitura e gravação
                                    # temos também o t e b que é modo texto ou arquivo binário


#r          Modo de leitura (padrão)
#w          Modo de gravação; se o arquivo já existir, seu conteúdo é apagado
#a          Modo de acréscimo; o conteúdo é acrescentado ao final do arquivo
#r+         Modo de leitura e gravação (fora do escopo deste livro)
#t          Modo de texto (padrão)
#b          Modo binário



#Problema pratico 4.7
def stringCount(nameArquivo, alvo):
    file = open(nameArquivo,'r')
    value  = file.read().count(alvo)
    file.close()
    return value

def palavras(nameFile):
    file = open(nameFile,'r')
    lst = file.read()
    
    words = lst.replace('.','')
    words = words.replace(',','')
    words = words.replace(';','')
    words = words.replace(':','')
    words = words.replace('?','')
    words = words.replace('!','')
    file.close()
    return words.split()    

def lineforline(nameFile):
    file = open(nameFile,'r')
    for i in file:
        print(i, end='')
    file.close()
def meuGrep(nameFile,alvo):
    file = open(nameFile,'r')
    for line in file:
        if alvo in line:
            print(line, end='')

    
    file.close()
import time
def openLog(fileName, modo):
    file = open(fileName, modo)
    
    fileLog = open("log.txt", "a")

    now = time.localtime() 
    nowFormat = time.strftime('%A %b/%d/%y %I:%M %p',now)
    
    fileLog.write('Arquivo {} aberto em {} \n'.format(fileName,nowFormat))
    fileLog.close()

    return file

def fribonacci(limite):
    anterior = 1
    atual = 1

    while atual <=limite:
        anterior, atual = atual, anterior+atual
    return atual

    

