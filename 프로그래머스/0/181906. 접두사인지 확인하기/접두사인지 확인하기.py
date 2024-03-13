def solution(my_string, is_prefix):
    prefix_length = len(is_prefix)
    substring = my_string[:prefix_length]
    return 1 if substring == is_prefix else 0