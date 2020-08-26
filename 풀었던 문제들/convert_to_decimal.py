def convert_to_decimal(number, base):
    multiplier, result = 1, 0
    while number > 0 :
        result += number % 10 * multiplier
        print(result)
        multiplier *= base
        print(multiplier)
        number = number// 10
        print(number)
    return result

def test_converter_to_decimal():
    number, base = 1001, 2
    assert (convert_to_decimal(number, base)==9)
    print("테스트 통과")

if __name__ == "__main__":
    test_converter_to_decimal()