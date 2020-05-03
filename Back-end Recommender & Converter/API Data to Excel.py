import xlsxwriter
import unittest

#Opens the Text file
tFile = open("GameData.txt", "r")

#Creates the Excel file
workbook = xlsxwriter.Workbook('GameData.xlsx')
worksheet = workbook.add_worksheet()

#Reads all the data from the text file into a list
blist = tFile.readlines()
list = []
#List iterator
x = 0

#Formats the data from the list into another by seperating it on every new line
while x < len(blist):
    list.append(blist[x].strip("\n"))
    x = x + 1

#List iterator
x = 0
#Current line in the excel sheet
row = 1

#Writes the name of the game into column A
while x < len(list):
    #Removes ID number from the the current game
    cut = list[x].split('. ')
    #Writes the data to the excel sheet
    if len(cut) == 2:
        worksheet.write('A' + str(row), cut[1])
    # Writes the data to the excel sheet if it has ". " in the title
    if len(cut) == 3:
        worksheet.write('A' + str(row), cut[1] + ". " + cut[2])
    x = x + 1
    rec = []

    # Writes the data of the game into column B
    while list[x] != "":
        rec.append(list[x])
        x = x + 1
    print(rec)
    if len(rec) == 0:
        worksheet.write('B' + str(row), "Null")
    if len(rec) == 8:
        worksheet.write('B' + str(row), rec[0] + "\n" + rec[1] + "\n" + rec[2] + "\n" + rec[3] + "\n" + rec[4] + "\n" + rec[5] + "\n" + rec[6] + "\n" + rec[7])

    x = x + 1
    row = row + 1

#Closes the excel sheet
workbook.close()
#Closes the text file
tFile.close()

#Unit tests
class Tests(unittest.TestCase):
    #Testing ". " splitting
    def testSplit1(self):
        self.assertTrue("1. D/Generation HD".split('. ')[1] == "D/Generation HD")

#Runs the tests
if __name__ == '__main__':
    unittest.main()