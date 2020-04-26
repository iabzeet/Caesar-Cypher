"""
    A Caesar cypher is a weak form of encryption that involves “rotating” each letter by a
    fixed number of places. To rotate a letter means to shift it through the alphabet, wrap‐
    ping around to the beginning if necessary, so ‘A’ rotated by 3 is ‘D’ and ‘Z’ rotated by 1
    is ‘A’.
    To rotate a word, rotate each letter by the same amount. For example, “cheer” rotated
    by 7 is “jolly” and “melon” rotated by -10 is “cubed”. In the movie 2001: A Space Odys‐
    sey, the ship computer is called HAL, which is IBM rotated by -1

    A Caesar Cypher program, from a book Think Pyhon.
    26-04-2020
"""


def rotate_letter(letter, num):             #primary function, takes two parameters- each letter from another function(one-by-one) and an integer of how much rotation should be added in a given string(vvalue of string)
    if letter.isupper():                    #checks whether a letter is uppercase and gets its ord(uppercase) value
        start = ord('A')                    
    elif letter.islower():                  #checks whether a letter is lowercase and gets its ord(lowercase) value
        start = ord('a')
    else:
        return letter                       

    c = ord(letter) - start                 #gets the postion of a letter from a starting letter of an alphabet, how far an object is from a starting alphabet
    i = (c+num)%26 + start                  #adds value(positional) of a letter with the ineger value of how much it needs to rotate, all within a limit of 26, letters of total alphabet, then adds it's calculated value into start to get rotated letter(integer)
    return chr(i)                           #returns a letter form of every integer from 'i' throughout the whole word

def rotate_word(word, num):                 #main function, takes two parameters- word and integer value of how much it should rotate
    res = ''                                #empty string to fill it gradually from the strings obtained in another function
    for letter in word:                     #traversing every letter in a word
        res += rotate_letter(letter, num)   #obtaining each string gradually from another function, gradually
    return res                              #returning value(interchanged) of res

if __name__ == '__main__':                  #test conditions
    print(rotate_word('cheer', 7))
    print(rotate_word('melon', -10))
    print(rotate_word('sleep', 9))