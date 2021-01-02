## Testing

- [Validator checks](#validator-checks)
- [Testing user stories](#testing-user-stories)
- [Manual testing](#manual-function-testing)  
- [Additional Testing](#additional-testing)
- [Known Bugs](#known-bugs)
  
### Validator Checks

The W3C Markup Validator and W3C CSS Validator Services were used to validate every page (apart from the ones where you need to be logged in) of the project to ensure there was no invalid code in the various languages used. There were some errors initially, but these were fixed and detailed in the commit history. 

- [W3C Markup Validator](https://validator.w3.org/) No errors or warnings
- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) No errors.
- [JsHint](https://jshint.com/) (0 warnings)
- [PEP-8 checker](http://pep8online.com/)(All right)


### Testing User Stories

1. I heard of this website via word of mouth and want to see what it’s about.
    * a. An enticing home page concisely detailing the aims of this website.
2. I would like to find a recipe for dinner tonight. I am allergic to some things. 
    * a. See a list of all recipes on the database.
    * b. Filter the recipes by both allergens (multiple selection available) and dish category.
    * c. View the details of the recipes in an uncluttered easy to read page.
3. I am looking for a one stop place to add, edit and view my own recipes.
    * a. Add a recipe (registered user only).
    * b. Edit recipes that they have added (registered user only).
    * c. View a list of recipes they have added (registered user only).
4. I want to view recipes and know that I will never see recipes with my allergens in them. Sometimes I might want to see all recipes though, so I can adapt them myself.
    * a. Registered users who have clicked on their allergens when registering will not see recipes containing those allergens.
    * b. Registered users can toggle a switch to switch between being shown recipes with their allergens in, or without.
5. I am throwing a dinner party and my friends have an assorted collection of allergies. I want to find a recipe for every course to satisfy all their requirements.
    * a. Filter the recipes by both allergens (multiple selection available) and dish category.
6. I like to easily share recipes with people. 
    * a. Share a recipe button that upon hovering or clicking links to a number of social media.
7. As a registered user, I would like to easily be able to favourite recipes and navigate to my favourites easily. 
    * a. A Floating Action button on each recipe card adds the recipe to the user's Favourite Recipes page.

### Site owner goals:
1. I want to create a customer base to target with occasional direct marketing and special offers. (If not necessarily by DM via email, then by showing special offers only to logged in users.
    * a. Provide special features to registered users only.
2. I want to promote certain cooking tools / recipe books via my website.
    * a. Shop page.



### Further Testing

-   The website was tested on Google Chrome, Mozilla Firefox and Microsoft Edge browsers.
-   The website was viewed, using Chrome Developer Tools, on a variety of devices such as Desktop, Laptop, iPhone7, iPhone 8 & iPhoneX.
-   A large amount of testing was done to ensure that all pages were linking correctly.
-   Friends and family members were asked to review the site and documentation to point out any bugs and/or user experience issues.

### Known Bugs
