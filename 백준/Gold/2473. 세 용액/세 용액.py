import sys

n = int(input())
solutions = list(map(int, input().split()))

solutions.sort()  # 용액들을 오름차순으로 정렬

closest_sum = sys.maxsize  # 가장 가까운 합
result = []

for i in range(n - 2):  # 첫 번째 용액을 선택
    left = i + 1  # 두 번째 용액의 인덱스
    right = n - 1  # 세 번째 용액의 인덱스

    while left < right:
        current_sum = solutions[i] + solutions[left] + solutions[right]
        # 현재 합이 가장 가까운 합에 더 가까우면 결과를 업데이트
        if abs(current_sum) < closest_sum:
            closest_sum = abs(current_sum)
            result = [solutions[i], solutions[left], solutions[right]]

        if current_sum < 0:
            left += 1  # 합이 0보다 작으면 왼쪽 포인터를 오른쪽으로 이동
        elif current_sum > 0:
            right -= 1  # 합이 0보다 크면 오른쪽 포인터를 왼쪽으로 이동
        else:  # 합이 0이면 더 이상 탐색할 필요 없음
            print(*result)  # 결과 출력
            sys.exit()

print(*result)  # 결과 출력