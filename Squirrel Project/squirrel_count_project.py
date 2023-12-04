import pandas

# Open the file and convert to a DataFrame
df = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
primary_fur_color = df["Primary Fur Color"]

# get hold of the gray, black and cinnamon squirrels
gray = df[primary_fur_color == "Gray"]
black = df[primary_fur_color == "Black"]
cinnamon = df[primary_fur_color == "Cinnamon"]

# pass in our squirrel count in form of a dict to a pandas DF
squirrel_df = pandas.DataFrame({
    "Fur Color": ["Gray", "Black", "Cinnamon"],
    "Count": [len(gray), len(black), len(cinnamon)]
})

# convert and save as a csv file as follows
squirrel_df.to_csv("squirrel_census_final.csv")
