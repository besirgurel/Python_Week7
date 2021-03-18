#==================E MAIL DOMAINS IN A TEXT=========================================
"""Write a program that list according to email addresses without email domains in a text.
Example:
Input:
The advencements in biomarine studies franky@google.com with the investments necessary and Davos sinatra123@yahoo.com. Then New Yorker article on wind farms...
Output :
franky
sinatra123
"""
#=====================================PROGRAM====================================================
import re
with open('metin.txt','r',encoding="utf-8") as file:
    text=file.read()
    patern=r"[a-z|A-Z|0-9]+[@]"
    liste=re.findall(patern,text)  #findall liste seklinde yazar
    new_lst=[]
    for i in range(len(liste)):
        new_lst.append(liste[i][:-1])  #[:-1] @ ifadesini atmak için
        print(new_lst[i])
#=======================================END===========================================================
#OUTPUT:
#franky
#sinatra123