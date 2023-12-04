# File path for our different letters and names
starting_letter = "./Input/Letters/starting_letter.txt"
closing_letter = "./Output/ReadyToSend"
invited_names = "./Input/Names/invited_names.txt"

# Open our names and add it to a list with the 'readlines' method
with open(invited_names) as file:
    invited = file.readlines()

# Open our letter as well
with open(starting_letter) as letter:
    letter_content = letter.read()

# Next, we loop through each name and strip them of new lines (bare strip will remove front and trailing whitespace)
for name in invited:
    stripped_name = name.strip("\n")
    to_send = letter_content.replace("[name]", stripped_name)
    # finally save letters with appropriate names into the correct directory
    with open(f"{closing_letter}/{stripped_name}.txt", "w") as to_be_sent:
        to_be_sent.write(to_send)
