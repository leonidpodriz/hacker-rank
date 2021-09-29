import os
from typing import Collection, Tuple


def compare_triplets(a: Collection[int], b: Collection[int]) -> Tuple[int, int]:
    a_points: int = 0
    b_points: int = 0

    for one_a_point, one_b_point in zip(a, b):
        if one_a_point > one_b_point:
            a_points += 1
        elif one_a_point < one_b_point:
            b_points += 1

    return a_points, b_points


# Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compare_triplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
