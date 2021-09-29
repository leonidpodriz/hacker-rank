import os
from typing import Collection


def simple_array_sum(array: Collection[int]) -> int:
    return sum(array)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = simple_array_sum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
