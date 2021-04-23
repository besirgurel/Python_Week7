import re
with open('text.txt','r',encoding="utf-8") as file:
    text=file.read()
    patern=r"[a-z|A-Z|0-9]+[@]"
    lst=re.findall(patern,text)
    new_lst=[]
    for i in range(len(lst)):
        new_lst.append(lst[i][:-1])
        print(new_lst[i])