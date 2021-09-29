def extra_long_factorials(number: int) -> int:
    result: int = 1

    for i in range(1, number + 1):
        result *= i

    return result


if __name__ == '__main__':
    n = int(input().strip())

    extra_long_factorials(n)
