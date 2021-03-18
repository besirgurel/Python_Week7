'''Developer: Furkan Sürücü
Purpose of Software: Reinforcement of learned python code and self-improvement
What does program do?: Write a program that detects the ID number hidden in a text. We know that the format of the ID number is 2 letters, 1 digit, 2 letters, 2 digits, 1 letter, 1 digit (For example: AA4ZA11B1).

Input : AABZA1111AEGTV5YH678MK4FM53B6

Output : MK4FM53B6

Input : AEGTV5VZ4PF94B6YH678

Output : VZ4PF94B6
'''

import re
def id_detection():
    hidden_id = input("Enter your ID number hidden in a text:\n ")
    patern = '\w\w\d\w\w\d\d\w\d'
    find = re.search(patern,hidden_id)
    print(find.group())
id_detection()
