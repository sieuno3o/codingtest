def solution(my_string, is_suffix):
    suffix_length = len(is_suffix)
    substring = my_string[-suffix_length:]
    return 1 if substring == is_suffix else 0