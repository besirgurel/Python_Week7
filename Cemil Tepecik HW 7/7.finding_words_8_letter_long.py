#=====================FINDING 8 LETTER WORDS WITHIN AN TEXT============================================0
"""Find words that are 6,7,8 letter long on this text ;
Without, the night was cold and wet, but in the small parlour of Laburnum villa the blinds were drawn and the fire burned brightly. Father and son were at chess; the former, who possessed ideas about the game involving radical chances, putting his king into such sharp and unnecessary perils that it even provoked comment from the white-haired old lady knitting placidly by the fire. "Hark at the wind," said Mr. White, "who, having seen a fatal mistake after it was too late, was amiably desirous of preventing his son from seeing it. I'm listening," said the latter grimly surveying the board as he stretched out his hand. "Check." I should hardly think that he's come tonight," said his father, with his hand poised over the board. "Mate," replied the son. "That's the worst of living so far out," balled Mr. White with sudden and unlooked-for violence; "Of all the beastly, slushy, out of the way places to live in, this is the worst. Path's a bog, and the road's a torrent. I don't know what people are thinking about. I suppose because only two houses in the road are let, they think it doesn't matter."""
#=====================================PROGRAM====================================================
import re
def write_file(text_raw):
    with open("dosya.txt", "a", encoding="utf-8") as file:  #start a text file named dosya
        file.write(text_raw+'\n') #record the results

def read_file():
    with open("dosya.txt", "r", encoding="utf-8") as file:

        cumle=file.read()
        patern = r"\s\w{8}\s" # for 8 letter words
        researched_code = re.findall(patern, cumle)
        patern1 = r"\s\w{7}\s" # for 7 letter words
        researched_code1 = re.findall(patern1, cumle)
        patern2 = r"\s\w{6}\s" # for 6 letter words
        researched_code2 = re.findall(patern2, cumle)
        choise=int(input('enter the lenght of word you wanted to search'))
        if choise==8:# for 8 letter words
            if researched_code:
                for i in researched_code:
                    write_file(i)
                return print(researched_code)
            else:
                return print('No 8 letter word')
        elif choise == 7: # for 7 letter words
            if researched_code1:
                for i in researched_code1:
                    write_file(i)
                return print(researched_code1)
            else:
                return print('No 7 letter word')
        elif choise == 6: # for 6 letter words
            if researched_code2:
                for i in researched_code2:
                    write_file(i)
                return print(researched_code2)
            else:
                return print('No 6 letter word')
#--------------------------------main-------------------------------------------------
text_raw=input('Enter the text>>>')
write_file(text_raw)
read_file()
#==========================================END=========================================
#OUTPUT:
# [' Laburnum ', ' provoked ', ' knitting ', ' desirous ', ' thinking ']