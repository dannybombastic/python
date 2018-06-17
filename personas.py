from io import open

fichero = open('personas.txt','r')
lineas = fichero.readlines()
fichero.close()
personas = []

for linea in lineas:
    linea.replace('\n','')
    campos = linea.split(";")
    persona = {"id":campos[0],"name":campos[1],"birthday":campos[-1].replace('\n',''),"surname":campos[2]}
    personas.append(persona)


for p in personas:
    
     print("(id = {}) : {}  {} :  {}".format(p['id'],p['name'],p['surname'],p['birthday']))



