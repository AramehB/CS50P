import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    s = s.strip().lower()
    match = re.findall(r"(\s|^)um{1}(\W|$|\s{1})", s)
    amount = len(match)
    return amount



if __name__ == "__main__":
    main()
