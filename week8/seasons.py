from datetime import date
import sys
import inflect
p = inflect.engine()

def main():
    birth_date = input("DOB (YYYY-MM-D): ")
    dob = validate_dob(birth_date)
    dt = date.today()
    r = dt - dob
    d = r.days
    print(p.number_to_words(d*1440, andword = ''))

def validate_dob(n):
    try:
        year, month, day = n.split('-')
        year = int(year)
        month = int(month)
        day = int(day)

        return date(year, month, day)

    except ValueError:
        sys.exit("Invalid Input")

if __name__ == "__main__":
    main()