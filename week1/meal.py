def main():
    time = input("What time is it? ").strip()
    time = convert(time)
    if 7 <= time <= 8:
        print("Breakfast time")

    elif 12 <= time <= 13:
        print("Lunch time")

    elif 18 <= time <= 19:
        print("Dinner time")
    

def convert(time):
    hr,min = time.split(":")
    min = float(min)/60
    new_time = float(hr) + min
    return new_time

if __name__ == "__main__":
    main()