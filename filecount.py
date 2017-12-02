import os


def changedirectory():
    cwd = os.getcwd()
    print("The current directory is:",cwd)
    loop = True

    while loop:
        changeboolian = raw_input("Would you like to change the working directory? (Y/N)")
        if changeboolian == "Y" or changeboolian == "N":
            loop = False
        else:
            print("Please type either 'N' or 'Y' to proceed)")

    if changeboolian == "N":
        return cwd
    else:
        wd = raw_input("What would you like to change the directory to? (Must be an absolute path)")
        os.chdir(wd)
        print("Changed directory!")
        return


def getdirectories():
    listtoreturn = []
    directories = os.listdir(os.getcwd())
    for directory in directories:
        listtoreturn.append(directory)
    return listtoreturn


def getfiles(directories):
    filelist = []
    originaldirectory = os.getcwd()
    for directory in directories:
        newWD = originaldirectory + "/" + directory
        if os.path.isdir(newWD):
            ls = os.listdir(newWD)
            for file in ls:
                filelist.append(file)
    ls = os.listdir(originaldirectory)
    for file in ls:
        filepath = originaldirectory + "/" + file
        if os.path.isfile(filepath):
            filelist.append(file)
    return filelist


def hasextension(file):
    for character in file:
        if character == ".":
            return True
    return False


def getextension(file):
    charlist = []
    periodLocations =[]
    for character in file:
        charlist.append(character)
    for i in range(len(charlist)):
        if charlist[i] == ".":
            periodLocations.append(i)
    index = periodLocations[-1]
    return file[-(len(file)-index-1):]


def getExtensionList(filelist):
    extensionlist =[]
    for file in filelist:
        if hasextension(file):
            extensionlist.append(getextension(file))
        else:
            extensionlist.append("NONE")
    return extensionlist


def countExtensions(extensionlist):
    extDict = {}
    extSet = set()
    for extension in extensionlist:
        if extension not in extSet:
            extSet.add(extension)
            extDict[extension] = 1
        else:
            extDict[extension] += 1
    return extDict


def writetofile(extensioncount,path):
    output = open(path + "/" + "output.csv", 'w')
    output.write("File Type,Count\n")
    for key in extensioncount:
        toprint = str(key) + "," + str(extensioncount[key]) + "\n"
        output.write(toprint)


def filecount():
    loop = True
    while loop: #Include subdirectories query
        changeboolian = raw_input("Would you like to include subdirectories? (Y/N)")
        if changeboolian == "Y":
            directories = getdirectories()
            loop = False
        elif changeboolian == "N":
            directories = [os.getcwd()]
            loop = False
        else:
            print("Please type either 'N' or 'Y' to proceed)")

    filelist = getfiles(directories) #get list of all file names
    extensionlist = getExtensionList(filelist)
    extensioncount = countExtensions(extensionlist)


    loop = True
    while loop:  # Include subdirectories query
        changeboolian = raw_input("Would you like to to save the output csv to a different folder? (Y/N)")
        if changeboolian == "Y":
            path = input("What is the path to the directory? (must be an absolute path)")
            loop = False
        elif changeboolian == "N":
            path = os.getcwd()
            loop = False
        else:
            print("Please type either 'N' or 'Y' to proceed)")
    writetofile(extensioncount,path)

    return


def main():
    loop = True
    while loop:
        print("Welcome to the Filetype Lister 1.0")
        option = raw_input("Type 'R' to run the tool, 'D' to change directory, or 'exit' to exit the tool: ")
        if option == "R":
            confirm = raw_input("Press enter to continue or type anything else to return to the menu")
            if len(confirm) == 0:
                filecount()
        elif option == "D":
            changedirectory()
        elif option == "exit":
            print("Now exiting the tool, Goodbye.")
            exit()
        else:
            print("Error: Input not recognized, returning to the menu.")


main()
