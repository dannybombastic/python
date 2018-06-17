import re

# *con y sin +all menos un {}numero de o rango de rep  | patrones =['h[ae]*la'] 
# patrones =["ho{0,1}","ho{1,2}","ho{0,10}"]
def buscar(patrones,texto):
    
    for patrone in patrones:
       print( re.findall(patrone,texto) )

texto = "haaala hiiila hula hooooola heeela"
# patrones =['h[ae]*la','h[ou]{0,9}la','h[^ae]*la']
# buscar(patrones,texto)
patrones =['h[a-z]la','h[0-9]la','[A-z]{5}']


texto = "holA m0la zZola h0la hola"
buscar(patrones,texto)