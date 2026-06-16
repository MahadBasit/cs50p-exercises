months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    try:
        date = input('Date: ')
        if ',' in date:
            m = date.split(" ")
            m[1] = m[1].strip(',')
            m1 = months.index(m[0]) + 1
            if 1 <= m1 <= 12 and 1 <= int(m[1]) <= 31: 
                print(f'{m[2]}-{m1:02}-{int(m[1]):02}')
                break

        elif '/' in date:
            m = date.split('/')
            m1 = int(m[0])
            if 1 <= m1 <= 12 and 1 <= int(m[1]) <= 31: 
                print(f'{m[2]}-{m1:02}-{int(m[1]):02}')
                break

    except (IndexError, ValueError):
       pass