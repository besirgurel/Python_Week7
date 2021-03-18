"""Write a program that detects the ID number hidden in a text. 
We know that the format of the ID number is 2 letters, 1 digit, 2 letters, 2 digits, 1 letter, 1 digit 
(For example: AA4ZA11B1).

Input : AABZA1111AEGTV5YH678MK4FM53B6
Output : MK4FM53B6
Input : AEGTV5VZ4PF94B6YH678
Output : VZ4PF94B6
"""

import re
input_data = 'AABZA1111AEGTV5YH678MK4FM53B6'
regex= '[A-Za-z][A-Za-z][0-9][A-Za-z][A-Za-z][0-9][0-9][A-Za-z][0-9]'


match = re.search(regex, input_data)
print(match.group())

input_data='AEGTV5VZ4PF94B6YH678'
match = re.search(regex, input_data)
print(match.group())