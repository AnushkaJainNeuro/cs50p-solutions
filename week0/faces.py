sentence = input("Type a sentence and use an emoticon to express your feelings: ")

def convert(sentence):
    sentence = sentence.replace(":)", "🙂")
    sentence = sentence.replace(":(", "☹️")
    return sentence

print(convert(sentence))