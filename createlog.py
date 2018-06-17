import sys
from io import open
from pathlib import Path
import datetime
import os

i = 1
list = sys.argv
dt = datetime.datetime.now()
if len( list ) < 2:
    print("Es necesario dos parametros ej. ( FileNmae.extension, Message )") 
else:
    filename = list[1]
    line = list[2:]
    if os.path.isfile( filename ) :

              
                  
                  
                   fichero = open(filename,'r+')
                   lines = fichero.readlines()
                
                   if len( lines ) > 0:
                         if len( lines[0] ) > 0:
                            vect = lines[-1].split( ":" )
                            print(vect[0])
                            print(len(lines[0]))
                            i = (int( vect[0] )+1)
                            lines.append( "{}: [{}] : {} , {}\n".format( i,(dt.hour,":",dt.minute,":",dt.second),filename,line ) )
                          
                   else:  
                            lines.append( "{}: [{}] : {} , {}\n".format(i,(dt.hour,":",dt.minute,":",dt.second),filename,line ) )
                 
                   fichero.seek(0)
                   fichero.writelines(lines)
                   fichero.close()   
    else:
        
         fichero = open(filename,'a')
         fichero.write( "{}: [{}] : {} , {}\n".format( i,(dt.hour,":",dt.minute,":",dt.second),filename,line ) )    
         fichero.close()   
                           
              
        
                   
                 
                      
    
    
                      
            
   