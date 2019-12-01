import sys

text = str(sys.argv[1: ])

def count_words(text):
    summary = {}
    text2 = text.split()
    for words in text2:
        if words in summary:
            summary[words] += 1
        else:
            summary[words] = 1
    return summary

if __name__ == '__main__':
    print(f'''lista:{count_words(text)}''')
