#============================== detects the ID number hidden in a text===============0
"""
Write a program that detects the ID number hidden in a text. We know that the format of the ID number is
2 letters, 1 digit, 2 letters, 2 digits, 1 letter, 1 digit (For example: AA4ZA11B1).
Input : AABZA1111AEGTV5YH678MK4FM53B6
Output : MK4FM53B6
Input : AEGTV5VZ4PF94B6YH678
Output : VZ4PF94B6
"""
#===========================PROGRAM================================
import re
def write_file(text_raw):
    with open("dosya.txt", "a", encoding="utf-8") as file:
        file.write("\nInput :"+text_raw)
    with open("dosya.txt", "r", encoding="utf-8") as file:
        cumle=file.read()
        patern = r"\w{2}\d{1}\w{2}\d\d\w\d"
        researched_code = re.search(patern, cumle)
    with open("dosya.txt", "a", encoding="utf-8") as file:
        file.write("\nOutput :" + researched_code.group())
#-------------------------main-------------------------------------------
text_raw=input('Enter the text>>>')
print(write_file(text_raw))
#==========================================END=========================================

