import pandas

# Our NATO phonetic dict consisting of alphas and their corresponding value pairs
df = pandas.read_csv("nato_phonetic_alphabet.csv")
NATO_dict = {
    row.letter: row.row for (index, row) in df.iterrows()
}


def NATO():
    # request user input as follows
    user_input = input("Enter your name to generate corresponding NATO codes: ").upper()
    try:
        NATO_list = [NATO_dict[letter] for letter in user_input]
    except KeyError:
        print("Only alpha characters allowed! Try again...")
        NATO()
    else:
        print(NATO_list)


print(NATO())
