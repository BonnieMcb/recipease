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
    * An enticing home page concisely detailing the aims of this website.
    * Explicit advertising of the features available to registured users.
![home page](/documents/screenshots/home_page.PNG)
2. I would like to find a recipe for dinner tonight. I am allergic to some things. 
    * See a list of all recipes on the database.
    * Filter the recipes by both allergen (multiple selection available) and dish category.
    * View the details of the recipes in an uncluttered easy to read page.
![filtered recipe](/documents/screenshots/filtered_recipe.PNG)
![recipe detail](/documents/screenshots/recipe_page.PNG)
3. I am looking for a one stop place to add, edit and view my own recipes.
    * Add a recipe (registered user only).
    * Edit/delete recipes that they have added (registered user only).
    * View a list of recipes they have added on the MY RECIPES page (registered user only).
 ![edit](/documents/screenshots/edit_recipe.PNG)
 ![dropdown](/documents/screenshots/dropdown.PNG)
 ![my recipes](/documents/screenshots/my_recipes.PNG)
4. I want to view recipes and know that I will never see recipes with my allergens in them. Sometimes I might want to see all recipes though, so I can adapt them myself.
    * Registered users who have clicked on their allergens when registering will not see recipes containing those allergens by default.
    * Registered users can toggle a switch to swap between being shown recipes with their allergens in, or without. An 'are you sure?' warning modal is displayed and must be clicked on to confirm.
 ![toggle](/documents/screenshots/hide_ally_on.PNG)
 ![confirmation](/documents/screenshots/confirmation_show_allergens.PNG)
5. I am throwing a dinner party and my friends have an assorted collection of allergies. I want to find a recipe for every course to satisfy all their requirements.
    * Filter the recipes by both allergens (multiple selection available) and dish category. (Also see 2. for screenshot evidence.) 
![recipes_page](/documents/screenshots/recipes_page.PNG)


### Site owner goals:
1. I want to create a customer base to target with occasional direct marketing and special offers. (If not necessarily by DM via email, then by showing special offers only to logged in users.
    * Provide special features to registered users only to encourage registration
    * Maintain a database of registered users. Email address verification etc. was beyond the scope of this project, but if this were a real world application then a valid email address would also be required to register.
2. I want to promote certain cooking tools / recipe books via my website.
    * I did not have time to implement a shop page.



### Further Testing

-   The website was tested on Google Chrome, Mozilla Firefox and Microsoft Edge browsers.
-   The website was viewed, using Chrome Developer Tools, on a variety of devices such as Desktop, Laptop, iPhone 11 and a Motorola phone.
-   Friends and family members were asked to review the site and documentation to point out any bugs and/or user experience issues.

### Known Bugs
