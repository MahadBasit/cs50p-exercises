import emoji

em = input("Enter emoji string: ")

emo = emoji.emojize(em, language = 'alias')
print(emo)