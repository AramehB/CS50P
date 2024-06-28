import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    s = s.strip()

    match = re.search(r"^<iframe.+(https?://(?:www\.)?youtube\.com/embed/([A-Za-z0-9]+))", s)
    if match:
        _ = match.group(2)
        link = "https://youtu.be/" + _
        return link
    else:
        return None



if __name__ == "__main__":
    main()
