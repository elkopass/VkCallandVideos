
from doctest import master
from re import T


def ToMas():
    mas = []
    file = open("query.txt", "r")
    s  = file.read()
    file.close()
    s = s.split('\n')
    for i in range(len(s)):
        s[i] = s[i].split(" ")
    return s

def ToQuery(massiv):
    s = ""
    for i in massiv:
        for k in i:
            s += k + " "
        s = s[:-1]
        s += '\n'
    s = s[:-1]

    file = open("query.txt", "w")
    file.write(s)
    file.close()

def Beg(id, link, isFree):

    massiv = ToMas()
    massiv.append([id, link, isFree])
    ToQuery(massiv)

def Free(id):
    massiv = ToMas()
    flag = 0

    for i in range(len(massiv)):
        if massiv[i][0] == id:
            flag = 1
            massiv[i][2] = "1"
    ToQuery(massiv)
    if flag == 0:
        print("вы не начали звонок")
            
def Call():
    massiv = ToMas()
    flag = 0

    for i in range(len(massiv)):
        if massiv[i][2] == "1":
            flag = 1
            massiv[i][2] = "0"
            ToQuery(massiv)
            return
    
    if flag == 0:
        print("очередь занята")

