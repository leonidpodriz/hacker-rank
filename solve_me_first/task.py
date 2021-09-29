def solve_me_first(*args: int) -> int:
    return sum(args)


if __name__ == '__main__':
    num1 = int(input())
    num2 = int(input())
    res = solve_me_first(num1, num2)
    print(res)
