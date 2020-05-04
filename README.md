# GMRZ Gaming Recommender
GMRZ is a video game recommender system that allows users to search for game recommendations based on the games they searched.

<h2>Tutorial</h2>
<h3>User Account Creation</h3>

To start out and create an account, go to the upper right of the page where it says Login Register as pictured below
![](GMRZ%20Tutorial/LoginHomePage.png)

Click the <b> Register </b> Button which brings you to a form to register your account

![](GMRZ%20Tutorial/RegisterPage.png)

Fill in all the fields and then click the "Sign Up" button on the bottom of the form

![](GMRZ%20Tutorial/RegisteredFilledIn.png)


<h3> Login </h3>

Now that you've successfully made an account you can login, and you will be redirected to the login page where you can fill in your credentials to login

![](GMRZ%20Tutorial/LoginPage.png)

<h3>Profile</h3>

When logged in you will notice that the register and login button and the top right of the page is now replaced with the <b>Profile</b> and <b>Logout</b> buttons. 

Selecting Logout will log the user out and bring them back to the login page

By selecting the <b>Profile</b> page they can now access they account information and edit it as shown below
![](GMRZ%20Tutorial/ProfilePage.png)

From here the user can change their username, email, and profile photo by changing the fields and clicking on the "update" button

<h3>Searching For A Game</h3>

Now if you want to search for a game recommendation you first click the search bar on the top left.

![](GMRZ%20Tutorial/search.png)

Once you click the button you are brought to this recommender search bar

![](GMRZ%20Tutorial/search1.png)



You then can simply search for a game that you like to get recommended similiar games which will be shown like below


![](GMRZ%20Tutorial/search2.png)

You can then always click either the GMRZ logo or Home button to go back to the home page


-------------------------------------------------------------------------------------------------------------------------------------


<h2>Backend Recommender</h2>

![](GMRZ%20Tutorial/python.png)
![](GMRZ%20Tutorial/python1.png)


The API is parsed for games by ID number and the names are converted to ascii to be written into the text file. The recommendations are then found using the tag information and other aspects of the game from the API. The recommended games names are then also converted to ascii and written to the text file.



![](GMRZ%20Tutorial/python2.png)


These exceptions catch any errors that are returned from the API such as there not being any data for the games at that ID number. It also catches if there are not enough recommended games to fill the requested amount.


![](GMRZ%20Tutorial/python3.png)


Function that makes sure input text is in ascii format.



![](GMRZ%20Tutorial/python4.png)


The data is then taken from the text file and put into a list where it each items is separated by new lines. This data is then written to the excel file


![](GMRZ%20Tutorial/python5.png)


Then the data from all the games is extracted from the API by each ID number. The data being collected is the title, description, genre, tags, developer, publisher, platforms and places to purchase. Every aspect besides places to purchase gets converted to ascii.


![](GMRZ%20Tutorial/python6.png)


The description needs to be cleaned before it is 100% legible. After the ascii is removed the html tags needed to be removed. After the new lines are stripped and any unique characters are removed to not effect the text output.


![](GMRZ%20Tutorial/python7.png)


Function to remove html tags from the description


![](GMRZ%20Tutorial/python8.png)


The rest of the data was written to the excel sheet in this list iteration structure with commas in-between each tag.


![](GMRZ%20Tutorial/python9.png)



The text data was moved into a list just like the recommendations and then each aspect of the data was put into its own column.
