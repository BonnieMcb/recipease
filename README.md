# Recipease 

## Code Institute Milestone Project 2

This website is created for educational purposes only.

![Responsive](...)    
    
The brief for this third Milestone project was to ..............make a responsive and dynamic website using HTML5, CSS3 and JavaScript. CRUD .............It is the third of four projects as part of the Full Stack Web Development Program at The Code Institute. 

## Table of Contents
1. [**Project overview**](#project-overview)
2. [**UX (User Experience**](#ux-(user-experience))
3. [**Project overview**](#project-overview)
4. [**Project overview**](#project-overview)


## Project Overview
The Recipease recipe website was created first and foremost as a way to fulfill the requirements of the CI project brief. One of the example projects for the project brief was a recipe website. I decided to go with an example project this time, because with my last two projects I learnt that I am able to spend a long time deciding on what to make and I didn't want to waste valueble time deciding while I could be actually building the site instead. I once again took inspiration from my own life to differentiate the website a little. This website focuses on users who have allergies in their families.
Recipease was built using [Python](https://www.python.org/), [Flask](https://flask.palletsprojects.com/en/1.1.x/) and [MongoDB Atlas](https://www.mongodb.com/), which is a document-based database for the storing and retrieving data.

[Click here to view the project live.](https://ms3-recipease.herokuapp.com/)

## UX (User Experience)

### Goals
The Recipease website is a web application where users are able to add and store their own recipes, as well as view recipes added by others. It is designed with users in mind who have multiple allergens in their family or friend circle. 

#### Basic Goals
Users visiting this site will be able to:
- Register an account
- Log in and out
- See a list of all recipes on the database
- Registered users who have clicked on their allergens when registering will not see recipes containing those allergens
- Filter the recipes by both allergens (multiple selection available) and dish category
- View the details of the recipes
- Add a recipe (registered user only)
- Edit recipes that they have added (registered user only)
- View a list of recipes they have added (registered user only)
- Share a recipe?????????????//
- Visit the shop page??????????????

#### Stretch Goals
With time and resources allowing, other goals are to:
- Favourites

#### Future ideas for new features
- For the bird category in learning mode, have the modal play a soundfile of the noise the bird makes upon matching a pair.
- Have a collection of different facts in a json file and display a random one upon matching a pair instead of always the same one. This would increase replayability value.


### User Stories

1. I am looking for a one stop place to add, edit and view my own recipes.
2. I want to view recipes and know that I won't see recipes with my allergens in them.
3. I am throwing a dinner party and my friends have an assorted collection of allergies. I want to find a recipe for every course to satisfy all their requirements.
4. 

### Design

The ![Materialize library](https://materializecss.com/) was used throughout in order to maintain a consistent and clean-looking site throughout the pages. I looked at various other recipe websites for inspiration and decided on small recipe cards on the recipes page. The recipe page itself (where ingredients and method is detailed) was inspired by the ![BBC Food website](https://www.bbc.co.uk/food), as I liked their simple design and I like to see the ingredients and method at the same time. 

...????......

If no image is uploaded by the user, a default black and white icon image is displayed based on the category of the dish, so there is an icon with cafetière and cup for the breakfast category, an icon with banana and apple for the snack category and so on.

#### Colour Palette

Colours:
Allergens on for example restaurant menus, are often marked in different colours, for example https://www.dickinson.edu/images/Menu_Picture_for_Website.jpeg This is something that people with allergies are used to seeing, and I wanted to keep this for my website. Since my last two projects used fairly muted colours and I wanted to be a bit more playful with colours this time. 


 ![coolors](https://coolors.co/u/bonnie_mcbride)

- ![#051f20](https://placehold.it/15/051f20/000000?text=+) #051f20 'Swamp'


#### Typography

I used ![Google fonts](https://fonts.google.com/) to embed fonts into my site by copying the code into the <head> of my html. I chose the easy to read Open Sans font throughout the site, which was complementary to the font I used for the name of the website. This is the Pacifico font. .......................

#### Imagery

No imagery???

#### Wireframes

I did not create the website fully in a design tool only to then create it again in HTML/CSS. Instead I used design tools to mock up rough versions of my site, including design and colour combinations. Since this was a solo project, and I was struggling through the JavaScript parts quite slowly, I was mindful of spending too much time creating perfectly responsive design mockups. As such, I was happy keeping some information in my head rather than drawing out the exact version of the final website. On collabarative projects, however, I would have a more finalised version of the website in a design tool. 

![Wireframes](/assets/images/wireframes.png) 







materialize css
jquery


08/12/20 Gitpod was having some outage issues, also noted by CI. Seems one of my pushes did not go through.

TODO:
Figure out checkboxes on Add recipe

nice TODO:
only show favourite buttons when logged in OR 
    flash message/tooltip(Materialize) that one must be logged in to save to favourites

testing while coding for example:
flash("Permission to edit")
write about user provided input validation / access permissions etc


attributes:
    for add recipe tickboxes
    https://stackoverflow.com/questions/5799090/remove-whitespace-and-make-all-lowercase-in-a-string-for-python

    for m=Materialize dropdown validation workaround
    jquery code copied from Code Institute lesson Course  Mini Project | Putting It All Together  Adding A Task - Writing to the Database  Materialize Form Validation

Breakfast by Edward Boatman from the Noun Project
Cake by starwin from the Noun Project
Dessert by Handicon from the Noun Project
dinner by Adrien Coquet from the Noun Project
Salad by Normansyah from the Noun Project
Fruit by Lnhi from the Noun Project
snack by Alan Davis from the Noun Project
Soup by Aneeque Ahmed from the Noun Project
