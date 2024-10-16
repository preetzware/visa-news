# VisaGlobal.News

![Am I Responsive](./assets/readme-img/am-i-responsive.png)

VisaGlobal.News is a full-stack web application that provides users with the latest news and updates on visas, airlines, travel advisories, and other travel-related topics. The project is built using the Django framework for the backend, with HTML, CSS, Bootstrap, and JavaScript powering the frontend.

The website serves as a reliable news portal designed to bridge the gap between travel enthusiasts and the ever-evolving world of visa regulations and global travel. The platform offers categorized articles, an efficient search function, and interactive features such as commenting, liking, and sharing articles on social media—allowing users to engage with and stay informed about important travel news.

[Link to deployed site](https://visa-global-news-3e0847e1af66.herokuapp.com/)

[Link for Admin](https://visa-global-news-3e0847e1af66.herokuapp.com/admin/login/?next=/admin/)


# Table Of Content

-   [User Experience](#user-experience)
    -   [User Stories](#user-stories)
    -   [Site Goals](#site-goals)
    -   [Scope](#scope)
-   [Design](#design)
    -   [Colour Scheme](#colour-scheme)
    -   [Database Schema](#Database-Schema)
    -   [Fonts](#Fonts)
    -   [Wireframes](#Wireframes)
    -   [Agile Methodology](#Agile-Methodology)
         -   [Overview](#overview)
         -   [EPICS(Milestones)](#epicsmilestones)
         -   [User Stories issues](#user-stories-issues)
         -   [MoSCoW prioritization](#moscow-prioritization)
         -   [GitHub Projects](#github-projects)
-   [Website Features](#features)
    -   [Navbar](#Navbar)
    -   [Footer](#Footer)
    -   [Home Page](#Home)
    -   [Visa News Page](#visa-news-page)
    -   [Sign Up Page](#sign-up-page)
    -   [Log In Page](#log-in-page)
    -   [Log Out Confirmation](#log-out-confirmation)
    -   [Error Pages](#error-pages)
-   [Future Features](#future-features)
-   [Testing](#testing)
-   [Bugs](#Bugs)
-   [Technologies And Languages](#technologies-and-languages)
    -   [Languages Used](#languages-used)
    -   [Python Modules](#python-modules)
    -   [Technologies and programs](#technologies-and-programs)
-   [Deployment](#deployment)
    -   [Before Deployment](#before-deployment)
    -   [Deployment on Heroku](#deployment-on-heroku)
-   [Credits](#credits)
    -   [Media](#media)
    -   [Code](#code)
    -   [Acknowledgements](#acknowledgements)
    -   [Comments](#comments)

## User Experience

### User Stories

1. As a first-time visitor, I want to easily navigate the website and find the latest travel-related news.
2. As a user I want the website to be responsive so I can view it on my mobile.
3. As a user, I want to be able to read articles categorized by topics such as visa, airline, or travel advisory news.
4. As a user I want to be able to register an account so that I can interact and share my opinions on articles.
5. As a registered user, I want to be able to like or dislike and comment on articles that are relevant to my interests.
6. As a registered user I want to be able to log in to my account so I can view my comments and edit, update or delete them.
7. As a registered user I want to be able to like or dislike any articles.
8. As a user, I want to read articles and the comments made on them by other users.
9. As a user, I want to see the amount of likes an article has received.
10. As a user, I want to search for specific country, visa or travel-related topics to get relevant information.
11. As a user I want to be able to see visa news article list that displays the title, the image, the excerpt, the author name and date and time of the article. 
12. As an admin, I want to manage the publication of articles, moderate user comments, and monitor overall engagement on the platform.
13. As an admin, I want to approve or disapprove comments.
14. As a non-authenticated user, I want to be prompted to register when accessing the website's interacive functionalities that are available to registered users only.
15. As user, I want to browse articles through pagination.

### Site Goals
The main goal of VisaGlobal.News is to provide a reliable and up-to-date source of travel news and visa regulations. This includes:

1. Offering categorized articles for a diverse range of travel-related topics.
2. Facilitating user interaction through features such as likes, comments, and social media sharing.
3. Implementing a powerful search functionality that allows users to quickly locate relevant articles.
4. Ensuring that the website is mobile-friendly and easily accessible on all devices.

## Design
### Colour Scheme
The VisaGlobal.News website features a soothing and professional color palette that blends shades of black, white, and blue, complemented by neutral tones. This combination creates a visually appealing and modern aesthetic, enhancing readability while conveying a sense of trust and reliability. The calming blue tones evoke feelings of tranquility and professionalism, making it an ideal choice for a travel news portal. 

![Colour Scheme](./assets/readme-img/color-palette.png)

### Database Schema

![database schema](./assets/readme-img/schema_diagram.png)

The database schema for VisaGlobal.News has been designed to well define the structure of the project's database, which includes managing data types and relationships between different entities like articles, comments, users. This structure is essential for organizing your data effectively. The Models section below provides more details about the models themselves and their relationships. 

## Models

### 1. visa_app(Home Page) Model

The visa_app is designed to manage travel-related articles, allowing users to create, read, update, and delete content efficiently. The main models in this app include:

**Article:** Represents an individual article with attributes such as title, slug, author, excerpt, content, and published_at. It establishes a relationship with the User model, where each article is linked to a specific author. Additionally, it features many-to-many relationships for likes and dislikes, enabling user interactions. Articles can also be categorized using the Category model, which allows users to filter content based on specific topics.

**Category:** This model categorizes articles into distinct groups, making it easier for users to navigate through related content. Each category has a name and a slug for URL-friendly identification.

**Comment:** Users can comment on articles, and each comment is linked to both the Article it belongs to and the User who authored it. The approved field indicates whether a comment is visible to other users.

### 2. Visanews Model

The visanews app mirrors the functionality of visa_app but focuses on visa-related news articles. Its structure includes:

**VisanewsArticle:** Similar to the Article model, it contains fields such as title, slug, author, content, and published_at. It also includes relationships with the User model and the Category model. The many-to-many relationships for likes and dislikes facilitate user engagement.

**Category:** The Category model in visanews serves the same purpose as in visa_app, allowing articles to be grouped for easier access.

**Comment:** This model allows users to leave comments on visa news articles. Each comment is associated with a specific VisanewsArticle and the User who posted it. An additional parent field supports threaded comments, enabling users to reply to specific comments.

### 3. Allauth User Model

The User model is part of Django Allauth package and includes models such as EmailAddress, EmailConfirmation, SocialAccount, SocialApp, and SocialToken. These models help manage how users log in, including verifying their email addresses and connecting social media accounts. These models are linked to the User model, making sure that each user's email verification and social media account information are correctly associated with their profile.

### 4. Django's Built-in Models

- The schema encompasses various built-in Django models, including Group, Permission, ContentType, Session, as well as models from the django.contrib.auth and django.contrib.admin applications. 
- These models facilitate functionalities such as managing user permissions, handling session data, and providing information about content types.
- While the LogEntry model is utilized for monitoring administrative actions performed within the Django admin interface.

### 5. Permissions and Groups:

The Permission and Group models collaborate to regulate access within the application. Users can be placed in groups, and these groups can be granted specific permissions that determine what areas of the application they can access.


### Fonts
For the VisaGlobal.News website, I opted for a straightforward and professional approach to typography. In the Django admin interface, where I manage and add articles, I used Helvetica due to limited font family options. This font offers a clean, modern look that complements the overall design of the site.

For the titles, excerpts, footer, and rest, I leveraged the system UI font that comes built-in with Bootstrap, which allowed me to maintain a cohesive style without importing additional fonts like Google Fonts. This combination keeps the website clean, user-friendly, and consistent across different devices and browsers. <br>


### Wireframes
- Home Page
![Homepage Laptop & Desktop Size ](./assets/wireframes-img/web-fullscreen.jpg)

- ![Homepage Tablet & Mobile Size ](./assets/wireframes-img/tablet-mob-wf.jpg)

- Visa News Page
![Visa News Page](./assets/wireframes-img/visa-news-wf.jpg)

- Article_Detail Page
![Single Article Page ](./assets/wireframes-img/article-wf.jpg)

- Sign Up Page
![Sign Up Page](./assets/wireframes-img/signup-wf.jpg)

### Agile Methodology
#### Overview
I created my project using agile principles which presented a significant learning curve, especially as it was my first experience developing a full-stack application. The Agile approach provided structure and flexibility, allowing me to plan and prioritize the website's features through detailed user stories. Each story had well-defined acceptance criterias, which ensured that the requirements for each feature were clearly understood and met during development. This method helped streamline the process and maintain focus on delivering functional and user-friendly features.

It is worth-mentioning that during the development of my project, I adjusted my user stories and acceptance criterias to prioritize the 'must-have' requirements. Initially, I had also planned to implement additional features like a "forgot password" option, "popular posts," and a "subscribe to newsletter" functionality. However, as I faced numerous errors while trying to incorporate these features, I decided to leave them out to focus on completing the core functionality without significant delays.

#### EPICS(Milestones)
The user stories are organized into eight EPICS or Milestones. Additionally, a Milestone named "Project Backlog" was created to track any extra features, bugs, or uncompleted tasks that emerged during the development process. <br>
![Milestones](./assets/readme-img/milestones.jpg)

#### User Stories issues
The structure of each user story issue consists of the user story itself, followed by acceptance criteria that define the specific requirements that must be met for the feature to be considered complete. These criteria serve as a clear guideline for testing and validating the functionality of the feature, ensuring it aligns with the user's needs and expectations. <br>
![User Story](./assets/readme-img/user-story.jpg)

#### MoSCoW prioritization
The MoSCoW prioritization technique was employed to efficiently rank the project’s features and requirements based on their significance. "MoSCoW" stands for "Must have, Should have, Could have, and Won't have," with each category helping to organize and prioritize features. This approach guided the development process, ensuring that the most essential elements were addressed first. <br>
![User Story](./assets/readme-img/moscow-prioritization.jpg)

#### GitHub Projects
For the development of the project, I made use of a simple Kanban Board structure, organized into columns like To Do, In Progress, Done, and Backlog. This layout offered a clear, efficient way to track task progress while helping to visualize and manage the workflow effectively. <br>
![User Story](./assets/readme-img/projectboard.jpg)

## Features
### Navbar
The navbar, a consistent feature across all pages, was built using Bootstrap with custom modifications to ensure full responsiveness. The VisaGlobal.News logo, created via [logodesign.ai website](https://www.logodesign.ai), is positioned on the left and functions as a link to the homepage. On the right, there are navigation links that allow users to move easily throughout the website. If a user is not authenticated, the links displayed include Home, Visanews, Signup, Login and the search icon. The search icon reveals a search bar and a "Go" button when clicked, enabling users to search for articles on both the Homepage and Visa News page. The search view has been designed using metrics such as article titles, excerpts, and categories to enable users to efficiently find relevant articles. By leveraging these key elements, users can quickly identify content that meets their interests, enhancing their overall experience on the platform.

![Unauthenticated User's nav view](./assets/readme-img/unauthen-navbar.png)

 If the user is authenticated, they will see navigation links for Home, Visa News, Log Out, along with a personalized greeting, "Hi (username), you're logged in!" and the search icon. To enhance user experience, the active navigation link is underlined with a border, providing a visual cue to indicate the page the user is currently viewing.

 ![Authenticated User's nav view](./assets/readme-img/authenticated-navbar.png)

 ### Footer
 The footer is divided into three sections: **About**, which provides an introduction to VisaGlobal.News; **Our Contact**, which presents the contact details; and **Connect with Us**, which features social media icons and links that allow users to connect with VisaGlobal.News by opening the links in a new tab.

 ![Footer](./assets/readme-img/visanews-footer.png)

### Home

The home page consists of the carousel section which has been incorporated to showcase the three most recent news articles, providing users with quick access to the latest updates. Additionally, a fourth story is positioned adjacent to the carousel, ensuring that visitors can easily discover important content at a glance. Below this section, three article cards feature the other latest visa news.

 ![Homepage](./assets/readme-img/home-page.jpeg)

### Visa News Page
The Visa News page contains three pages of article cards, each with pagination for easy navigation.

![Visa News Page](./assets/readme-img/visa-news-page.jpeg)

### Article_detail Page
![Visa News Page](./assets/readme-img/article-page.jpeg)

### Sign Up Page

![Sign Up Page](./assets/readme-img/sign-up-page.png)

#### Flash Messages
Flash messages are used to give users feedback whenever they perform CRUD operations or during the sign-in and sign-out processes. These messages notify users about the success or failure of their actions, improving the overall user experience.

![Signed-in message](./assets/readme-img/sign-in-flash.png)

![logout message](./assets/readme-img/logout-flash.png)

![After submitting comment message](./assets/readme-img/comment-approval-msg.jpeg)

![After editing comment message](./assets/readme-img/edit-comment.jpeg)

![After comment deleted](./assets/readme-img/comment-deleted-msg.jpeg)


### Login page
Consist of a form with username and password. 
![Log In](./assets/readme-img/login-page.png)

### Sign Up page
The sign-up process features a form that includes fields for the user's email, username, password, and password confirmation. There is also a link for users who already have an account to log in. At the bottom of the form, a sign-up button allows users to submit their information. Once signed up, users are automatically logged in and redirected to the homepage.

![Sign Up](./assets/readme-img/sign-up-page.png)

### Sign out confirmation
When the user clicks the logout link in the navigation bar, a modal with a warning message pops up. It also features two buttons: one to close the modal and stay on the actual page and another to proceed with logging out.

![log out confirmation](./assets/readme-img/logout-modal.png)

### Edit Comment
Editing comment can be done in the text field below the article once the user clicks on the edit button. Once submitted, a flash message will display. 

![Edit Comment](./assets/readme-img/edit-comment.jpeg)

### Delete Comment Confirmation
When user clicks on delete button below their comment, a warning message appears with options to delete or to close window.

![Delete Comment](./assets/readme-img/delete-confirmation.png)

### Error Pages
- 404
![404](./assets/readme-img/400-error.jpg)

- 403
![403](./assets/readme-img/403-error.png)

- 500
![500](./assets//readme-img/500-error.png)

## Future Features
1. User Profiles and Personalization:

Implement user profiles where users can save their favorite articles, set preferences for topics, and receive personalized content recommendations based on their reading history and interests. This could also include a dashboard that shows users their reading activity, liked articles, and comments.

2. Newsletter Subscription:

Add a newsletter subscription feature that allows users to sign up for regular updates about the latest articles, travel advisories, and visa regulations. This feature could include customizable options for users to choose the frequency and types of updates they wish to receive.

3. Multilingual Support:

Incorporate multilingual support to make the website accessible to a wider audience. This feature would allow users to select their preferred language for content, making the site more inclusive and user-friendly for non-English speakers.

## Testing
Testing documentation can be found [here.](TESTING.md)
 
## Bugs
#### **Fixed Bugs** ####

1. **URL conflict issues**  
   During the development process of my project, I experienced a bug with a URL conflict, and had to update the urlpattern in visa_app/urls.py to resolve it. 

2. **Filepath issues leading to 404 errors**  
   During the development of the project, I had encountered several filepath issues that caused 404 errors. These errors occurred when URLs didn't point to the correct files or resources, making parts of the website inaccessible. To resolve these, had to carefully check and adjust the paths, ensuring they matched the expected structure within the project. Handling these errors was a key aspect of the debugging process, as it ensured that the website could correctly load resources like images, CSS files, and templates without issues.

3. **Javascript: Like and dislike buttons not functioning**  
   At two points, I had encountered JavaScript issues where the like and dislike button counts were not functioning correctly. This issue stemmed from an error in the JavaScript code handling the button clicks, and also due to incorrect targeting of the DOM elements and issues with how the data was being sent and received from the server. Debugging this required inspecting the JavaScript logic, checking the view responses, and ensuring that the like/dislike count dynamically updated without page reloads. Resolving this improved user interaction on the website and allowed proper functionality for these features.

4. **Search functionality results**  
   During development, I encountered an issue where the search functionality only returned results from the visa_app, excluding the articles from the visanews app. This was a result of the search view being limited to one app. To resolve this, I had to adjust the views to ensure they queried articles from both apps—visa_app and visanews. This involved modifying the search logic to combine the search results from both models and ensuring that titles, categories, and excerpts were matched across both apps, allowing for comprehensive search results across the entire site.

5. **Styles not reflecting on deployed website**  
   A few times I had this issue where I applied some styles that would not reflect on the deployed website. After debugging, I realized it was due to not running `collectstatic` in the terminal to collect the latest CSS changes. After making CSS changes and running this command, this issue was completely resolved.

6. **Like and Dislike Buttons not Functioning**  
   At one point, stylesheet changes were not appearing even after refreshing the page. The solution was setting `DEBUG = True`, which allowed the changes to be reloaded correctly.

7. **Edit and Delete buttons functionality for comments**  
    I faced issues with the functionality of the "edit" and "delete" buttons for comments. Despite appearing correctly in the user interface, clicking them did not trigger the expected actions. The root cause was found in the views responsible for handling these actions. Specifically, the views were not receiving the correct comment ID, and the URLs were incorrectly mapped. To resolve this, I had to inspect both the views and the template files, ensuring that the comment ID was properly passed from the template to the view and that the correct URLs with trailing slashes were being used. This adjustment helped direct the forms correctly, allowing the views to process the requests properly. Once these fixes were applied, the buttons began functioning as intended, enabling users to edit or delete their comments.

8. **Code validation issues**  
    I encountered several code validation issues that needed to be addressed to ensure the site's functionality, accessibility, and performance. These issues spanned across HTML, Python, and JavaScript files, and required thorough validation and debugging to resolve. Here's an overview of the challenges and fixes:

- HTML Validation
I used tools like the W3C Markup Validation Service to validate my HTML files, which helped identify various errors, including:

Unclosed or misplaced tags, Missing alt attributes on images,Deprecated attributes and elements, Duplicate IDs.
Python Validation

- Python Validator
To validate my Python code, I used CI Python linter. Common issues included:

Indentation errors: Python relies on proper indentation, and I found several cases where my code had inconsistent spacing (mixing tabs and spaces). I corrected these errors to ensure consistent indentation throughout.
Unused imports and variables: I encountered warnings about importing libraries that were not being used or declaring variables that never got referenced. I removed the unused imports and variables to clean up the code.
Long lines and function complexity: PEP8 recommends keeping line lengths under 79 characters and reducing the complexity of functions. I refactored long lines into multiple shorter lines and broke complex functions into smaller, more manageable ones.

- JavaScript Validation
For this, I used JSHint and I validated my JavaScript files and fixed issues, including:

Missing semicolons, Undefined variables, Outdated or inefficient code.

All of these issues were resolved successfully.

 ### **Unfixed Bugs** ###

 **Mixed content warnings in Console**
 
 1. I encountered persistent "Mixed Content" warnings in the browser console, specifically related to Cloudinary images. Despite ensuring that the image URLs used in your project were served over HTTPS, the warnings continued to appear. Mixed content warnings generally occur when a secure HTTPS page attempts to load resources (like images or scripts) over an insecure HTTP connection. Even though your Cloudinary URLs seemed to be correctly prefixed with HTTPS, the browser still flagged the requests as insecure.

 **Uncaught TypeError: Cannot read properties of null (reading 'value') in like_dislike.js in console**

 2. This error occurred in the like_dislike.js file and is typically caused when the JavaScript tries to access an element with a specific id that does not exist on the page at the time of execution. The issue points to a missing element that the script is trying to interact with. Even though I tried changing the element's id, the error persisted.


## Technologies And Languages
### Languages Used
- HTML
- CSS
- JavaScript
- Bootstrap
- Python
- Django

### Python Modules

- gunicorn - Gunicorn is a popular WSGI (Web Server Gateway Interface) HTTP server for running Python web applications, including Django applications, in a production environment.

- psycopg2 - Psycopg2 is a PostgreSQL adapter for Python. It allows Django to connect to PostgreSQL databases.

- whitenoise - Whitenoise is a middleware for serving static files directly from your Django application.

### Technologies and programs
 - [Favicon Generator](https://www.favicon.io/) was used to generate Favicon
 - [GitHub](https://github.com/) is the hosting site used to store the code for the website.
- [Code Institute Template](https://github.com/Code-Institute-Org/gitpod-full-template) was used as a starting point for the project.
- [Google Fonts](https://fonts.google.com/) was used to import fonts.
- [Google Chrome Lighthouse](https://developers.google.com/web/tools/lighthouse) was used during the testing of the website.
- [Google Chrome Developer Tools](https://developer.chrome.com/docs/devtools/overview/) was used during testing, debugging and making the website responsive.
- [W3C HTML Validator](https://validator.w3.org/) was used to check for errors in the HTML code.
- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) was used to check for errors in the CSS code
- [Js Hint](https://jshint.com/) was used to validate the JavaScript code.
- [CI Python Linter](https://pep8ci.herokuapp.com/) was used to validate the Python code.
- [Image Convert](https://tinypng.com/) used to convert images to webp format
- [Coolors.co](https://coolors.co/) was used to display the colour scheme.
- [Logo Design](https://www.logodesign.ai) was used to create the website's logo.
- [Wireframes](https://balsamiq.com/) was used to create the website's wireframes.
- [Debugging] - (https://www.chatgpt.com) was used for troubleshooting and debugging.

## Deployment
### Before Deployment
To ensure the application is correctly deployed on Heroku, it is essential to update the requirements.txt file. This file contains a list of dependencies that the application requires to operate.

- To generate the list of requirements, use the command pip3 freeze > requirements.txt. This will update the file with the necessary dependencies.
- After that, commit and push the changes to GitHub.

**Important:** Before pushing code to GitHub, make sure that all sensitive credentials are stored in an env.py file, which should be included in the .gitignore file. This instructs Git not to track the file, preventing it from being uploaded to GitHub and exposing your credentials.

### Deployment on Heroku
- To deploy the project on Heroku, you must first create an account.
- Once logged in, create a new app by clicking the "Create App" button.
- Choose a unique name for your app, select a region, and then click "Create App."
- On the following page, navigate to the "Settings" tab and scroll down to the "Config Vars" section. Any sensitive files, such as credentials and API keys, should be added here. For this project, the following credentials need to be secured:
1. Django's secret key
2. Database credentials
3. AWS access key
4. AWS secret key

- Scroll down to the "Buildpacks" section. The buildpacks will install additional dependencies that are not included in the requirements.txt. For this project, you need the Python buildpack.
- From the tabs above, select the "Deploy" section.
- The deployment method for this project is GitHub. After selecting it, confirm the connection to GitHub, search for your repository name, and click "Connect" to link your Heroku app with your GitHub code.
- Scroll down to the deploy section where you can enable automatic deploys, meaning the app will update every time you push code to GitHub. Click "Deploy" and wait for the app to build. Once completed, a message should appear indicating that the app has been successfully deployed, along with a button to view the app.

## Credits
- [Travelobiz Website](https://travelobiz.com/)
- [Visaguide.News](https://visaguide.world/news/)
- [Stack Overflow](https://stackoverflow.com/)
- [Django documentation](https://docs.djangoproject.com/en/5.1/)
- [OpenAI's ChatGPT](https://chatgpt.com/)
- [Freepik](https://www.freepik.com/)

### Acknowledgements
- I would like to give special credit to Code Institute's "I Think Therefore I Blog" Django walkthrough project. The knowledge and guidance from this walkthrough were instrumental in helping me understand and implement the concepts needed to bring my VisaGlobal.News project to life.
- A heartfelt thank you to my cohort facilitators, Amy and Lewis, for their unwavering support and guidance throughout this journey.
- I am grateful to my mentor, Harry Dhillon, for his valuable feedback and insightful guidance while reviewing my project.
- A special mention goes to my friend, Brian McConway, for his advice and encouragement during the development process.
- Lastly, I want to express my deep appreciation to my husband and toddler for their support, which allowed me to dedicate the necessary time to complete this project while maintaining a healthy balance.

### Comments
This project consists of two primary apps: the homepage and the Visa News page. Both apps manage user interactions, such as commenting, liking, disliking, and searching for articles. They also handle the full range of CRUD functionalities, allowing users to add, delete, and interact with comments on articles, including the ability to like or dislike articles as well.
In addition, Users have the option to share articles via different social media platforms using the icons provided below the article excerpts, allowing for easy content sharing.

Besides, the search feature enables users to retrieve articles from both pages, regardless of which page they initiate the search from, ensuring a seamless user experience.

Although I had planned to include automated testing, I ran out of time during development. This is a feature I aim to implement in the future, as it will help me maintain the project more efficiently and confidently as I continue to add more functionality.