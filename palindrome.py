import sys

def is_palindrome(string):
    return string == string[::-1]

if __name__ == "__main__":
    string = sys.argv[1]

    if is_palindrome(string.lower()):
        print(string, "is a palindrome")
    else:
        print(string, "is not a palindrome")
