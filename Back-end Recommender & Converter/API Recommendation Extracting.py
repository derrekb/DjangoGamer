import rawgpy
import unittest

#Instantiation of the API with the name of our application
rawg = rawgpy.RAWG("GMRZ")

#Name of the file
tFile = open("GameRecommendations.txt", "w")

# Forces the name of the game to only use ascii charecters
def makeAscii(input):
    enas = input.encode("ascii", "ignore")
    out = enas.decode()
    return out

#Starting game ID number
x = 1

#Current total games in the API = 428553
#Set to 4 for testing
while x < 4:
    try:
        #Saves the current games data to variable "cur"
        cur = rawg.get_game(str(x))
        name = makeAscii(cur.name)
        #Writes the current ID of the game and its name to the file
        tFile.write(str(x) + ". ")
        tFile.write(name)
        tFile.write("\n")
        i = 0
        sug = cur.suggestions
        #Sets the max amount of recommendations
        while i < 5:
            #Forces the current recommended game to only use ascii charecters
            rec = makeAscii(next(sug).name)
            #Writes the number rank of the recommendation and then name of the game to the file
            tFile.write(str(i + 1) + ". " + rec)
            tFile.write("\n")
            i = i + 1
        tFile.write("\n")
        #Prints the current ID in the console
        print(x)
        x = x + 1
    #Catches Attribute Errors if there is no data from the api for that ID
    except AttributeError:
        print(x)
        print("No data")
        x = x + 1
    # Catches Key Errors if there is no data from the api for that ID
    except KeyError:
        print(x)
        print("No data")
        x = x + 1
    # Catches Stop Iteration endings if there is not enough data to fill the max amount of recommendations
    except StopIteration:
        tFile.write("\n")
        print("End")
        x = x + 1
#Closes the file
tFile.close()

tFile = open("GameRecommendations.txt", "r")
#ascii checking
isascii = lambda s: len(s) == len(s.encode())
#Data for testing
ges = rawg.get_game("1").suggestions


#Unit tests
class Tests(unittest.TestCase):
    #Testing ascii checking
    def testAscii1(self):
        self.assertTrue(isascii("Ascii"))
    def testAscii2(self):
        self.assertFalse(isascii("¿"))
    # Testing game name retrevial from the API
    def testName(self):
        self.assertTrue("D/Generation HD" == rawg.get_game("1").name)
    #Testting values are getting converted to ascii
    def testAscii3(self):
        self.assertFalse(isascii(rawg.get_game("183").name))
    def testAscii4(self):
        self.assertTrue(isascii(makeAscii(rawg.get_game("183").name)))
    #Checking recommendations
    def testRec1(self):
        self.assertTrue("Super Strawberry Man" == str(next(ges).name).rstrip())
    def testRec2(self):
        self.assertTrue("Death Fungeon" == str(next(ges).name).rstrip())
    def testRec3(self):
        self.assertTrue("Imprisoned Light" == str(next(rawg.get_game("2").suggestions).name))
    #Cheking text file
    def testFile1(self):
        self.assertTrue("1. D/Generation HD" == tFile.readline().rstrip())
    def testFile2(self):
        self.assertTrue("1. Super Strawberry Man" == tFile.readline().rstrip())
    def testFile3(self):
        self.assertTrue("2. Death Fungeon" == tFile.readline().rstrip())

#Runs the tests
if __name__ == '__main__':
    unittest.main()

#Closes the file
tFile.close()