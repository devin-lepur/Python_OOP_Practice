"""
    Author: Devin Lepur
    Opening and writing files in python
    1/11/24
    No true goal for the end of this practice, simply familiar with the
    relevant methods, end program will be very simple/messy
"""

def readWrite():
    myFile = open("practice3input.txt", "a+")
    myFile.write("\nThis is the new last line")

    #Seek is needed to redirect where reading and writing is done
    #Using "a" access mode defaults it to the end of the file
    myFile.seek(0)
    print(myFile.read())

    #Realized seek is characters not lines
    myFile.seek(5)
    print(myFile.readline())

    myFile.close()


#Makes sense but was surprised to see the newline contained within the line
def readSpecificLine():
    myFile = open("practice3input.txt", "r")

    #Reads the contents of myFile into fileContents
    #Not memory or time efficient but the best way is super complex
    fileContents = myFile.readlines()

    print(fileContents[5])

    myFile.close()

def writeNew():
    myFile = open("practice3output.txt", "w+")

    myFile.write("This is my new file!")
    
    myFile.seek(0)
    print(myFile.read())

    myFile.close()

readWrite()
readSpecificLine()
writeNew()
