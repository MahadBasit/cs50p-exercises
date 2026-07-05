import re

def main():
    print(convert(input("Hours: ")))


def convert(s):
    
    matches = re.match(r"^(1[0-2]|[1-9])(:[0-5][0-9])? (AM|PM) to (1[0-2]|[1-9])(:[0-5][0-9])? (AM|PM)$", s)

    if not matches:
        raise ValueError
    
    ap1 = matches.group(3)
    ap2 = matches.group(6)
    hr1 = matches.group(1)
    hr2 = matches.group(4)
    mn1 = matches.group(2)
    mn2 = matches.group(5)

    def to_24hr(hour_str, meridiem):
        if meridiem == 'AM':
            if hour_str == "12":
                hour_str = "00"
    
        elif meridiem == 'PM':
            if hour_str != "12":
                hour_str = str(int(hour_str) + 12)        

        return hour_str

    hr1 = to_24hr(hr1, ap1)
    hr2 = to_24hr(hr2, ap2)

    if not mn1:
        mn1 = ":00"

    if not mn2:
        mn2 = ":00"

    return f"{hr1}{mn1} to {hr2}{mn2}"




if __name__ == "__main__":
    main()