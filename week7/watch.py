import re

def main():
    print(parse(input("HTML: ")))


def parse(s):
    srch = re.search(r"http(?:s)?://(?:www\.)?(?:youtube\.com/embed/|youtu\.be/)([\w-]+)", s)
    if srch is None:
        return None

    id1 = srch.group(1)
    
    return f"https://youtu.be/{id1}"


if __name__ == "__main__":
    main()