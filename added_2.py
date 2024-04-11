def string_num(ch):
    letter_count = 0
    digit_count = 0
    space_count = 0
    other_count = 0
    for char in ch:
        if char.isalpha():
            letter_count += 1
        elif char.isdigit():
            digit_count += 1
        elif char.isspace():
            space_count += 1
        else:
            other_count += 1
    return letter_count, digit_count, space_count, other_count

input_string = input()
letter_count, digit_count, space_count, other_count = string_num(input_string)
print("统计结果：字母有{}个，数字有{}个，空格有{}个，其他字符有{}个。".format(letter_count, digit_count, space_count, other_count))