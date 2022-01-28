

Contenido del fichero mapper.py

#!/usr/bin/env python
# las operaciones de map  tienen como entrada un fichero que es un conjunto de lineas
# Las lineas estan separadas por retorno de carror

import sys             #importamos libreria de python

#  por cada linea ejecutamos esta operacion
#  la entrada es el fichero estandar
for linea in sys.stdin:

    linea = linea.strip()# dividimos la entrada en lineas por el retorno de carro o \n ya que puede tener la entrada varios ficheros
    keys = linea.split() # dividimos cada linea por palabra o tokens por el espacio en blanco

    for key in keys:     # por cada token generamos un par (palabra, 1) o (key , value) 
        value = 1
        
        print('{0}\t{1}'.format(key , value) ) 



Contenido del fichero reducer.py

#!/usr/bin/env python

import sys

last_key      = None              
running_total = 0

for input_line in sys.stdin:
    input_line = input_line.strip()

    this_key, value = input_line.split("\t", 1)  
    value = int(value)           

    if last_key == this_key:
        running_total += value

    else:
        if last_key :
            print( "{0}\t{1}".format(last_key, running_total) )
        running_total = value
        last_key = this_key

if last_key == this_key:
    print( "{0}\t{1}".format(last_key, running_total))




lanzar una tarea 
cat pg2000.txt 
lanzar la tarea de 
cat pg2000.txt | ./mapper.py
lanzar la tarea de 
cat pg2000.txt | ./mapper.py > output.txt
lanzar la tarea de 
cat pg2000.txt | ./mapper.py > output.txt
lanzar la tarea de 
less output.txt
lanzar la tarea de 
cat pg2000.txt | ./mapper.py  | sort > output.txt
lanzar la tarea de 
cat pg2000.txt | ./mapper.py  | sort | reducer.py > output.txt
lanzar la tarea de 
less output.txt


lanzar una tarea en mapReduce en el cluster

hadoop jar /opt/cloudera/parcels/CDH-*/lib/hadoop-mapreduce/hadoop-streaming.jar    -input ./practicaMapReduce/input    -output ./practicaMapReduce/output    -mapper /home/alumno0/mapper.py  -reducer ./reduce.py  -file mapper.py -file reduce.py


hacer un histograma de palabras
cutoff de 100
eliminar caracterers que no sean letras 
stopwords
sinonimos
hacer ngramas de 2 palabras
ordenar por value

