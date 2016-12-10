
""" FILES """
my_list = [str(i**3) for i in range(10)]
print(my_list)

import os
pathToFile = os.path.abspath("./Python_samedi/output.csv")
print(pathToFile)
my_file = open(pathToFile, "w")
# w = write to the file

my_col = ["a","b","c","d","e","f","g","h","i","j"]

my_file.write(";" .join(my_col)+"\n")
my_file.write(";" .join(my_list)+"\n")

my_file.close()

# for item in my_list:
#     my_file.write(str(item)+"\n")
# # n => go to the next line
# my_file.close()

#  read a full file

import csv
with open(pathToFile, "r") as csvfile:
    reader = csv.DictReader(csvfile, delimiter=";")
    for row in reader:
        print(row["c"])

