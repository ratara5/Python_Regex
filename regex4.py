#MATCH (in start) AND SEARCH (anywhere)
from osgeo import gdal
from osgeo import gdalnumeric
from osgeo import osr

osr.SpatialReference().ImportFromProj4('+init=epsg:3857')

import re

name1='Sandra López'
name2='Antonio Gómez'
name3='María López'
name4='sandra López'
name5='Jara López'
name6='Lara López'

first_name='Sandra'

#match: find match at start of string
if re.match(first_name,name1,re.IGNORECASE): #pass case
    print('SÍ hemos encontrado el nombre {}'.format(first_name))
else:
    print('NO hemos encontrado el nombre {}'.format(first_name))
print('----------------------------')

#match con metacharacter '.'
first_name2='.ara'
if re.match(first_name2,name5,re.IGNORECASE): #pass case
    print('SÍ hemos encontrado el nombre que contiene {}'.format(first_name2))
else:
    print('NO hemos encontrado el nombre que contiene {}'.format(first_name2))

if re.match(first_name2,name6,re.IGNORECASE): #pass case
    print('SÍ hemos encontrado el nombre que contiene {}'.format(first_name2))
else:
    print('NO hemos encontrado el nombre que contiene {}'.format(first_name2))
print('----------------------------')

#match with metacharacter '\d'
string1='Jara López'
string2='5465456265454'
string3='A543215465'

substring='\d' #start with number
if re.match(substring,string2):
    print('SÍ inicia con número')
else:
    print('NO inicia con número')
print('----------------------------')

#search 
name1='Jara López'
name2='Antonio Gómez'
name3='Lara López'

last_name='López'

if re.search(last_name,name3,re.IGNORECASE): #pass case. Change SECOND parameter
    print('La persona SÍ tiene el apellido {} '.format(last_name))
else:
    print('La persona NO tiene el apellido {} '.format(last_name))
print('----------------------------')

#searh with codes
code1='joiiohnfaiopiuounoij9ye71jijiojoij'
code2='dafdafdsadsf71adsfsdasdadsf'
code3='kjkljlijopijaf65gaiuoiu'

frag_code='71'

if re.search(frag_code,code2): #Change SECOND parameter
    print('El fragmento {} SÍ está en el código'.format(frag_code))
else:
    print('El fragmento {} NO está en el código'.format(frag_code))
print('----------------------------')