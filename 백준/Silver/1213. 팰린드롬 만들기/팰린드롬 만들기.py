eng_name = input()

# { char: cnt } 형태로 딕셔너리 생성
dic = {}
for char in eng_name:
    dic[char] = dic.get(char, 0) + 1

# 팰린드롬 판별
t = 0
for num in dic.values():
    if num % 2 == 1:
        t += 1
if t > 1:
    print("I'm Sorry Hansoo")
else:
    # 팰린드롬 만들기
    ans = ""
    t_ans = ""
    center = ""
    for char in sorted(dic.keys()):
        count = dic[char]
        if count % 2 == 1:
            center = char  # 홀수인 문자를 중앙에 위치
        ans += char * (count // 2)  # 문자열의 왼쪽 부분에 추가
        t_ans = char * (count // 2) + t_ans  # 문자열의 오른쪽 부분에 추가

    # 최종 팰린드롬 문자열 조합
    ans += center + t_ans
    print(ans)
