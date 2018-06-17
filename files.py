from io import open




texto = "una linea de texto en un archivo\n otra linea de texto\ny otra mas que no contaban"
file = open('archivo_num1.txt','w')
file.write(texto)
file.close()


fichero = open('archivo_num1.txt','r')

text = fichero.read()
fichero.close()
print( text )


fichero = open('archivo_num1.txt','r')
lineas = fichero.readlines()
fichero.close()
print( lineas )


fichero = open('archivo_num1.txt','a')

fichero.write( "\n estamos locos o que?" )
fichero.close()

fichero = open('archivo_num1.txt','r')
l = fichero.readline()
fichero.readline()
fichero.close()

with open('archivo_num1.txt','r') as fichero:
    for linea in fichero:
        print( linea )
fichero.close()



fichero = open('archivo_num1.txt','r')

fichero.seek(10) # caracter 10

print( fichero.read() ) #puntero al final

fichero.seek(0) # puntero al principio 10
fichero.read(5) # numero dce caracteres a leer

texto  = fichero.read

fichero.seek( len(text)/2 ) # a la mitad del contenido
fichero.read()
fichero.seek(0)
fichero.seek( len( fichero.readline() ) )


fichero = open('archivo_num1.txt','r+') # lectura y ecritura
fichero.close()


    
fichero = open('archivo_num1.txt','r+') # lectura y ecritura
lineas = fichero.readlines()
lineas[2] = "esta linea se ha modificado en memoria\n"
fichero.seek(0)
fichero.writelines(lineas)
fichero.close()


