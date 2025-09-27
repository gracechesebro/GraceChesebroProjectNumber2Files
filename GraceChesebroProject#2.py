with open("vgsales.csv", "r") as my_file:
    lines = my_file.readlines()

for line in lines:
    split_line = line.split(",")

    game = str(split_line[1])
    NA_sales = int(split_line[6])
    EU_sales = int(split_line[7])
    JP_sales = int(split_line[8])
    Other_sales = int(split_line[9])

    #addition
    total_copies_per_year = NA_sales + EU_sales + JP_sales + Other_sales

    #division
    average_copies_per_year = total_copies_per_year /4