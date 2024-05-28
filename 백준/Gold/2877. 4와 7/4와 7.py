def count_47_numbers(n):
    # n자리의 수열 중에서 4와 7로 이루어진 수의 개수를 반환
    if n == 1:
        return 2
    return 2 * count_47_numbers(n - 1)

def kth_47_number(k):
    length = 1
    while True:
        count = count_47_numbers(length)
        if k <= count:
            break
        k -= count
        length += 1

    result = ''
    for i in range(length):
        if k <= 2 ** (length - i - 1):
            result += '4'
        else:
            result += '7'
            k -= 2 ** (length - i - 1)
    return result

k = int(input())
print(kth_47_number(k))
