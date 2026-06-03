def convert(text):
    text = text.replace(':)', '🙂')
    text = text.replace(':(', '🙁')
    return text

def main():
    speech = input("What do you want to say? ")
    speech = convert(speech)
    print(speech)
main()