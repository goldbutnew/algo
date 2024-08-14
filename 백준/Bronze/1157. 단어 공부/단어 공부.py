words = input().upper()
word_lst = list(set(words))

cnt_lst = []

for word in word_lst:
    cnt = words.count(word)
    cnt_lst.append(cnt)

if cnt_lst.count(max(cnt_lst)) > 1:
    print("?")
else:
    idx = cnt_lst.index(max(cnt_lst))
    print(word_lst[idx])