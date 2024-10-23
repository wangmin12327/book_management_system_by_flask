from itertools import combinations

def min_difference(input_str):

    min_difference = float('inf') #确保初始值不为无穷小

    for input_str_child_a in combinations(input_str, 5): # 返回iterable中所有长度为r的子序列

        a = sum(input_str_child_a)
        b = sum(input_str) - a
        min_difference = min(min_difference,abs(a-b))

    return min_difference

if __name__ == '__main__':
    input_str = list(map(int, input().split()))
    result = min_difference(input_str)
    print(result)