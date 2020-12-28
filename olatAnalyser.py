import re
import matplotlib.pyplot as plt
import datetime
import random
# Using readline()
file1 = open('2020-12-17.txt', 'r')
dataRaw = []
data = []
count = 0
time = []
students = []

while True:
    count += 1

    # Get next line from file
    line = file1.readline()

    # if line is empty
    # end of file is reached
    if not line:
        break
    dataRaw.append(line)
    datapoint = (count,line)
    time.append(line[11:16])
    studentsAtTime = [int(s) for s in re.findall(r'\b\d+\b', line)] #findall Numbers
    students.append(studentsAtTime[-1])
    point = (count, line[11:16], studentsAtTime[-1])
    data.append(point)
    print("Line{}: {}".format(count, line.strip()))

file1.close()
print("Print data tuples")
#print(time)
#print(students)
print(data)

shrinkTime = time[0::15]
shrinkStudents = students[0::15]



plt.scatter(shrinkTime,shrinkStudents)
plt.plot(shrinkTime,shrinkStudents)
plt.show()
