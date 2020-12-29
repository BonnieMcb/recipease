# Recipease 

## Code Institute Milestone Project 3

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


### Features

#### Existing Features

##### Consistent Features across all pages

- Always-visible navigation bar with the *Recipease* logo on the left (linking to index.html) and links to the sub-pages on the right. 
................... - Navigation bar changes to a hamburger button on small screens.
- Sticky footer with links to social media.
...................- A 'Back to Top' button that pops up on all pages once the user has scrolled more than 100px.

##### Home

- A simple but bright home page detailing briefly what the site is intended to do.
- Three sections advertising its main and differentiating features, with the intent to entice the user to continue on to use the features of the site.

"Feel at ease at Recipease that if you want to, you will never see recipes with your allergens in them."

##### Recipes

- The user is presented with an uncluttered page with small recipe cards (4 on large screens, 2 on small screens) which are all the same size with the same size pictures. Only picture, name and allergens are shown at first.
- Upon clicking a card, more information relating to the recipe is shown, and with another click, the user is taken to the recipe page.
- If the user has linked to a picture when they added the recipe, this will be displayed on the card. If not, a black and white icon will be displayed that relates to the type of dish (cake, dinner, soup etc.).
- At the top of the page are two dropdown filters. The allergen filter has multiple selection options, the category dropdown only one. There are apply filter and clear filter buttons. 

##### Recipe page

- Information about the recipe is featured at the tope of the page, widely spaced and easy to scan. The allergens are displayed with the same colours as on the recipe cards.
- Ingredients and method are divided into two columns that are next to each other on large screens and stack on top of each other on smaller screens.
....... - Picture at bottom????

##### Shop 

- ??

##### My Recipes

- The user is presented with identical recipe cards as on the RECIPES page, but only the ones that they have added themselves.
- On the cards there are EDIT and DELETE buttons. Clicking on DELETE will bring up a modal that asks the user if they definitely want to delete the recipe, or cancel the deletion. Clicking EDIT will redirect to the EDIT RECIPE page (see below).

##### Add Recipe / Edit Recipe

- The EDIT RECIPE page is identical to the ADD RECIPE one, but has all the information pre-selected and filled in.
- The ADD/EDIT pages are layed out in a similar structure as the Recipe page, with widely spaced out sections for the vital information, and then the sections to fill in ingredients and methods at the bottom of the screen. 
- At the bottom there are buttons to ADD/EDIT or CANCEL. 
- In terms of input fields ................................................
regex etc....

##### Account

- In order to unclutter the nav bar, the navigation links to pages related to a user's account were consolidated into an expandable ACCOUNT button, containing the options to LOG IN and REGISTER.
describe verification and regex etc....


#### Features To Be Implemented

- 


## Technologies Used

#### Languages Used
- HTML5
- CSS3
- jQuery
- Python

#### Frameworks, Libraries & Programs Used

1. [MongoDB](https://www.mongodb.com/)
    - MongoDB is a document-based database where content of the website is stored, read, edited and deleted.
2. [Flask](https://flask.palletsprojects.com/en/1.1.x/)
    - Flask is a web application framework.
3. [Flask PyMongo] (https://flask-pymongo.readthedocs.io/en/latest/)
    - v  MongoDB support for Flask applications
4. [https://pymongo.readthedocs.io/en/stable/index.html](https://pymongo.readthedocs.io/en/stable/index.html)
    - PyMongo is a Python distribution containing tools for working with MongoDB, and is the recommended way to work with MongoDB from Python
5. [Werkzeug](https://palletsprojects.com/p/werkzeug/)
    - Flask wraps Werkzeug, using it to handle the details of WSGI while providing more structure and patterns for defining powerful applications.
6. [Jinja](https://palletsprojects.com/p/jinja/)
    - Jinja2 is a full-featured template engine for Python.
7. [BSON](https://www.mongodb.com/json-and-bson)
    - BSON is the binary encoding of JSON-like documents that MongoDB uses when storing documents in collections.
8. [Gitpod](https://www.gitpod.io/)
    - Gitpod was the environment in which the site was created, using the terminal to commit to Git and Push to GitHub.
9. [Github](https://github.com/)
    - Hosting for software development and version control using Git.
10. [Heroku](https://www.heroku.com/home)
    - Heroku is a cloud platform as a service supporting several programming languages.
11. [Materialize](https://materializecss.com/)
    - A modern responsive front-end framework based on Material Design.
12. [Google Fonts:](https://fonts.google.com/)
    - Google fonts were used to import the 'Montserrat' font into the style.css file which is used on all pages throughout the project.
13. [Font Awesome:](https://fontawesome.com/)
    - Font Awesome was used on all pages throughout the website to add icons for aesthetic and UX purposes.
14. [Figma](https://www.figma.com/) 
    - Figma was used to create wireframes and aid design and layout decisions.




## Testing

The W3C Markup Validator and W3C CSS Validator Services were used to validate every page of the project to ensure there was no invalid HTML or CSS.

-   [W3C Markup Validator](https://validator.w3.org/) Fully passed, no errors or warnings
-   [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) My CSS has no errors or warnings, but Bootstrap CSS intentionally does.

### Testing User Stories

#### 1. As a potential customer, I want to see services on offer and get a feel for the company.
- The user is presented with a high-contrast, easily-readable navigation bar with links to other pages on the site. 
- The eye is also drawn down to the hero image, with contrasting text clarifying what the company provides in just a few words.
- The user can then scroll down to read more about the company, with “What we do” visible in tablet and mobile to invite scrolling. 
- A ‘Back to top’ button is provided on all pages once the user scrolls a certain amount, and the nav bar is stuck to the top of the screen as you scroll, so the user never gets stuck at the bottom of a page with nowhere to go.
#### 2. As a potential customer who has had a bad experience at a competitor, I want to know who the groomers are and if they are reliable.
- A description of the team and their qualifications is provided on the home page, immediately followed by testimonials and links to social media for further investigation of the company’s reputation.
#### 3. As a potential user, I browse websites on my mobile phone and want to have a good experience and be able to find and view the information I want.
- The website is responsive on smaller screens with the result being an aesthetically-pleasing and functional site on all screen sizes.
#### 4. As a potential customer I want to know if this place is easy to get to.
- In addition to the address and contact information in the footer, there is also a page with an embedded google map, and parking/public transport information.
#### 5. As a potential customer I want to know what other people say about this business.
Testimonials are found on the home page, and the links to social media are visible on the high-contrast footer on every page.
#### 6. As a returning or potential customer I want to be reminded of the services available and be able to make a booking easily.
- The services are laid out in a clear and clean manner, with a text description, as well as pictograms to provide information at a glance. A ‘Book Now’ button under every different service links to the Bookings page.
- The Bookings page has a short form with required fields, as well as the phone number at the top of the page for those who prefer to call.
- The contact information for phone and email are also provided in the footer on every page.


### Further Testing

-   The website was tested on Google Chrome, Mozilla Firefox and Microsoft Edge browsers.
-   The website was viewed, using Chrome Developer Tools, on a variety of devices such as Desktop, Laptop, iPhone7, iPhone 8 & iPhoneX.
-   A large amount of testing was done to ensure that all pages were linking correctly.
-   Friends and family members were asked to review the site and documentation to point out any bugs and/or user experience issues.

### Known Bugs







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
