def simple_array_sum(array):
    return sum(array)


if __name__ == "__main__":
    n = int(input())
    my_array = list(map(int, input().split()))
    print(simple_array_sum(my_array))
