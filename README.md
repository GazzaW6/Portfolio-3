![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

# Hangman

This is my version on the classic game, Hangman. It was coded using Python. The aim of the game is for players to guess the correct word whilst ensuring they don't make more than 6 mistakes. Every mistake the user makes will result in your 'man' being one step closer to meeting his end and being hung.

This game is ideal for anyone who is wanting to improve their spelling or who is looking to blow off steam and kill some time. It is suitable for people of all ages.



## Features

* The game features an intro that contains the name of the game as well as the rules on how to play. This is printed to the console when the game is played.
* Players are promted to input a letter into the imput space. If player input a number or a full word, they will be prompted to try again as this is invalid.
* The Hangman image will be displayed throughout the game and will display the different stages of the game, illustrating the amount of mistakes the player has made and how many mistakes they can still afford to make.

## Testing

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

-----
Happy coding!