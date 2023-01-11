import datetime

def save_response(response):
    file = open("responses.txt", "a")
    timeMark = datetime.datetime.now().isoformat()
    file.write(str(timeMark) + "," + response + "\n")
    file.close

def runCSV(file):
    strings = []
    with open(file, "r") as f:
        for line in f:
            line = line.replace('\n', '')
            strings.append(line)
    return strings
