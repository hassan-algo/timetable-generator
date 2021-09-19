import numpy as np
import random


class Person:

    def __init__(self, data):  # data=[ no of Teacher, no of lectures, no of rooms, no of section ]

        self.data = []  # 4D array
        # 4D array contains:
        # 1. Length of Teacher's name
        teacherData = []
        for i in range(data[0]):
            teacherData.append(bool(random.getrandbits(1)))
        # 2. Lecture Name
        lectureData = []
        for i in range(data[1]):
            lectureData.append(bool(random.getrandbits(1)))

        # 3. Room no.
        roomData = []
        for i in range(data[2]):
            roomData.append(bool(random.getrandbits(1)))
        # 4. Section
        sections = []
        for i in range(data[3]):
            sections.append(bool(random.getrandbits(1)))

        self.data = [teacherData, lectureData, roomData, sections]
        self.data = np.array(self.data)
        print(self.data)




if __name__ == "__main__":
    # Todo: get teachers data
    teacherData = [['A', 'B'], ['A', 'B']]  # two parameters => 1. Teacher Name 2. Lecture Name
    # Todo: get Class data
    classData = [['A', 'B'], [24, 50]]  # two parameters => 1. Room No. 2. Room Strength
    # Todo: get Student data
    studentData = [['A', 'B'], [24, 50], ['A', 'B']]  # 3 parameters => 1. Lecture Name 2. Lecture Strength 3. Section name
    # Todo: get Time data
    timetable = [[], []]  # two parameter => 1. Starting Time 2. Ending Time
    # Todo: get lectures data
    lectureData = [['A', 'B'], [1.5, 2]]  # two parameters => 1. Lecture Name 2. Lecture Length
    data = [len(teacherData[0]), len(lectureData[0]), len(classData[0]), len(studentData[2])]
    person = Person(data)
