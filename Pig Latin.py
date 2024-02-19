#Pig Latin
#Pig Latin is a game of alterations played on the English language game.
#To create the Pig Latin form of an English word the initial consonant sound is transposed to the end of the word and an ay is affixed
#(Ex.: "banana" would yield anana-bay). Read Wikipedia for more information on rules.


#take lone consonant or consonant cluster at begining of word and move to end followed by 'ay'
#if word begins with vowels jsut add hay, way, yay or nay to the end

list_of_vowels = ['a','e','i','o','u']


def pig_latin():
    snt = input("Please type the sentence you'd like to convert to pig latin: ").split()
    new_sentence = []
    print(snt)
    for word in snt:
        conscount = 0
        for char in word:
            if char not in list_of_vowels:
                print(char)
                conscount += 1
            elif char in list_of_vowels and conscount != 0:
                new_sentence.append(word[conscount:] + word[0:conscount] +'ay')
                print(word[conscount:])
                break
            elif char in list_of_vowels and conscount == 0:
                new_sentence.append(word + 'way')
                break
    print(' '.join(new_sentence))

pig_latin()