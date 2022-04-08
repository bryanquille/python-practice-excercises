# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 17:02:29 2022

@author: Bryan
"""

def counting_vowels(word):
    
    vac, vec, vic, voc, vuc = 0, 0, 0, 0, 0
    for i in word:
        if i == 'a' or i == 'A':
            vac += 1
        elif i == 'e' or i == 'E':
            vec += 1
        elif i == 'i' or i == 'I':
            vic += 1
        elif i == 'o' or i == 'O':
            voc += 1
        elif i == 'u' or i == 'U':
            vuc += 1
     
    print(f'The word {word} has {vac} vowels a.')
    print(f'The word {word} has {vec} vowels e.')
    print(f'The word {word} has {vic} vowels i.')
    print(f'The word {word} has {voc} vowels o.')
    print(f'The word {word} has {vuc} vowels u.')
    return vac, vec, vic, voc, vuc

if __name__ == '__main__':
    word = input("Enter a word: ")
    counting_vowels(word)
        