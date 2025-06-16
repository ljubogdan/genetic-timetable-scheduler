import os

DATA_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data', 'data_timetable.txt'))

def read_rooms():
    with open(DATA_PATH, "r") as file:
        first_line = file.readline().strip()
        rooms = first_line.split(": ")[1].split(", ")

    return rooms

def read_lectures():
    lectures = []
    with open(DATA_PATH, "r") as file:
        lines = file.readlines()[2:]  
        for line in lines:
            lecture_name, time_minutes = line.strip().split(", ")
            lectures.append((lecture_name, int(time_minutes)))
    return lectures

