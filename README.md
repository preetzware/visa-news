# VisaGlobal.News
<hr>
![VisaGlobal.News website Image]()

VisaGlobal.News is a full-stack web application that provides users with the latest news and updates on visas, airlines, travel advisories, and other travel-related topics. The project is built using the Django framework for the backend, with HTML, CSS, Bootstrap, and JavaScript powering the frontend, creating a seamless and responsive user experience.

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
    -   [Visa News Page](#user-account-and-user-account-listings)
    -   [Sign Up Page](#sign-up-page)
    -   [Log In Page](#sign-in-page)
    -   [Log Out Confirmation](#sign-out-confirmation)
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
The website features a calming and professional color palette that combines shades of blue, violet, and green with complementary neutrals. <br>
Overall, this color scheme creates a professional and user-friendly environment, with subtle variations in hue and transparency to guide users' attention and enhance the visual appeal of the website.
![Colour Scheme]()

### Database Schema
![database schema]()

#### Models
1. Allauth User Model

The User model is part of Django Allauth. The model comes with predefined fields as standard. Some of them are username, email, name, password, and more. This model is used for user authentication, hence why changes directly to this model are not advisory. The User model is connected to the Profile model with one to one relationship. 

2. visa_app(Home Page) Model

The Profile model is a custom custom-created model to handle the user profile details. Signals are used to reflect the changes between the User and Profile models. For example, if the Profile gets updated or deleted the changes will apply to the user model as well. 

3. Visanews Model

The listing model is connected to the Profile with a ForeignKey field - owner. It is furthermore connected to the CarMake and CarModel models via ForeignKey field again


### Fonts
The font used in this project is Roboto Slab, which compliments the design of the website. <br>
![Font]()





