t = int(input())

lst = []

for _ in range(t):
    age, name = input().split()
    age = int(age)
    lst.append([age, name])

lst.sort(key = lambda x : x[0])

for i in lst:
    print(i[0], i[1])