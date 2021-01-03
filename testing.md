## Testing

- [Validator checks](#validator-checks)
- [Testing user stories](#testing-user-stories)
- [Manual testing](#manual-testing)  
- [Additional testing](#additional-testing)
- [Known bugs](#known-bugs)
  
### Validator Checks

The W3C Markup Validator and W3C CSS Validator Services were used to validate every page (apart from the ones where you need to be logged in) of the project to ensure there was no invalid code in the various languages used. There were some errors initially, but these were fixed and detailed in the commit history. 

- [W3C Markup Validator](https://validator.w3.org/) No errors or warnings
- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) No errors.
- [JsHint](https://jshint.com/) (0 warnings)
- [PEP-8 checker](http://pep8online.com/) (All right)


### Testing User Stories

1. I heard of this website via word of mouth and want to see what it’s about.
    * An enticing home page concisely detailing the aims of this website.
    * Explicit advertising of the features available to registered users.
    
![home page](/documents/screenshots/home_page.PNG)

2. I would like to find a recipe for dinner tonight. I am allergic to some things. 
    * See a list of all recipes on the database.
    * Filter the recipes by both allergen (multiple selection available) and dish category.
    * View the details of the recipes in an uncluttered easy to read page.
    
![filtered recipe](/documents/screenshots/filtered_recipe.PNG)
![recipe detail](/documents/screenshots/recipe_page.PNG)

3. I am looking for a one-stop place to add, edit and view my own recipes.
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


#### Testing site owner goals:
1. I want to create a customer base to target with occasional direct marketing and special offers (if not necessarily by DM via email, then by showing special offers only to logged in users).
    * Provide special features to registered users only to encourage registration
    * Maintain a database of registered users. Email address verification etc. was beyond the scope of this project, but if this were a real world application then a valid email address would also be required to register.
2. I want to promote certain cooking tools / recipe books via my website.
    * I did not have time to implement a shop page.

### Manual testing

#### Testing during development

The majority of testing occured during development. Chrome Development Tools were used extensively, both for front-end styling as well as checking what is being POSTed. The CRUD functionality and filtering was tested both on the website and by checking within MongoDB. Within the app.py file, flash messages were frequently used to check logic such as IF statements.

#### Testing the finished website

The site was tested first as a logged-out user (desktop and mobile) and then as a logged-in user.

1. Links
- All links and buttons were tested from and to every page.
- All hover effects were tested.
- All modals were tested by choosing both options and checking that the user was being redirected to the appropriate place.

2. Account
- A large number of test accounts were created with and without allergens.
- The user input validation was tested, and is correctly working so that the limitations set by me are working (for instance only alphanumeric characters for username).
- Log in and log out flash messages appear correctly.
- The correct content for logged-in users and guests is shown, including hiding the login/register hyperlinks in the home page content.
- Logging in with an incorrect username or password brings up the flash message "INCORRECT USERNAME OR PASSWORD".

3. Filtering allergens
- This was tested extensively, both logged-in and not. As a registered user with allergens and without. Turning safe search on and off. Adding and applying more allergens, and clearing filters.
- The filters were tested in all recipes and within the various categories and are functioning as expected, and without issues.

4. Add recipe
- Allergen tick boxes that are checked are sent through to MongoDB to create an array and are displayed on the recipe and recipe card.
- When ingredients and method steps are separated by comma they are displayed as unordered and ordered list items, respectively. 
- Submit button sends the data to MongoDB, and the Cancel button redirects to the recipes page as expected.
- Once the recipe has been submitted, it is displayed in the appropriate category, and excluded from the appropriate allergens.  
- It was found that no user input limitations or truncate class (from Materialize) had not been set on most of the input fields. This caused an issue on the recipes page where, if the user put in a long string of characters in any of the fields, this would create a long list of characters that shoot off viewport and create a horizontal scroll bar. This is what happens when you forget to apply defensive programming on one of the sections. It was an easy fix, the details of which are described in the Features section in the README.md
![](/documents/screenshots/user_input_bug.PNG) ![](/documents/screenshots/fixed_issue.png)

5. Edit / Delete recipe
- All of the tests under 'add recipe' are passed.
- Pressing 'submit' successfully updates the data in MongoDB and the edited recipe is displayed correctly.
- Clicking 'delete' brings up the confirmation modal. Clicking 'cancel' closes the modal and user remains on My Recipes page. Clicking 'delete' deletes the recipe from the database and the recipe is no longer accessible.
- Only users who have added the recipe can edit and delete it. During development it was noted that anyone could edit or delete recipes added by others by for example changing the 'show_recipe' part of the url to 'edit_recipe'. This was fixed by adding access permissions in the app.py file.

6. View recipe
- Image, allergens, and all information displaying correctly.
- It was noticed during testing that the user becomes stuck on the recipe page, with only the navigation bar to navigate for them. This is bad UX, so a BACK button was added that redirects to the page where the user came from.
![](/documents/screenshots/.png)


### Additional testing

-   The website was tested on Google Chrome, Mozilla Firefox and Microsoft Edge browsers.
-   The website was viewed, using Chrome Developer Tools with responsive mode, as well as on a variety of actual devices such as Desktop, Laptop, iPhone 11 and a Motorola phone.
-   Friends and family members were asked to review the site and documentation to point out any bugs and/or user experience issues.

### Known Bugs

Unfortunately there was no time to fix these issues.

- On small screens, the allergen key allignment gets messy on the Recipes and categories screens. 
- On some small screens the APPLY FILTER button is pushed down and obscures the allergen filter on the Recipes and categories screens.
![](/documents/screenshots/iphone11.jpeg)
