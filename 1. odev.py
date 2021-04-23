import re
t="AEGTV5VZ4PF94B6YH678 AABZA1111AEGTV5YH678MK4FM53B6"
x=re.findall("[(A-Z)|(a-z)]{2}\d[(A-Z)|(a-z)]{2}\d{2}[(A-Z)|(a-z)]\d",t)
print("".join(x))