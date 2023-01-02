# BLS Digital


Welcome to [BLS Digital](#)!

![Application on different screens](#)

## Contents
- [User Experience](#user-experience)
    - [User Stories](#user-stories)
    - [Agile Methodology](#agile-methodology)
    - [Wireframes/Flowchart](#wireframesflowchart)
    - [Design](#design)
- [Features](#features)
    - [Existing Features](#existing-features) 
    - [Future Features](#future-features)
- [Tecnologies Used](#technologies-used)
    - [Technologies Used](#technologies-used)
    - [Libraries](#libraries)
- [Testing](#testing)
- [Bugs](#bugs)
    - [Solved](#solved)
    - [Left to Solve](#left-to-solve)
- [Deployment](#deployment)
    - [Deployment to Heroku](#deployment-to-heroku)
    - [Forking The Repository On GitHub](#forking-the-repository-on-github)
    - [How To Clone The Project](#how-to-clone-the-project)
- [Credits](#credits)
- [Acknowledgements](#acknowledgements)


## User Experience
### User Stories
![Screenshot of all user stories](/media/readme_images/user_stories.png)

[Back to top](#contents)
### Agile Methodology
#### GitHub Project Board
GitHubs Projects is used in this project to keep track of the user stories that is done, ongoing and not started yet.
It has been a big help to go there and get a overlook of what has been done and what is left when it has been tough.
When you work in a team i think this will be an even bigger help.

I also divided the work in two iterations so I could have goals that were more manageable.

![Screenshot of project board](/media/readme_images/project_board.png)

[Back to top](#contents)
### Wireframes
Before i started with anything else I made some wireframes to guide me through the design decisions. There has been some changes along the way, but the base structure is still the same.

![Home](/media/readme_images/home.png)
![Home](/media/readme_images/my_profile.png)
![Home](/media/readme_images/product_detail.png)
![Home](/media/readme_images/products.png)
![Home](/media/readme_images/shopping_bag.png)
![Home](/media/readme_images/checkout.png)
![Home](/media/readme_images/sign_in.png)
![Home](/media/readme_images/sign_up.png)
![Home](/media/readme_images/why_smart_locks.png)
![Home](/media/readme_images/why_contact_form.png)

[Back to top](#contents)
### Database
For this project I used a free database called [ElephantSQL](https://www.elephantsql.com/).
More about how to set that up in the deployment section.

There is five models in the database that I have created, along with a number that comes with Django from start.
- Products. A model for all the product details needed for a product.
- Category. Complements the product model and makes it possible to sort the products in to categories.
- UserProfile. Gives logged in user the possibility to save their delivery information and have it pre filled to the next time.
- Order. Stores all the order information. This is also presented to logged in user in their profile page.

Alot in these models comes from Boutique Ado Walkthrough Project at Code Institute. But I have made some changes to the models to suit my need better. Their is also some more validation and help texts added where needed.

![Database](/media/readme_images/database_schema.png)

[Back to top](#contents)
### Design
#### Typography
For this project I decided to stick with the standard font provided from bootstrap. I thought it looked like I wanted so there was no need to change it.

#### Colors
The colors used is combination of three main color. Two darker ones and a lighter one that is used as background on the page. I wanted a dark forest green look, so I chossed a color I liked and then used [Colormind](http://colormind.io/bootstrap/) to pick some matching colors.

![Colors](/media/readme_images/colors.png)

[Back to top](#contents)
## Features
### Existing Features For All Users
#### Navigation Bar
Here I wanted clear and simplistic look. A small logo to the left followed by some menu links. Products and Account have dropdowns for further menu choices.
To the right there is a search bar, followed by a link to the shopping bag. The shopping bag have a badge the quantity of ptoducts in the shopping bag. Below that there is a summary of the total amount in the shopping bag.

The search bar searches in the product name and in the description. With this amount of products it is not absolutely necessary, but it is a nice feature to have if there more products added to the shop. 

![Navbar](/media/readme_images/navbar.png)

[Back to top](#contents)
#### Home
When visiting the home page I wanted something clean but at the same time something that could sell. So i decided to go with a slideshow at the top with three pictures rotating. A mix of environment pictures and a made up "mechanical lock" that looks digital. Each slide have a diffrent quote with a link to the shop beneath. The quotes are hidden on smaller screens because it would not look good.

Beneath the slides there is three headings with icons. They have some short USPs and link to read more or to enter the shop.

Without scrolling further you get a picture of what the store sells and what kind of products that is offered.

![Home 1](/media/readme_images/home_1.png)

If you scroll down the page there is a nice picture of one of products on a door. It give a little bit of a luxury feeling around the product. To the left of the image there is a heading in two colors that shows that the product is available in two colors.

![Home 2](/media/readme_images/home_2.png)

[Back to top](#contents)
#### Footer
The footer have a copyright, a small logo and a form to subscribe to the newsletter. The newsletter form is connected to my mailchimp so emails entered there will be saved. 

![Footer](/media/readme_images/footer.png)

[Back to top](#contents)
#### Products
The products are divided in to three columns. Showing the picture, price, category, name and a link to the details page. It is possible to sort by name, category or price. There is not much use for this now, but it makes the shop future prof if there are more products added. There is also a pagination if there is more than six products.

![Products](/media/readme_images/product_page.png)

[Back to top](#contents)
#### Product Detail
This page shows a picture of the product, description, name, category and price. Then there is a option to choose quantity before adding it to the shopping bag. There is also a link back to the product list.

![Product detail](/media/readme_images/product_detail_page.png)

[Back to top](#contents)
#### Why Smart Locks?
This page gives some further information about smart locks and their benefits with a link to the contact page if there is some questions.
In a real business I think it should be a bigger page with more unique selling points and more information.

![Why smart locks](/media/readme_images/why_smart_locks_page.png)

[Back to top](#contents)
#### Contact
This page has a contact form that will send an email to the store owner. When submitted succesfully a message will show that confirms that mail have been sent.

![Contact form](/media/readme_images/contact_page.png)
![Thank you message](/media/readme_images/thank_you.png)

[Back to top](#contents)
#### Sign In
The sign in page is a standard page from allauth with some styling added to it.

![Sign in](/media/readme_images/sign_in_page.png)

[Back to top](#contents)
#### Sign Up
The sign up page have the same styling as the sign in page. The email confirmation is active so the user would need to enter a real email address. The form checks that the password is long enough and not too common. The username and email also has to be unique.

![Sign up](/media/readme_images/sign_up_page.png)

[Back to top](#contents)
#### Toasts
When adding a product to the shopping bag a message will show in the top right corner. This message is from bootstrap and is called a toast. If there is a error or other success message it will also show there, but without the shopping bag summary. This is so the user always knows what is happening.

![Toast](/media/readme_images/toast.png)

[Back to top](#contents)
### Existing Features For Store Owners
#### Add, delete and edit products


[Back to top](#contents)
#### Mark Order As Shipped


[Back to top](#contents)
#### All Reviews


[Back to top](#contents)
### Future Features
- Add discount cuopons would be a nice feature to have in the future.
-


[Back to top](#contents)
## Technologies Used
- [Django](https://www.djangoproject.com/) - A model-view-template framework used to create Locksmith Booking
- [Bootstrap](https://getbootstrap.com/) - A CSS framework used for the front end development.
- [HTML5](https://en.wikipedia.org/wiki/HTML) - Provides the content and structure for the website.
- [CSS3](https://en.wikipedia.org/wiki/CSS) - Provides the styling for the website.
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript) - Provides interactive elements of the website
- [Python](https://en.wikipedia.org/wiki/Python_(programming_language)) - Provides the functionality of the website.
- [a11y](https://color.a11y.com/Contrast/) - Used to test the contrast and accessibility.
- [Gitpod](https://gitpod.io/) - Used to create and edit the website.
- [GitHub](https://github.com/) - Used to host the repository.
- [GitBash](https://en.wikipedia.org/wiki/Bash_(Unix_shell)) - Terminal used to push changes to the GitHub repository.
- [Google Chrome DevTools](https://developer.chrome.com/docs/devtools/) - Used to test responsiveness and debug.
- [Balsamiq](https://balsamiq.com/) - Used to create the wireframes for the project.
- [Amazon AWS](https://aws.amazon.com/) - Used to host all static files and images.
- [Heroku](https://dashboard.heroku.com) - Used to deploy the website.
- [PEP8 Validation](http://pep8online.com/) - Used to validate Python code.
- [HTML Validation](https://validator.w3.org/) - Used to validate HTML code.
- [CSS Validation](https://jigsaw.w3.org/css-validator/) - Used to validate CSS code.
- [JSHint Validation](https://jshint.com/) - Used to validate JavaScript code.
- [drawSQL](https://drawsql.app/) - Used to draw the database schema.
- [Colormind](http://colormind.io/bootstrap/) - Used to chose colors.

[Back to top](#contents)
### Libraries
The following libraries are used in the project and are located in the requirements.txt file.


[Back to top](#contents)
## Testing
### Validator Testing
Locksmith Booking have been tested by using validation tools for HTML, CSS, JavaScript and Python.
- [W3C HTML Validator](https://validator.w3.org/)
- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)
- [JSHint JavaScript Validator](https://jshint.com/)

#### HTML Validation
![HTML](#)

#### CSS Validation
![CSS](#)

#### JavaScript Validation
![JS](#)

#### Python Validation
![Python](#)

[Back to top](#contents)
### Lighthouse Testing
The application has been tested with Chrome Dev Tools Lighthouse Testing which tests the application for:
- Performance
- Accessibility
- Best Practices
- SEO 

#### Home page
![Home](#)

#### About Page
![About](#)


[Back to top](#contents)
### Accessibility Testing
I checked so the contrast was enough on the site using [a11y](https://color.a11y.com/Contrast/).

![Contrast](#)

[Back to top](#contents)
### Responsiveness Testing
Test for responsiveness was made with [Google Chrome DevTools](https://developer.chrome.com/docs/devtools/).

[Back to top](#contents)
### Browser Testing


[Back to top](#contents)
### Manual testing


[Back to top](#contents)
## Bugs
### Solved
- When clicking on a category link under products, the products in that category won't show.
I solved this one by adding a split by "," to the category in the views.

- Submitting checkout form without country code on the phone number throws an error instead of a message.
This took me several hours, including a couple with tutor support. In the end it was an easy fix. It was a block that was indented wrong and inside an if-statement.

- Delivery costs become 34$ instead of 5$ after checkout.
I had made a mistake in the calculation of the grand total. It was total + total + delivery. The issue were fixed by removing one of the totals.

[Back to top](#contents)
### Left to Solve



[Back to top](#contents)
## Deployment
### Deployment to Heroku
This application is deployed using [Heroku](https://heroku.com/).

- Before doing the following steps I created a env.py file in gitpod that contains the sensitive information that should not be pushed to github/heroku. And added that file to the .gitignore file.
- Created a Procfile so Heroku knows what kind of application it is.
- Created a requirements.txt file with all the necessary requirements for the app to run.

The steps for deploying through [Heroku](https://heroku.com/) is as follows:

1. Visit [Heroku](https://heroku.com/) and make sure you are logged in.
2. Click on New and then choose New App.
3. Choose a name for your app and then choose your region.
4. Then press 'Create app'.

#### Attach The Database
1. Log in or sign up to [ElephantSQL](https://www.elephantsql.com/).
2. Press create new instance.

![Create new](media/readme_images/elephant1.png)

3. Choose a name and plan. Then click on select region.

![Name and plan](media/readme_images/elephant2.png)

4. Select the data center that is closest to you and press review.

![Data center](media/readme_images/elephant3.png)

5. Then just click on "Create Instance".
6. Go back to the start page and click on your new database.
7. Copy the URL for the database.

![Data center](media/readme_images/elephant4.png)

8. Back in [Heroku](https://heroku.com/) click on the settings tab of your application.
9. Click on "Reveal config vars".
10. Add a new config var named DATABASE_URL and paste in the URL from [ElephantSQL](https://www.elephantsql.com/) as the value.
11. Go back to Gitpod or other IDE and install two more requirements for the database:
    - `pip3 install dj_databse_url`
    - `pip3 install psycopg2-binary`
12. Update your requirements.txt file by typing in `pip3 freeze --local > requirements.txt`
13. Add the DATABASE_URL to your env.py file.
14. Go to settings.py and `import dj_database_url`
15. Comment out the default `DATABASES` setting.
16. Add this under the commented out section:

    ```
    DATABASES = {
        'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
    }
    ```
17. Run migrations for the new database.

#### Continue Deployment to Heroku
1. Create a file in the base directory called "Procfile" and add `web: gunicorn project_name.wsgi` so Heroku will know what kind of application it is.
2. In settings.py add ['app_name.heroku.com', 'localhost'] to `ALLOWED_HOSTS`.
3. Commit and push these changes to GitHub.

4. Back in the Heroku settings tab update the config vars:
    |     Variable name     |                           Value/where to find value                           |
    |:---------------------:|:-----------------------------------------------------------------------------:|
    | AWS_ACCESS_KEY_ID     | AWS CSV file                                                                  |
    | AWS_SECRET_ACCESS_KEY | AWS CSV file                                                                  |
    | DATABASE_URL          | In your ElephantSQL dashboard                                                 |
    | EMAIL_HOST_PASS       | Password from email client                                                    |
    | EMAIL_HOST_USER       | Email address                                                                 |
    | SECRET_KEY            | Random key generated with [Djecrety](https://djecrety.ir/)                    |
    | STRIPE_PUBLIC_KEY     | Stripe Dashboard > Developers tab > API Keys > Publishable key                |
    | STRIPE_SECRET_KEY     | Stripe Dashboard > Developers tab > API Keys > Secret key                     |
    | STRIPE_WH_SECRET      | Stripe Dashboard > Developers tab > Webhooks > site endpoint > Signing secret |
    | USE_AWS               | True                                                                          |

If you do this in the beginning of the project you will also need `DISABLE_COLLCETSTATIC` set to 1. When you have some staticfiles ready you can then remove this variable.

5. If this is at the end of the project make sure `DEBUG` is set to `False` in settings.py.
6. Go to the "Deploy" tab in Heroku and connect your GitHub account.
7. Search for your repository and connect it.
8. At the bottom of the page click "Deploy Branch".

![Heroku Deploy](media/readme_images/heroku-deploy.png)

9. You are now ready and can click "Open App" to see the live deployed version.


[Back to top](#contents)
### Forking the repository on GitHub
A copy of the repository can be made. This copy can be viewed and changed on another account without affecting the original repository.

The steps for doing this:
1. Make sure you are logged in on GitHub and then find the repository.
2. On the top right there is a button called Fork.
3. Press the Fork button to make a copy to your account.

![Image showing how to fork](#)

[Back to top](#contents)
### How to clone the project
This is how you make a clone of the repository:

1. Click on the code tab under the repository name.
2. Then click on "Code" button to the right above the files listed.
3. Click on the clipboard icon to copy the URL.

![Imge that shows where to find the URL for cloning](#)

4. Open Git Bash in the IDE of your choice.
5. Change the working directory to where you want your cloned directory.
6. Type `git clone` and then paste the URL that you copied.
7. Press enter and clone has been finished.

[Back to top](#contents)
## Credits
### Content
- [Bootstrap](https://getbootstrap.com/) is used alot in this project when adding the design to the front end.

[Back to top](#contents)
### Media


[Back to top](#contents)
## Acknowledgements


[Back to top](#contents)