import datetime
import time
import requests




def getOlat():
    f = open("Log.txt", "a")
    now = datetime.datetime.now()

    url = "https://lms.uzh.ch/dmz/"
    req = requests.get(url)
    # find "People"
    indexPeople = req.text.index("People")
    i = 0
    # find "("
    while req.text[indexPeople - i] != "(":
        i += 1
    # print(req.text[indexPeople-i])
    filter = req.text[indexPeople - i + 1:indexPeople]
    people = int(filter)


    f.write(now.strftime("%Y-%m-%d %H:%M:%S"+ ": "+ str(people) + "\n"))
    f.close()

def main():
    while True:
        getOlat()
        time.sleep(2)

if __name__ == "__main__":
    main()
