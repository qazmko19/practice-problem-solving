def extra_long_factorials(end):
    start = 1
    for number in range(1, end+1):
        start *= number
        yield start


if __name__ == "__main__":
    n = int(input())
    result = []
    for num in extra_long_factorials(n):
        result.append(num)
    print(result[-1])
