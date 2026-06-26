def main():
    sen = input()
    print(shorten(sen))


def shorten(word):
    result = ''
    for i in word:
        if i.upper() not in ['A', 'E', 'O', 'I', 'U']:
            result += i
    
    return result


if __name__ == "__main__":
    main()