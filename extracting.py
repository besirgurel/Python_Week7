'''Developer: Furkan Sürücü
Purpose of Software: Reinforcement of learned python code and self-improvement
What does program do?: Write a program that list according to email addresses without email domains in a text.
Example:
Input:
The advencements in biomarine studies franky@google.com with the investments necessary and Davos sinatra123@yahoo.com. Then New Yorker article on wind farms...
Output :
franky
sinatra123'''
import re

txt = "The advencements in biomarine studies franky@google.com with the investments" \
      "necessary and Davos sinatra123@yahoo.com. Then New Yorker article on wind farms"
patern = "[a-z|A-Z|0-9]+[@]"
find = re.findall(patern,txt)

for i in find:
    print(i[:-1])