def calculate_an(n, p, q):
    calculated_values = {}

    def recursive_calculation(x):
        if x <= 0:
            return 1
        if x in calculated_values:
            return calculated_values[x]
        calculated_values[x] = recursive_calculation(x // p) + recursive_calculation(x // q)
        return calculated_values[x]

    return recursive_calculation(n)

n, p, q = map(int, input().split())
result = calculate_an(n, p, q)
print(result)

