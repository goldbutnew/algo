N = int(input())

max_list = []

for s in range(1, N+1):
    first_num = N
    second_num = s
    temp_list = [first_num, second_num]

    while True:
        next_num = first_num - second_num
        if next_num >= 0:
            temp_list.append(next_num)
            first_num = second_num
            second_num = next_num
        else:
            if len(temp_list) > len(max_list):
                max_list = temp_list
            break

print(len(max_list))
print(* max_list)