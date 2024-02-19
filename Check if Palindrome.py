import re

def checkifpalindrome():
    word = input('Please type in the word or phrase you want to test, to see if it is a palindrome (punctuation and spaces excluded): ')
    result = re.sub(r'[^\w]', '', word)
    if result.lower() == result.lower()[::-1]:
        print(f'{word} is a palindrone')
    else:
        print(f'{word} is not a palindrone')

checkifpalindrome()
