import datetime
import time
import requests

def getOlat(name):
    f = open(name, "a")
    now = datetime.datetime.now()

    url = "https://lms.uzh.ch/dmz/"
    req = requests.get(url)
    # find "People"
    indexStudents = req.text.index("People")
    i = 0
    # find "("
    while req.text[indexStudents - i] != "(":
        i += 1
    # print(req.text[indexStudents-i])
    filter = req.text[indexStudents - i + 1:indexStudents]
    students = int(filter)

    f.write(now.strftime("%Y-%m-%d %H:%M:%S" + ": " + str(students) + "\n"))
    f.close()


def main():
    # generate new logfile
    logdate = datetime.datetime.now()
    nameOfLogFile = str(logdate.strftime("%Y-%m-%d")) + ".txt"
    # write new logfile
    logfile = open(nameOfLogFile, "w+")
    while True:
        getOlat(nameOfLogFile)
        time.sleep(60)
if __name__ == "__main__":
    main()
