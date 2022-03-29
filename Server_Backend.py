

#adds username to file to be exported to front end
def addUserName(name, file):
    file = open(file, "a")
    file.write(name + "\n")
    file.close()

    
#verifies if the username is take or not
def verifyUserName(name, file):
    file = open(file, "r")
    lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].strip("\n")
        if name == lines[i]:
            return False
    return True

#eventually will use inputs from a website
def main():
    file = "usernames.txt"
    verify = verifyUserName("L", file)
    if verify == False:
        print("That username is already taken, try another.")
    else:
        addUserName("L", file)
main()