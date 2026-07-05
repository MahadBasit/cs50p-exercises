import re

def main():

    print(validate(input("IPv4 Address: ")))


def validate(ip):
    m = re.fullmatch(r"(?:1\d\d|2[0-4]\d|25[0-5]|[1-9]\d|\d)\.(?:1\d\d|2[0-4]\d|25[0-5]|[1-9]\d|\d)\.(?:1\d\d|2[0-4]\d|25[0-5]|[1-9]\d|\d)\.(?:1\d\d|2[0-4]\d|25[0-5]|[1-9]\d|\d)", ip)
    return bool(m)


if __name__ == "__main__":
    main()