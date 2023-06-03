import datetime

"""This script create an empty file"""
filename = datetime.datetime.now()


# create empty file
def create_file():
    with open(filename.strftime("%Y-%m-%d-%H-%M") + ".txt", "w") as file:
        file.write("")  # empty string


create_file()
