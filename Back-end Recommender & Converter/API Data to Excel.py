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
    if len(cut) == 4:
        worksheet.write('A' + str(row), cut[1] + ". " + cut[2] + ". " + cut[3])
    x = x + 1
    rec = []

    # Writes the data of the game individually into column B-N
    while list[x] != "":
        rec.append(list[x])
        x = x + 1
    print(rec)
    if len(rec) == 0:
        worksheet.write('B' + str(row), "Null")
    if len(rec) == 13:
        worksheet.write('B' + str(row), rec[0])
        worksheet.write('C' + str(row), rec[1])
        worksheet.write('D' + str(row), rec[2])
        worksheet.write('E' + str(row), rec[3])
        worksheet.write('F' + str(row), rec[4])
        worksheet.write('G' + str(row), rec[5])
        worksheet.write('H' + str(row), rec[6])
        worksheet.write('I' + str(row), rec[7])
        rec1 = rec[8].split(". ")
        if len(rec1) == 2:
            worksheet.write('J' + str(row), rec1[1])
        # Writes the data to the excel sheet if it has ". " in the title
        if len(rec1) == 3:
            worksheet.write('J' + str(row), rec1[1] + ". " + rec1[2])
        if len(rec1) == 4:
            worksheet.write('J' + str(row), rec1[1] + ". " + rec1[2] + ". " + rec1[3])
        rec2 = rec[9].split(". ")
        if len(rec2) == 2:
            worksheet.write('K' + str(row), rec2[1])
        # Writes the data to the excel sheet if it has ". " in the title
        if len(rec2) == 3:
            worksheet.write('K' + str(row), rec2[1] + ". " + rec2[2])
        if len(rec2) == 4:
            worksheet.write('K' + str(row), rec2[1] + ". " + rec2[2] + ". " + rec2[3])
        rec3 = rec[10].split(". ")
        if len(rec3) == 2:
            worksheet.write('L' + str(row), rec3[1])
        # Writes the data to the excel sheet if it has ". " in the title
        if len(rec3) == 3:
            worksheet.write('L' + str(row), rec3[1] + ". " + rec3[2])
        if len(rec3) == 4:
            worksheet.write('L' + str(row), rec3[1] + ". " + rec3[2] + ". " + rec3[3])
        rec4 = rec[11].split(". ")
        if len(rec4) == 2:
            worksheet.write('M' + str(row), rec4[1])
        # Writes the data to the excel sheet if it has ". " in the title
        if len(rec4) == 3:
            worksheet.write('M' + str(row), rec4[1] + ". " + rec4[2])
        if len(rec4) == 4:
            worksheet.write('M' + str(row), rec4[1] + ". " + rec4[2] + ". " + rec4[3])
        rec5 = rec[12].split(". ")
        if len(rec5) == 2:
            worksheet.write('N' + str(row), rec5[1])
        # Writes the data to the excel sheet if it has ". " in the title
        if len(rec5) == 3:
            worksheet.write('N' + str(row), rec5[1] + ". " + rec5[2])
        if len(rec5) == 4:
            worksheet.write('N' + str(row), rec5[1] + ". " + rec5[2] + ". " + rec5[3])


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