import rawgpy
import re
import html
import unittest

#Instantiation of the API with the name of our application
rawg = rawgpy.RAWG("GMRZ")

#Name of the file
tFile = open("GameData.txt", "w")

# Forces the name of the game to only use ascii charecters
def makeAscii(input):
    enas = input.encode("ascii", "ignore")
    out = enas.decode()
    return out

# Removes unwanted html tags in the string
def remHtml(input):
    tag_re = re.compile(r'(<!--.*?-->|<[^>]*>)')
    no_tags = tag_re.sub('', input)
    out = html.escape(no_tags)
    return out

#Starting game ID number
x = 1

#Current total games in the API = 428553
#Set to 4 for testing
while x <= 3:
    try:
        # Saves the current games data to variable "cur"
        cur = rawg.get_game(str(x))
        name = makeAscii(cur.name)
        # Writes the current ID of the game and its name to the file
        tFile.write(str(x) + ". ")
        tFile.write(name)
        tFile.write("\n")
        # Writes the title of the game to the file
        tFile.write("Title: " + name)
        tFile.write("\n")
        des = makeAscii(cur.description)
        des = remHtml(des)
        #Removes newlines from the string
        des = des.rstrip()
        #Removes unwanted charecters from the string that might make newlines
        des = re.sub('[^a-zA-Z0-9-_*.:/]', " ", des)
        #Replaces newlines with blanks just to be sure they are gone
        des = des.replace("\n", "")
        # Writes the description of the game to the file
        tFile.write("Description: " + des)
        tFile.write("\n")
        # Writes the genres of the game to the file
        tFile.write("Genres: ")
        i = 0
        #Writes every genre in the list and formats it properly
        while len(cur.genres) > i:
            gen = makeAscii(cur.genres[i].name)
            tFile.write(gen)
            if i < len(cur.genres)-1:
                tFile.write(", ")
            i = i + 1
        tFile.write("\n")
        # Writes the tags of the game to the file
        tFile.write("Tags: ")
        i = 0
        # Writes every tag in the list and formats it properly
        while len(cur.tags) > i:
            tag = makeAscii(cur.tags[i].name)
            tFile.write(tag)
            if i < len(cur.tags)-1:
                tFile.write(", ")
            i = i + 1
        tFile.write("\n")
        # Writes the developers of the game to the file
        tFile.write("Developers: ")
        i = 0
        # Writes every developer in the list and formats it properly
        while len(cur.developers) > i:
            dev = makeAscii(cur.developers[i].name)
            tFile.write(dev)
            if i < len(cur.developers)-1:
                tFile.write(", ")
            i = i + 1
        tFile.write("\n")
        # Writes the publishers of the game to the file
        tFile.write("Publishers: ")
        i = 0
        # Writes every publisher in the list and formats it properly
        while len(cur.publishers) > i:
            pub = makeAscii(cur.publishers[i].name)
            tFile.write(pub)
            if i < len(cur.publishers)-1:
                tFile.write(", ")
            i = i + 1
        tFile.write("\n")
        # Writes the platforms the game is advalible on to the file
        tFile.write("Platforms: ")
        i = 0
        #Writes every platform the game is advalible on in the list and formats it properly
        while len(cur.platforms) > i:
            plt = makeAscii(cur.platforms[i].name)
            tFile.write(plt)
            if i < len(cur.platforms)-1:
                tFile.write(", ")
            i = i + 1
        tFile.write("\n")
        # Writes where the game can be purchased to the file
        tFile.write("Places To Purchase: ")
        i = 0
        # Writes every place the game can be purchased in the list and formats it properly
        while len(cur.stores) > i:
            tFile.write(cur._stores[i].url)
            if i < len(cur.stores)-1:
                tFile.write(", ")
            i = i + 1
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
        # Prints the current ID in the console
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

tFile = open("GameData.txt", "r")
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
    # Testing game name retrieval from the API
    def testName(self):
        self.assertTrue("D/Generation HD" == rawg.get_game("1").name)
    #Testting values are getting converted to ascii
    def testAscii3(self):
        self.assertFalse(isascii(rawg.get_game("183").name))
    def testAscii4(self):
        self.assertTrue(isascii(makeAscii(rawg.get_game("183").name)))
    #Checking unwanted html tags get removed
    def testHtml1(self):
        self.assertFalse("New control menu<br/></li><li> can save at any point" == "New control menu can save at any point")
    def testHtml2(self):
        self.assertTrue(remHtml("New control menu<br/></li><li> can save at any point") == "New control menu can save at any point")
    def testHtml3(self):
        self.assertTrue(remHtml("<strong>Extreme Exorcism</strong>") == "Extreme Exorcism")
    #Cheking text file
    def testFile1(self):
        self.assertTrue("1. D/Generation HD" == tFile.readline().rstrip())
    def testFile2(self):
        self.assertTrue("Title: D/Generation HD" == tFile.readline().rstrip())
    def testFile3(self):
        tFile.readline()
        self.assertTrue("Genres: Adventure, Puzzle" == tFile.readline().rstrip())
    def testFile4(self):
        self.assertTrue("Tags: Full controller support, Steam Achievements, Steam Leaderboards, Retro, Singleplayer" == tFile.readline().rstrip())
    #Checking recommendations
    def testRec1(self):
        self.assertTrue("Super Strawberry Man" == str(next(ges).name).rstrip())
    def testRec2(self):
        self.assertTrue("Death Fungeon" == str(next(ges).name).rstrip())
    def testRec3(self):
        self.assertTrue("Imprisoned Light" == str(next(rawg.get_game("2").suggestions).name))

#Runs the tests
if __name__ == '__main__':
    unittest.main()

#Closes the file
tFile.close()