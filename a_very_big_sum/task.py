def a_very_big_sum(array):
    return sum(array)


if __name__ == "__main__":
    n = int(input())
    my_array = list(map(int, input().split()))
    # my_array = [162547823, 342135, 32951325897, 204387, 49204823094]
    print(a_very_big_sum(my_array))
