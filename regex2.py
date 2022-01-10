#Metacharacters
import re

names_list=['Analisa Gómez',
            'María Martín',
            'Sandra López',
            'Santiago Martín']

text_search='^sa' #string or substring
for elem in names_list:
    if re.findall(text_search, elem, re.IGNORECASE): #See if text_search is at START(^) of elem. IGNORECASE ignore case (admits S or s...)
        print(re.findall(text_search, elem)) #list of text_search
        print(elem) #print the element

text_search='tín$' #string or substring
for elem in names_list:
    if re.findall(text_search, elem): #See if text_search is at END($) of elem
        #print(re.findall(text_search, elem))#list of text_search
        print(elem) #print the element

print('----------------------------')

##########APPLICATION: SEARCH DOMAIN N' PROTOCOLS IN LINKS, FOR PRINT LINKS##############

link_list=['https://domain.com',
            'ftp://domain.com',
            'https://domain.es',
            'ftp://domain.es']

link_search='^ftp' #string or substring
for link in link_list:
    if re.findall(link_search, link): #See if text_search is at START(^) of elem. Search the protocol
        print(link) #print the element

link_search='es$' #string or substring
for link in link_list:
    if re.findall(link_search, link): #See if text_search is at END($) of elem. Search the domain
        print(link) #print the element
print('----------------------------')

##########APPLICATION: SEARCH 'ñ' IN LINKS, FOR PRINT LINKS##############

link_list=['https://españa.com',
            'ftp://españa.com',
            'https://domain.es',
            'ftp://domain.es']

char_search='[ñ]' #string or substring
for link in link_list:
    if re.findall(char_search, link): #See if text_search is ANYWHERE([]) of elem. Search the protocol
        print(link) #print the element
print('----------------------------')

##########APPLICATION: SEARCH ONE OR ELSE CHAR IN ELEMENTS, FOR PRINT ELEMENTS##############

list=['hombres',
      'mujeres',
      'mascotas',
      'niños',
      'niñas']

chars_search='niñ[oa]s' #string or substring
for elem in list:
    if re.findall(chars_search, elem): #See if text_search is ANYWHERE([]) of elem. Search the protocol
        print(elem) #print the element
print('----------------------------')

##########APLICATION: SEARCH '´' OR NOT '´' IN ELEMENTS, FOR PRINT ELEMENTS##############

list=['hombres',
      'mujeres',
      'mascotas',
      'camión',
      'camion']

chars_search='cami[óo]n' #string or substring
for elem in list:
    if re.findall(chars_search, elem): #See if text_search is ANYWHERE([]) of elem. Search the protocol
        print(elem) #print the element