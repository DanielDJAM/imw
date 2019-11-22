import sys

chain_num = [sys.argv[1:]]
count_num = 0
count_chain = 0
chain2 = []

chain = chain_num.split()
for i in range(1, len(chain), 2):

    for k in range(0, len(chain), 2):
        j = i - k


print(j)
