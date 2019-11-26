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
    half = len(text) // 2
    text2 = text[0:half] + ' | ' + text[half:]
    return text2

def upper_vowels(text):
    text2 = ""
    for char in text:
        if char in 'aeiou':
            char = char.upper()
        text2 += char
    return text2

def sorted_by_words(text):
    text2 = text.split()
    text2.sort()
    text = ' '.join(text2)
    return text

def length_of_words(text):
    text3 = ''
    text2 = text.split()
    for i in text2:
        text3 += (str(len(i)) + ' ')
    return text3

if __name__ == '__main__':
    text = sys.argv[1]
    print(f'''
    Number of vowels:{num_vowels(text)}
    Number of whitespaces:{num_whitespaces(text)}
    Number of digits:{num_digits(text)}
    Number of words:{num_words(text)}
    Reverse of text:{reverse(text)}
    Length of text:{length(text)}
    Halfs of text:{halfs(text)}
    Text with uppercased vowels:{upper_vowels(text)}
    Sorted by words:{sorted_by_words(text)}
    Length of words:{length_of_words(text)}''')
