def convert_to_decimal_larger_bases(number, base):
    strings = "0123456789ABCDEFGHIJ"
    result = ""
    while number > 0:
        digit = number % base
        result = strings[digit] + result
        number = number // base
    return result


def test_convert_to_decimal_larger_base():
    number, base = 31, 16
    assert(convert_to_decimal_larger_bases(number, base) == "1F")
    print("테스트통과")

if __name__ == "__main__" :
    test_convert_to_decimal_larger_base()