# with open("weather_data.csv", mode="r") as file:
#     data = file.readlines()
#     weather_data_list = [elm.strip() for elm in data]
# print(weather_data_list)

# import csv

# with open("weather_data.csv") as file:
#     data = csv.reader(file)
#     temperatures = []
#     for index, row in enumerate(data):
#         if index != 0:
#            temperatures.append(int(row[1]))
    
# print(temperatures)

import pandas

# data = pandas.read_csv("weather_data.csv")
# data_dict = data.to_dict()
# data_list = data["temp"].to_list()
# avg_temp = round(sum(data_list)/len(data_list), 2)
# avg_temp = data["temp"].mean()
# max_temp = data["temp"].max()

# get the row

# monday_row = data[data.day == "Monday"]
# max_temp_row = data[data.temp == data.temp.max()]

# print(monday_row.condition)

# create some data frame

# data_dict = {
#     "students": ["Amy", "John", "Johnny"],
#     "scores": [76, 56, 65]
# }

# custom_data = pandas.DataFrame(data_dict)
# convert the data frame to csv
# custom_data.to_csv("new_data.csv")


# Challenges 

squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census.csv")

black_color = squirrel_data[squirrel_data["Primary Fur Color"] == "Black"]
gray_color = squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"]
red_color = squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"]

black_squirrel = len(black_color)
gray_squirrel = len(gray_color)
red_squirrel= len(red_color)

survey_data = {
    "Fur Color" :["Gray", "Black", "Red"],
    "Count": [gray_squirrel, black_squirrel, red_squirrel]
}

data_frame =  pandas.DataFrame(survey_data)
data_frame.to_csv("squirrel_data.csv")
