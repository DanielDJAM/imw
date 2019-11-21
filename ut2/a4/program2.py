import random

NUCLEOBASES = 'ATGC'
DNA_SIZE = 100

sequence = ''.join([random.choice(NUCLEOBASES) for i in range(DNA_SIZE)])

count_a = 0
count_t = 0
count_c = 0
count_g = 0

for char in sequence:
    if 'A' in char:
        count_a += 1
    elif 'T' in char:
        count_t += 1
    elif 'C' in char:
        count_c += 1
    elif 'G' in char:
        count_g += 1

print(f'''
        Adenine:{count_a}
        Thymine:{count_t}
        Cytosine:{count_c}
        Guanine:{count_g}''')
