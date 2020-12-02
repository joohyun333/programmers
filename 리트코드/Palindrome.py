import string
import timeit
def palindrome(word : str) -> bool:
    result = [i.lower() for i in word if i in string.ascii_uppercase or i in string.ascii_lowercase or i in string.digits]
    while len(result) > 1:
        if result.pop(0) != result.pop():
            return False
    return True
if __name__ == "__main__":
    s = timeit.default_timer()
    # word = "A man, a plan, a canal : Panama"
    word = "race a car"
    print(palindrome(word))
    e = timeit.default_timer()
    print(e - s)