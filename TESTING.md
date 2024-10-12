# Testing
- [Code Validation](#code-validation)
    - [HTML](#html)
    - [CSS](#css)
    - [JavaScript](#JavaScript)
    - [Python](#python)
- [Lighthouse](#Lighthouse)
- [Manual Testing](#manual-testing)
- [Responsiveness](#Responsiveness)
- [Browser Compatibility](#browser-compatibility)
- [User Story Testing](#user-story-testing)

## Code Validation
### HTML
|Page|Validator|Result|
| --- | --- | --- |
| Home Page |![home](./assets/testing-img/html-home.png) | <mark>PASS<mark> |
| Visa News Page |![listings](./assets/testing-img/visanews-html.png) | <mark>PASS<mark> |
| Sign Up Page |![Create Listing](./assets/testing-img/sign-up-html.png) | <mark>PASS<mark> |
| Log In |![Log In](./assets/testing-img/login-html.png) | <mark>PASS<mark> |
| Error pages |![home](./assets/testing/html-validator/404.PNG) | <mark>PASS<mark> |


### CSS
Test Results CSS  <mark>PASS<mark> 

![css-validator](./assets/testing-img/css-validation.png)

### JavaScript
1. like_dislike.js from home page articles <mark>PASS<mark> 

![like_dislike](./assets/testing-img/like-dislike-js.png)

2. comments.js from home page articles <mark>PASS<mark>

![comments.js](./assets/testing-img/comments-js.png)

3. visanews_like_dislike.js from Visa News page articles <mark>PASS<mark>

![visanews_like_dislike.js](./assets/testing-img/visanews-likes.png)

4. visanews_comments.js from Visa News page articles <mark>PASS<mark>

![visanews_comments.js](./assets/testing-img/visanews-comments.png)


### Python
1. visa_app (Home page)

- models.py <mark>PASS<mark>

![models](./assets/testing-img/visa-app-model.png)

- urls.py <mark>PASS<mark>

![urls](./assets/testing-img/visa-app-urls.png)

- views.py <mark>PASS<mark>

![views](./assets/testing-img/visa-app-views.png)

- admin.py <mark>PASS<mark>
![admin](./assets/testing-img/visa-app-admin.png)

- forms.py <mark>PASS<mark>

![forms](./assets/testing-img/visa-app-forms.png)

2. visa_news app (project app)
- settings.py <mark>PASS<mark> 

![settings](./assets/testing-img/project-settings.png)

- urls.py <mark>PASS<mark>

![urls](./assets/testing-img/project-urls.png)

- views.py <mark>PASS<mark>

![views](./assets/testing-img/project-views.png)

3. visanews app
- admin.py <mark>PASS<mark>

![admin](./assets/testing-img/visanews-admin.png)

- models <mark>PASS<mark>

![models](./assets/testing-img/visanews_model.png)

- views.py <mark>PASS<mark>

![views](./assets/testing-img/visanews_views.png)

- urls.py <mark>PASS<mark>

![urls](./assets/testing-img/visanews-urls.png)

- forms.py <mark>PASS<mark>

![forms](./assets/testing-img/visanews-forms.png)


## Lighthouse

|Page|Validator|Result|
| --- | --- | --- |
| Home Desktop |![home](./assets/testing/lighthouse/home-d.PNG) | <mark>PASS<mark> |
| Home Mobile |![home](./assets/testing/lighthouse/home-m.PNG) | <mark>PASS<mark> |


## Manual Testing
- Home Page 

|Section|Test Action|Expected Result|Pass/Fail|Comments|
| ---| ---| ---| ---| ---|
|Navbar|Click on logo in Navbar|Redirect to Home |Pass|Navbar present on all pages |
||Click on Home link in Navbar|Redirect to Home |Pass|Navbar present on all pages |
||Click on Listings link in Navbar|Redirect to Listings Page |Pass|Navbar present on all pages |
||Click on Create Listing link in Navbar|Redirect to Create Listing Page |Pass|Navbar present on all pages |
||Click on Profile link in Navbar|Redirect to My Profile Page |Pass|Navbar present on all pages |
||Click on Log Out link in Navbar|Redirect to Create Listing Page |Pass|Navbar present on all pages |
||Click on Login/Sign Up in Navbar|Redirect to Login Page |Pass|Navbar present on all pages |
|Hero section|Open Home page. Ensure the hero section loads as it should|Hero section loads as it should |Pass| |
|Search form|Open the Home page. Ensure the search form section loads as it should|Search form section loads as it should |Pass| |
||Click on each input field. Ensure all choices are loaded.|All input fields appear as they should. |Pass| |
||Search listings by a combination of filters. Ensure the results displayed are accurate with the search filters|All search results match the search criteria |Pass| |
||Select a max year. Ensure the min year cannot exceed the max year|All values of min year that exceed the max year are disabled |Pass| |
||Select min year. Ensure the max year cannot be less than the max year|All values of the max year that are below the min year are disabled |Pass| |
||Select max price. Ensure the min price cannot exceed the max price|All values of min price which exceed the max price are disabled |Pass| |
||Select min price. Ensure the max price cannot be less than the max price|All values of max price which are below min price are disabled |Pass| |
||Click on the search button. Ensure the user is redirected to the listings page|The user is redirected to the listings page with accurate results |Pass| |
|Recent Listings|Open the Home page. Scroll down to recent listings. Ensure the most recent listings are showing by comparing the time added stamp|The most recent listings are displayed |Pass| |
||Open the Create Listing page and create a listing. Ensure it shows as first in the most recent listings section |The added listing is displayed as most recent |Pass| |
|Listing Card| Click on the listing card. Ensure it redirects to the correct single listing page |When clicked each card redirects to the correct single listing page |Pass| |
|| Click on the listing card button. Ensure it redirects to the correct single listing page |When clicked each card button redirects to the correct single listing page |Pass| |
|| Go to the Create Listings page and create a new listing. Ensure the details displayed on the card are accurate |The information displayed on the card is accurate |Pass| |
|Pagination| Click on all of the links in the pagination. Ensure they redirect to the appropriate page. |All links redirect to the correct page. |Pass| |
|Pagination| Use the search form to search listings. Click on all of the links in the pagination. Ensure they redirect to the appropriate page displaying only the search results. |All links redirect to the correct page displaying the correct results. |Pass| |
|Footer|Click on all of the social links in the footer. Ensure each one opens the correct page in a new tab |All links open the correct page in a new tab |Pass| |


- Listings Page 

|Section|Test Action|Expected Result|Pass/Fail|Comments|
| ---| ---| ---| ---| ---|
|search form|||Pass|Tested on home page|
|listing card|||Pass|Tested on home page|
|Pagination| Click on all of the links in the pagination. Ensure they redirect to the appropriate page. |All links redirect to the correct page. |Pass| |
|Pagination| Use the search form to search listings. Click on all of the links in the pagination. Ensure they redirect to the appropriate page displaying only the search results. |All links redirect to the correct page displaying the correct results. |Pass| |
|Footer|Click on all of the social links in the footer. Ensure each one opens the correct page in a new tab |All links open the correct page in a new tab |Pass| |

- Single Listing Page 

|Section|Test Action|Expected Result|Pass/Fail|Comments|
| ---| ---| ---| ---| ---|
| Back button|Open the single listing page. Click on the back button. Ensure it sends you back to the previous page|When clicked the button brings you back to the previous page.|Pass||
|back button|Open the single listing page and the listing to favourites. Click on the back button. Ensure it sends you back to the previous page|When clicked the button does not bring you back to the previous page due to the fact the page reloaded|Fail|This is a known bug.|
|Images section|Click on the main image. Ensure it opens using Lightbox. Ensure arrows appear to navigate through the images|When clicked the images open using lightbox. Arrows appear on the sides and allow you to navigate through the images|Pass||
|Listing details|Ensure all the car specs are accurate with the details used when creating the listing. Ensure all icons display as they should|All icons display as they should, and the information is accurate.|Pass||
|Save to favourites button|Click on the heart icon. Ensure the page reloads, a flash message is displayed with confirmation and the icon changes to full heart|When clicked the page reloads, a flash message is displayed with confirmation and the icon changes to full heart|Pass||
||As not authenticated user, Click on the heart icon. Ensure the page redirects to the login page|When clicked the page redirects to the login page|Pass||
||As an authenticated user, open your listing. Ensure the favourites button does not appear|When visiting your listing the favourites button does not appear|Pass||
|Seller Card|Click on the seller's image. Ensure the link leads to the user's account profile|When clicked redirects to the user's account profile|Pass||
|Email Seller form|Click on the Email Seller button. Ensure a modal pops up with a form to fill in|When clicked, the modal pops up with a form to fill in|Pass||
||Click on the Email Seller button. Ensure The listing title field is populated and read-only. |The listing title field is populated and read-only.|Pass||
||As an authenticated user, ensure the form is prefilled with the user's details|When clicked, a modal pops up with pre-filled form fields for existing details like name and email.|Pass||
||Fill all fields with correct data in the expected format. Click send a message. Ensure an email has been sent with the details entered using a test email address |Email was received with accurate details|Pass||
||Fill all fields with correct data but one. Click send a message. Ensure the form is not submitted and an appropriate message is displayed. Repeat for all fields. |Form did not submit, the appropriate message was displayed|Pass||
|Description|Scroll to the description section. Ensure the accurate description is displayed |The accurate description is displayed|Pass||

## Browser Compatibility

|Browser|Result|Pass/Fail|Notes|
| --- | --- | --- | ---|
| Google Chrome | All pages, load as expected. All features work as expected | PASS | --- |
| Firefox | All pages, load as expected. All features work as expected | PASS | --- |
| Edge | All pages, load as expected. All features work as expected | PASS |



