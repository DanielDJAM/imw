import sys

def num_vowels(text):
    num_vowels = 0
    for char in text.lower():
        if char in 'aeiou':
            num_vowels += 1
    return num_vowels

def num_whitespaces(text):
    num_whitespaces = 0
    for space in text:
        if space in ' ':
            num_whitespaces += 1
    return num_whitespaces

def num_digits(text):
        num_digits = 0
        for number in text:
            if number in '0123456789':
                num_digits += 1
        return num_digits

def num_words(text):
    num_words = len(text.split())
    return num_words

def reverse(text):
    reverse = text[::-1]
    return reverse

def length(text):
    length = len(text)
    return length

def halfs(text):
    length = len(text)
    length2 = length / 2
    phrase = text.split(length, 1)
    halfs = phrase[length2] = ' | '
    return halfs

if __name__ == '__main__':
    text = sys.argv[1]
    print(f'''
    Number of vowels:{num_vowels(text)}
    Number of whitespaces:{num_whitespaces(text)}
    Number of digits:{num_digits(text)}
    Number of words:{num_words(text)}
    Reverse of text:{reverse(text)}
    Length of text:{length(text)}
    Halfs of text:{halfs(text)}''')
