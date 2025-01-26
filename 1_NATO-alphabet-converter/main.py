import pandas
data=pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_dict={value.letter:value.code for (key, value) in data.iterrows()}
print(phonetic_dict)

def generate_phonetic():
    word=input("enter your word ->").upper()
    try:
        output_list = [phonetic_dict[i] for i in word]
    except KeyError:
        print("Sorry, only letters in alphabet please")
        generate_phonetic()
    else:
        print(output_list)

generate_phonetic()
