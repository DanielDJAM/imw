import random

NUCLEOBASES = 'ATGC'
DNA_SIZE = 100

sequence = ''.join([random.choice(NUCLEOBASES) for i in range(DNA_SIZE)])

count_A = 0
count_T = 0
count_C = 0
count_G = 0

for char in sequence:
    if 'A' in char:
        count_A += 1
    elif 'T' in char:
        count_T += 1
    elif 'C' in char:
        count_C += 1
    elif 'G' in char:
        count_G += 1

print(f'''
        Adenine:{count_A}
        Thymine:{count_T}
        Cytosine:{count_C}
        Guanine:{count_G}''')
