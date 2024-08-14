find_lst = []

for _ in range(9):
    i = int(input())
    find_lst.append(i)

max_num = max(find_lst)
idx = find_lst.index(max_num)

print(max_num)
print(idx+1)