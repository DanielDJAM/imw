import sys

chain_num = sys.argv[1:]
count_num = 0
count_chain = 0

for value1 in chain_num:
    count_num += 1
    count_chain = float(value1) + count_chain
final = count_chain / count_num
print(f'La media de los valores es:{final}')
