"""Write a program that list according to email addresses without email domains in a text.
Input:
The advencements in biomarine studies franky@google.com with the investments necessary and 
Davos sinatra123@yahoo.com. Then New Yorker article on wind farms...

Output :
franky
sinatra123"""

import re

input = "The advencements in biomarine studies franky@google.com with the investments necessary \
         and Davos sinatra123@yahoo.com. Then New Yorker article on wind farms..."

regex="[A-Z0-9a-z]+@[A-Za-z0-9]+\.com"

obj_list= re.findall(regex, input)

for i in obj_list:
    split= i.split("@")
    print(split[0])
