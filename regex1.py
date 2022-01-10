#go to web python howto regex
#regex are a programming mini-language
#Methods: findall(), serach(), match(), finditer()...
import re

string='Vamos a aprender expresiones regulares'

print(re.search('aprender',string)) #return object _sre.SRE_Match if find the substring
print(re.search('aprenderrrr',string)) #returns None

text_search='Vamos'
if re.search(text_search,string) is not None:
    print('El texto {} SÍ está en la cadena'.format(text_search))
else:
    print('El texto {} NO está en la cadena'.format(text_search))

text_search2="expresiones"
object_find=re.search(text_search2,string)
print(object_find.start()) #initial position of find
print(object_find.end()) #end position of find
print(object_find.span()) #tuple position of find


string3='Vamos a aprender expresiones regulares en Python. Python es un lenguaje de sintaxis sencilla'
text_search3='Python'
fa=re.findall(text_search3,string3) #retuns matches list
print(len(fa)) #print count matches
print(len(re.findall(' ',string3))) #print count of spaces


