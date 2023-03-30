# **Fore Golf**

![Responsive Image](/readme_images/responsive-image.png)

**[Link to the Deployed Site](https://p5-fore-golf.herokuapp.com/)**

---
## Project Overview

Fore Golf is a fictitious ecommerce full stack project built using Django, Python, JavaScript and Bootstrap 4. The site is deployed to Heroku, uses Amazon S3 for cloud storage and Stripe for payment processing. Fore Golf is a business to customer online retailer full of all types of golf equipment.

Fore Golf is my fifth milestone project for Code Institute's Level 5 Diploma in Full Stack Software Development.
<br/>

---
## Planning
### Balsamiq Wireframes
 
I created a Wireframe for this project to get a rough idea what my design idea for this project would look like using [Balsamiq - wireframes](https://balsamiq.com/). But I also created this so I could focus more on designing the actual website instead of having to think too much about how the design for this project would look while building the project.
Since the wireframes are an idea of how I think the website would look like before I started coding, the finished website isn't 100% look alike.

<details>
<summary>Wireframes</summary>

![home page](/readme_images/home-page-wireframe.png)
![product page](/readme_images/products-page-wireframe.png)
![product detail page](/readme_images/product-detail-wireframe.png)
![shopping bag page](/readme_images/bag-wireframe.png)
</details>

---
## Ux
### User Stories

As a guest I would like to be able to:
 
* As a Guest User, I find it easy to navigate the website.
* As a Guest User, I can register for an account using username, email, and password.
* As a Guest User, I can visit the website's social platforms.
* As a Guest User, I can visit the website's Facebook page.
* As a Guest User, I can view all of the products available.
* As a Guest User, I can view the individual details of a selected product.
* As a Guest User, I can purchase products using my credit/debit card.
* As a Guest User, I can contact the site owner.
 
As a registered user I would like to be able to:
 
* As a Registered User, I can login to my account.
* As a Registered User, I can log out of my account for security reasons.
* As a Registered User, I can see my order history, and change delivery information.
* As a Registered User, I can visit the website's social platforms.
* As a Registered User, I can visit the website's Facebook page.
* As a Registered User, I can view all of the products available.
* As a Registered User, I can view the individual details of a selected product.
* As a Registered User, I can purchase products using my credit/debit card.
 
As an admin I need to be able to:
 
* As an Admin, I can create, read, update and delete posts from the admin panel and the main website.
* As an Admin, I can see the entire list of products available.
* As an Admin, I can add products to the store.
* As an Admin, I can edit products.
* As an Admin, I can delete products.

### Strategy
 
#### Project Goal
Create a website for golf lovers around the world to purchase products. Also that it allows users to create an account so they can see order history, change shipping and billing information. Purchasing of products is of course open for all users even for those who aren't registered with an account.

### Scope
* A simple and straightforward UX experience. 
* A navigation bar that is easy to navigate the website with.
* A website that is compatible with most screen devices and browsers.

---
## Website Design
 
### Design
<details> 
<summary>Hero Image</summary>
<br>
I downloaded the background hero image from Google. I have used the hero image only on the home page of this project. The background color is set to black and if the background image wouldn't load the text would still be visible.
<br>

<br>

![Screenshot of hero image](/readme_images/hero-image2.png)
</details>

<details>
<summary>Navigation Bar</summary>
<br>
My navigation bar for this website is relatively clean, with just the most necessary text/buttons/search bar/menus to give the website an overall clean look.
<br>

![Screenshot of navigation bar](/readme_images/nav-bar.png)
</details>

<details>
<summary>Buttons</summary>
<br>
The design of the buttons on this website of course varies depending on the background and the surrounding (if the button is next to another button etc). Most of the buttons are green with white text, but some buttons are white with black text. Almost all buttons/links change their color when you hover over them giving them an effect that makes the user aware of clicking. 

![Screenshot of buttons](/readme_images/add-to-bag-btn.png)
![Screenshot of buttons](/readme_images/checkout-btn.png)

</details>

<details>
<summary>Footer</summary>
<br>
The footer holds the Newsletter, Contact link, social media links and privacy policy link.
<br>

![Screenshot of footer](/readme_images/footer.png)
</details>

<details>
<summary>Dropdown Menus</summary>
<br>
I choose to go for dropdown menus for "Products" and "My profile" as in the Code Institute - Boutique Ado Walkthrough Project.
<br>

![Screenshot of dropdown products](/readme_images/dropdown-products.png)
![Screenshot of dropdown profile](/readme_images/account-dropdown.png)
</details>

<details>
<summary>My Profile</summary>
<br>
My profile page is the same layout as in Code Institute - Boutique Ado Walkthrough Project, but with the correct color theme for this website. This page holds all the saved delivery information of the user (if the user has made purchases before) where the user can update the information and the page also lists order history with all orders made with that user account.
<br>

![Screenshot of profile page](/readme_images/my-profile.png)
</details>

<details>
<summary>Register/Login/Log out</summary>
<br>
The register, login, and logout pages hold the relevant input boxes for users to either create an account, log in, or log out. The styling for these is almost the same with the correct color scheme of the website.
<br>

![Screenshot of register page](/readme_images/sign-up.png)
![Screenshot of login page](/readme_images/sign-in.png)
</details>

<details>
<summary>Toasts (messages)</summary>
<br>
For each transaction made on the website, regardless of whether it is adding a product to the shopping bag or triggering an error the user/admin will get a message in the top right corner with the relevant information if the transaction was successful or not. The different toasts used are success, info, warning, and error with all of them wearing it's own color relating to the message. These toasts were taken as inspiration from the Code Institute - Boutique Ado Walkthrough Project.
<br>

![Screenshot of toast success](/readme_images/toast.png)
</details>

<details>
<summary>Shopping Bag pop-up</summary>
<br>
Every time when a user adds a product to the shopping bag or when a user removes a product from the bag the pop up appears. The user can use the button in this pop-up bag to get to the real shopping bag. This feature is taken as inspiration from the Code Institute - Boutique Ado Walkthrough Project but I have styled it to match the rest of this website.
<br>

![Screenshot of pop-up bag](/readme_images/pop-up-bag.png)
</details>

<details>
<summary>Shopping Bag</summary>
<br>
The shopping bag displays all the products that have been added to the bag, the quantity of each product, an update/remove quantity input, price, subtotal, bag total, grand total, and buttons for keep shopping more or secure checkout. This page is taken as inspiration from Code Institute - Boutique Ado Walkthrough Project but I have styled it to match the rest of this website.
<br>

![Screenshot of shopping bag](/readme_images/shopping-bag.png)
</details>

<details>
<summary>Checkout</summary>
<br>
The checkout page displays a form for submitting the delivery and billing information (this form can be pre-filled if the user is logged in and has saved past purchase info), an order summary that shows the products the user has added, quantity, subtotal, order total, grand total and buttons for either adjusting the bag if the user wants to add more products or remove products. The other button is to confirm the purchase. This page is taken as inspiration from the Code Institute - Boutique Ado Walkthrough Project but I have styled it to match the rest of this website.
<br>

![Screenshot of checkout page](/readme_images/checkout.png)
</details>

<details>
<summary>Checkout Success/Order Information</summary>
<br>
When the user has clicked the button to complete the order a new page will show up with the order information. This page displays order info, order details, delivery to, billing info, and a button for shopping for more products. A success message will show up on this page after the purchase was completed with information about the order. This page is taken as inspiration from the Code Institute - Boutique Ado Walkthrough Project but I have styled it to match the rest of this website.
<br>

![Screenshot of checkout success page](/readme_images/checkout-success.png)
</details>

<details>
<summary>Add/edit products</summary>
<br>
The pages for add/edit products/blog posts are almost the same in layout as CI - Boutique Ado, but they follow the color theme of this website. With a form for either adding or editing the related product.  
<br>

![Screenshot of add products](/readme_images/add-product.png)
![Screenshot of edit products](/readme_images/edit-product.png)

</details>

<details>
<summary>Delete products (Only admin/Store owner)</summary>
<br>
Only the admin/Store owner can delete products. Important to remember here is that when deleting, the action can not be undone! The buttons for this look like the images below.
<br>

![Screenshot of delete products](/readme_images/delete-product.png)
</details>

### Color Scheme
This palette has been selected to bring contrasting colours to improve accessibility to visually impaired users. As the aim of the site is to promote and sell golf equipment, white text on a green background is the primary colors. Green has been chosen as conventionally this represents where the game of golf is played, on grass.

![Screenshot of whigreente to white colors](/readme_images/color-pallette.png)

I created this color palette at [coolors.co](https://coolors.co/).

### Fonts

I choose two different fonts for my website, `"Kanit"` for my website name header and `"Maven Pro"` for all other text including all headings. I choose these two fonts because I thought they matched well together for this website. The fonts were taken from [pairfonts.com]().
 

---
## Features

### Profiles

User management is handled through the external package django-allauth. All user profiles are registered at Fore Golf's website when the user has verified the email address that was used when creating the account. When a user is doing a purchase at the store all the information the user filled into the checkout process will be saved to the user's profile (if the user leaves the "save info" checkbox as it is) for future purchases. 
The user will have access to a `My Profile` page where they can do the following:

* Edit their delivery information.
* View order history and click on an order number for past orders to view the details of that order.

### Products

All products are stored in a database within the product's app models. All products are stored with images, prices, descriptions, brands, degrees(if it has degrees), and their individual sku.  Admin/store owner can edit all products via the front end instead of going via the standard admin panel that is provided by Django. Admin/store owner can also add new products to the website via the `Product Managment` page. Each product can be clicked on for displaying the details of the selected product. Admin/store owner can also delete products from the website, but be careful because this action can not be undone.

### Newsletter

The newsletter app for this project is set up with [Mailchimp](https://mailchimp.com/), I decided to use Mailchimp because they have an already robust product with all sorts of templates for when signing up.

### Home

The home app holds the views for rendering the index page along with the header and footer. The home page is the page that the user will see first of all when visiting Fore Golf also called the "hero image" with a call to action button ('Shop Now) for the all products page. The contact us page allows users to contact the site owner directly.

### Checkout

The checkout app has all of the database models for `Order` and `OrderLineitem` to store orders for users. Even if a user who makes a purchase at the website isn't a registered user the order will be saved, and the admin/store owner can see it in the Django admin panel. The `Order` holds all of the order information and the `OrderLineItem` hold all the information about orders that have been made by a registered user, so users can see their history for previous orders. The checkout app also renders the checkout page and checkout success page.

### Bag

The bag app is for rendering the bag page template so the user can see all of the products that have been added to the shopping bag before checkout. Here the user can update the quantity via the `blue` update link of the selected products or remove products from the bag via the `red` remove link.

### Responsive Layout and Design

Using Bootstrap 4, the project has been designed to be fully responsive on most viewports, ensuring all functionality is maintained from 320px width and up. The targeted media queries are custom-made to make the website look good on most screen devices. All features have been developed with most viewports in mind.


---
## Marketing Strategy

The business model of `Fore Golf` is B2C (Business to Customer), this website sells golf products from all kinds of brands in a price range of €2 - €1,500.
The marketing aspect of Fore Golf has been done via creating a [FaceBook](https://www.facebook.com/profile.php?id=100088231741635) mockup page that you can take a look at. Creating a newsletter via [mailchimp](https://mailchimp.com/) for storing email addresses from users and visitors at `Fore Golf's` Mailchimp email list so we can send email campaigns to these subscribers like new products. I have added `rel` attributes to all external links on the website, added a `robots.txt` file and a `sitemap.xml` file, descriptive meta tags, and `alt` on all images.

The marketing strategy of Fore Golf is to send emails to our email subscribers.

### FaceBook page
![Screenshot of mockup facebook page](/readme_images/Facebook-mockup.png)

### Mailchimp
![Screenshot of mailchimps footer part](/readme_images/footer.png) 

### robots.txt
`Robots.txt` is a text file webmasters create to instruct web robots (typically search engine robots) how to crawl pages on their websites. The robots.txt file is part of the robots exclusion protocol (REP), a group of web standards that regulate how robots crawl the web, access, and index content, and serve that content up to users.

### sitemap.xml
An XML sitemap is a file that lists a website’s essential pages, making sure Google can find and crawl them all. It also helps search engines understand your website structure. You want Google to crawl every important page of your website. But sometimes, pages end up without internal links pointing to them, making them hard to find. A sitemap can help speed up content discovery.

### Privacy Policy
I have added an external link for `Fore Golf's` Privacy Policy, which I generated with a free online tool that you can check out [here](https://www.privacypolicygenerator.info/).

### Meta data
Meta data is included within the HTML head element to increase the traffic to the website.

---
## Technologies

The technologies that I used for `Fore Golf's` website project are the following down below.
 
### Languages
* HTML5
* CSS3
* Python
* JavaScript
 
#### Frameworks & Programs
 
* [Django](https://www.djangoproject.com/): Django is a high-level `Python web framework` that enables rapid development of secure and maintainable websites.
 
* [Bootstrap 4](https://getbootstrap.com/): Bootstrap is a `CSS framework and toolkit`. Developers can't use it to write programs, but because Bootstrap contains massive amounts of reusable code and website element templates, the framework can remove some of the “busy work” and significantly speed up the process of building a website.
 
* [GitHub](https://github.com): GitHub is used to store all data from the project after it has been pushed using the `git add . | git commit -m message here | git push` command in the GitPod terminal.
 
* [GitPod](https://www.gitpod.io): I used `GitPod` as my `IDE` which stands for `An integrated development environment (IDE) is a software for building applications that combines common developer tools into a single graphical user interface (GUI)`.
 
* `Git`: This is used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub. In case something unexpected happens to your gitpod workspace, everything is committed to your GitHub repository.
 
* [Heroku](https://www.heroku.com): Heroku is a container-based cloud Platform as a Service `(PaaS)`. Developers use Heroku to deploy, manage, and scale modern apps.

* [ElephantSQL](https://www.elephantsql.com/): I used ElephantSQL as my database for this project since Heroku has become a paid service only.

* [AWS](https://aws.amazon.com/): used to store media files.

* [Google Developer Tools](https://developers.google.com/web/tools/chrome-devtools) Used as the primary method for developing the sites         responsiveness and identifying bugs.

[PEP8ci](https://pep8ci.herokuapp.com/): This is a validation tool that was used to validate my python code.
 
* [Techsini](https://techsini.com/multi-mockup/index.php): Used to create the mockup image.
 
* [Font Awesome](https://fontawesome.com/): Was used to add icons to the site.
 
* [Balsamiq](https://balsamiq.com/): Balsamiq was used to create my wireframe for my design process.

* [Stripe](https://stripe.com/): Stripe was used for my checkout functionality in this project so visitors and users can make successful payments at the store.

* [Mailchimp](https://mailchimp.com/): Mailchimp was used for my newsletter.

* [Google](https://google.com/) . Unsplash was used for downloading all of the product images/blog images, and the hero image.

---
## Testing

---
## Deployment

**GitHub:**
 
I frequently used `commit` throughout the whole project, this is the command used in the terminal:
 
* `git add .` (This command is used for adding files to the staging area before committing).
* `git commit -m “commit message here..”` (This is used to label the commit changes made to the local repository).
* `git push` (This command is used to push all changes to the GitHub repository).
 
This is all done to prevent any `data` loss in case Gitpod crashes and saves the `data` to GitHub.
 
 
### GitHub & Gitpod
 
For this project, I used the Code Institute Python template.
 
**Steps to create a new repository in Github:**
 
1. Sign in or sign up to [GitHub](https://github.com).
2. When you have done that, you will see `"new"` up in the left corner.
3. Select in the dropdown menu under `Repository template` if you for example would like to use the template provided by `Code Institute` that I did for this project. Click `Use this template` to the left of the green Gitpod button.
4. When you have done that, give the repository a name. Leave it public if you want anyone on the internet to see your repository.
5. Click create a repository.
6. **Remember** to use the `commit` commands that I explained above so your hard work doesn't get lost if anything happens to Gitpod.
 
### Heroku
 
Deploying a project using Heroku:
 
* Don't forget to set your `DEBUG` in your `settings.py` file of your main app in `Django` to `False`.
* Ensure that all of your project dependencies are listed in the `requirments.txt` file.
* If not, then you can use this command in the Gitpod terminal: `pip3 freeze --local > requirments.txt`.
* Visit [Heroku](https://www.heroku.com) and click on create an account.
* Click the `"New"` button.
* Click the `"Create new app"` button.
* Provide a name for the app in the `App` name input field.
* Select your region from the `"choose region"` dropdown menu.
* Click the `"Create App"` button.
* Once redirected, proceed to the settings tab.
* Click on the `"config vars"` button.
* Supply a `KEY` of `PORT` and its value of `8000`. Then click the `"add"` button. Do this with `Database URL (from ElephantSQL), your secret key, AWS Keys, and Stripe keys`.
* Go to the deploy tab, once on the deploy screen, select GitHub as the deployment method and connect your GitHub profile.
* Search for the repository that you wish to deploy to `Heroku` and click `"connect"`.
* Once your repository is connected to Heroku you can choose to either automatically or manually deploy your app. 
* By selecting automatic deploy, Heroku will build a new version of the app each time a change has been made and pushed to the repository on `GitHub`.
* Click on manual deploy to build your App. When complete, click on `View` to open up the live site on `Heroku`. 
* Finished.

### ElephantSQL

Since `Heroku` now only offers paid plans for their service, the use of `ElephantSQL` exists as a free option for `Heroku Postgres`. For creating an `ElephantSQL` account these are the steps:

**Create an account:**

* Navigate to [ElephantSQL.com](https://www.elephantsql.com/) and click on `Get a managed database today` (green button).
* Then select `Try now for FREE` in the TINY TURTLE database plan.
* Select `Login with GitHub` and authorize ElephantSQL with your selected GitHub account.
* In the Create new team form:
  * Add a team name (your own name is fine)
  * Read and agree to the Terms of Service
  * Select Yes for GDPR
  * Provide your email address
  * Click “Create Team”
* Your account is now `successfully` created.
* Now you will need to create your database. Navigate to your elephantsql.com dashboard, and click `Create New Instance`.
* Set up your plan:
    * Give your plan a Name (this is commonly the name of the project).
    * Select the Tiny Turtle (Free) plan.
    * You can leave the Tags field blank.
* Select a data center near you.
* Then click `Review`.
* Check your details are correct and then click `Create Instance`.
* Return to the ElephantSQL dashboard and click on the database instance name for this project.
* You will return to this projects dashboard as part of the steps to `Deploy with Heroku` as you will need the DATABASE_URL.

### Amazon Web Services (AWS) Storage
Considering the development of the site could require a significant volume of product images, AWS has been used as the cloud host for imagery. To implement this you will need and AWS account and to create an S3 Bucket and User Profile. Developer guidance can be followed on AWS's site.

To serve the images you will need to add the following config to your settings.py file.

```
if 'USE_AWS' in os.environ:
    # Cache control
    AWS_S3_OBJECT_PARAMETERS = {
        'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
        'CacheControl': 'max-age=94608000',
    }
    # Bucket config
    AWS_STORAGE_BUCKET_NAME = 'the-coffee-collective'
    AWS_S3_REGION_NAME = 'eu-west-2'
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
    # Static and media files
    STATICFILES_STORAGE = 'custom_storages.StaticStorage'
    STATICFILES_LOCATION = 'static'
    DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
    MEDIAFILES_LOCATION = 'media'
    # Override static and media URLs in Production
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}'
```

---
## Credits

Support with how to develop ideas into code also came from various online resources, as well as using open source code. All these are documented below.

* In general the coding has relied on the Code Institutes walkthrough project "Boutique Ado".

* [W3schools](https://www.w3schools.com/) as a source of 'How to...' information throughout the build.
* [Stackoverflow](https://stackoverflow.com/)
* [Django Project Docs](https://docs.djangoproject.com/en/4.0/ref/models/fields/) were referenced many times, especially in how to reference fields correctly across differing python files.
* The [Bootstrap Documentation](https://getbootstrap.com/docs/5.0/getting-started/introduction/) was a big source of information when the styling of the website was created.
* **Google** for always clear things up.
* **Code Institute Slack channel** for always helping out with problems or questions.