
## Manual Testing
### Testing User Stories
### **User Stories**
| **User Story #** | **As a/an** | **I want to be able to...** | **So that I can...** | **How was this achieved** | **PASS/FAIL**
| :-- | :-- | :-- | :-- | :-- | :-- |
| **VIEWING & NAVIGATION** |  |  |  |  |  |
| 1 | Shopper | Navigate around the site | View a list of products | The navbar's main navigation component allows the shoppers to browse for products. The all products link from the main navigation enables the visitors to view the list of all the products available on the site. | PASS
| 2 | Shopper | View a specific category of products | Quickly find products I'm interested in without having to search through all products. | The site's main navigation component allows the shoppers to browse for specific category of products. | PASS
| 3 | Shopper | View individual product details | Identify the price, description, product reviews, product image, product ingredients and instructions how to use product | A shopper is taken to the product detail page after clicking on a product image or the shop now button from an individual product card. The product detail page displays the product information such as name, image, brand, category, price and description. | PASS
| 4 | Shopper | Easily view the total amount of products in my shopping bag at any time throughout my visit | Avoid spending too much | Whenever a product is added to the shopping bag, a toast will display confirming that the product was indeed added to the bag successfully and also shows how much a shopper needs to spend to reach the free delivery threshold (if not yet reached). Below the bag icon, the running total of the items currently in the bag is displayed and the user can navigate across the different pages on the site and still be able to view the current amount in the bag. | PASS
| 5 | Shopper | Search/ View all of the available *Fore Golf brands | Look for my favourite brands | From the main navigation, the shoppers are able to click on **All Products** navlink and it will open the brands dropdown where all available brands are listed. | PASS
| 6 | Shopper | View a list of available products when viewing a brand | Quickly decide what product to purchase from a particular brand | On the brand page, the shoppers are able to view the list of available products from any brand. | PASS
| :-- | :-- | :-- | :-- | :-- | :-- |
| **REGISTRATION & USER ACCOUNTS** |   |   |  |  |
| 7 | Shopper | Easily register for an account | Have a personal account and be able to view my profile | Shoppers are easily able to create an account via the site's top navigation which has the My Account icon. This icon has two dropdown links, the first of which is the Sign Up. Clicking the Sign Up link opens the site's sign up page where they can then register to create an account. Alternatively, shoppers who do not yet have an account with the site can also create an account from a link at the checkout page. | PASS
| 8 | Shopper | Easily login and logout of my shopper's account | Access my personal account information | Via the top navigation (My Account), users are able to easily login and logout of their shopper's account. Successful log in is confirmed by toast. Once logged in, the shoppers are able to access their personal information, again via the My Account dropdown that displays two options for the user, My Profile and Logout. The My Profile link opens up the logged in user's personal profile page where they can view and edit their default delivery information. The shopper's order history is also displayed, ready for the shopper to review via the order number link. | PASS
| 9 | Shopper | Have a personalised user profile | View my personal order history and order confirmations | A logged in user, via their profile page, has access to their order history, arranged chronologically. The order confirmations are accessible from the Order Number links. | PASS
| :-- | :-- | :-- | :-- | :-- | :-- |
| **SORTING & SEARCHING** |   |   |  |  |
| 10 | Shopper | Sort the list of available products | Easily identify the best priced, brand and categorically sorted products | Using the sort selector in the products page, users are able to sort all the available products by price, category and brand. | PASS
| 11 | Shopper | Sort a specific category of product | Find the best priced product in a specific category | From the main navigation, the users can select a specific category of products, for example eye care category. The users can also user the sort selector on the products page to sort a specific category (same example, eye care category). Using the same selector, the user can further sort the results to find the best priced product. | PASS
| 12 | Shopper | Search for a product or products by name, by description or by brand | Find a specific product I'd like to purchase  | Per the placeholder text on the search bar, users can search for a product by name, description or by brand. | PASS
| 13 | Shopper | Easily see what I've searched for and the number of results | Quickly decide whether the product I want is available | Using the examples for user story #23 above, when users search for a product by name, description or brand, the results also include the number of products found. | PASS
| :-- | :-- | :-- | :-- | :-- | :-- |
| **PURCHASING & CHECKOUT** |   |   |  |  |
| 14 | Shopper | Easily select the quantity for a product when purchasing it | Ensure I don't accidentally select the wrong product quantity | From the product detail page as well as from the shopping bag, shoppers are able to adjust the quantity of items prior to checking out. In both instances, users are also only able to increment or decrement the item quantity by a whole number. | PASS
| 15 | Shopper | Easily view notifications on screen when I add a product to my bag | Find out immediately if my actions were correct or if the was an error | A toast message appears whenever a user adds a product to the shopping bag. An error notification also appears if a user increases the product quantity using a float number, as an example. | PASS
| 16 | Shopper | View items in my bag to be purchased | Identify the total cost of my purchase and all items I will receive | From the shopping bag page, shoppers are able to view the items they are planning to purchase including the cost per item, the bag total, the delivery fee (if they have not met the free delivery threshold) as well as the grand total. | PASS
| 17 | Shopper | Adjust the quantity of individual items in my bag | Easily make changes to my purchase before checkout | From the bag page, shoppers are still able to adjust the quantity of the items in their shopping bag, including even removing the item. A toast will appear notifying the shopper whether an item quantity has been updated or if an item has been removed from the bag. | PASS
| 18 | Shopper | Easily enter my payment information | Check out quickly and with no hassles | On the checkout page, shoppers are able to see the information they need to provide to check out quickly, including which information are required. These are their full name, email address, phone number, street address1, town or city and country. They can also see the payment information required such as their card number, month and year of card expiry and the CVC. Errors in logging in the wrong information such as a credit card already expired is dealt with by an error message displayed to the shopper. | PASS
| 19 | Shopper | Feel my personal and payment information is safe and secure | Confidently provide the needed information to make a purchase | Fore Golf's payments processing is powered by Stripe. Stripe is a suite of APIs powering online payment processing and commerce solutions for internet businesses of all sizes. | PASS
| 20 | Shopper | View an order confirmation after checkout | Verify that I haven't made any mistakes | After a successful checkout, shoppers are taken to an order confirmation page to thank them for their purchase. The page displays their order information, their order details, the delivery information and the billing info. A toast also appears notifying the shopper that the order has been successfully processed and that an email confirmation is on it's way. | PASS
| :-- | :-- | :-- | :-- | :-- | :-- |
| **ADMIN & STORE MANAGEMENT** |  |  |  |  |
| 21 | Store Owner | Add a product | Add new items to my store | The logged in store owner is able to add a product to the store directly from the product management page. The product management page can be accessed by clicking the **My Account** icon in the top navigation component of the navbar. The icon displays several dropdown links, one of which is **Product Management** | PASS
| 22 | Store Owner | Edit/update a product | Change product process, descriptions, ingredients, images and other product criteria | The logged in store owner is able to edit a product directly in the store using the **Edit Product** button on the product detail page. This button is only displayed to authenticated store owner/ admins and links directly to the product management page. The product management page (edit a product) is exactly the same as the product management page (add a product). The product information is pre-populated. A toast also appears providing an alert that a specific product is being edited. | PASS
| 23 | Store Owner | Delete a product | Remove items that are no longer for sale | The logged in store owner is able to delete a product directly in the store using the **Delete Product** button on the product detail page. This button is only displayed to authenticated store owner/ admins. To prevent unintended deletion, a modal pops up a warning that such action will delete the product forever if they continue. The option to **cancel** and **delete** buttons are also included in the modal. | PASS
| 24 | Store Owner | Have a privacy policy on the site | Be assured that all the legalities of doing business online are taken care of | The Privacy Policy can be accessed from their respective links in the footer. | PASS
| 25 | Store Owner | Receive a warning if I accidentally click the delete a product button | Avoid accidental deletion of a product | To prevent unintended deletion, a modal pops up a warning that such action will delete the product forever if they continue. The option to **cancel** and **delete** buttons are also included in the modal. | PASS
| 26 | Store Owner | Add a brand to my store | Add new products even if the product's brand is not in the store yet | The logged in store owner is able to add a brand to the store.  | PASS
| :-- | :-- | :-- | :-- | :-- | :-- |
| **DIGITAL MARKETING** |   |   |  |  |
| 27 | Store Owner | Have a social media presence | Create awareness of Fore Golf products | From the footer section, the links to social media sites such as Facebook and Instagram are included. A Facebook page for Fore Golf is also created as an example of having a social media presence. | PASS


## Validation
### HTML Validation

I used [W3C Markup Validation Service](https://validator.w3.org/) to validate all the HTML files by direct input, you can find my results below:

<details>
<summary>Home Page</summary>
<br>

![Home](/readme_images/home-page.png)
</details>

<details>
<summary>All Products Page</summary>
<br>

![All Products](/readme_images/all-products-page.png)
</details>

<details>
<summary>Product Detail Page</summary>
<br>

![Product Detail](/readme_images/product-detail-page.png)
</details>

<details>
<summary>Shopping Bag Page</summary>
<br>

![Shopping Bag](/readme_images/shopping-bag-page.png)
</details>

<details>
<summary>Checkout Page</summary>
<br>
There is one warning here due to an empty h1 element, however it does have an icon within the element so I ignored this warning.

![Checkout](/readme_images/checkout-page.png)
</details>

<details>
<summary>Checkout Success Page</summary>
<br>

![Checkout Success](/readme_images/checkout-success-page.png)
</details>

<details>
<summary>Register Page</summary>
<br>

![Register](/readme_images/register-page.png)
</details>

<details>
<summary>Login Page</summary>
<br>

![Login](/readme_images/login-page.png)
</details>

<details>
<summary>Profile Page</summary>
<br>

![Profile](/readme_images/profile-page.png)
</details>

<details>
<summary>Add Product Page</summary>
<br>

![Add Product](/readme_images/add-product-page.png)
</details>

<details>
<summary>Edit Product Page</summary>
<br>

![Edit Product](/readme_images/edit-product-page.png)
</details>

***
### CSS Validation

I used [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) to validate all the CSS files by direct input, you can find my results below:

<details>
<summary>Base CSS</summary>
<br>

![base.css](/readme_images/base-css-val.png)
</details>

<details>
<summary>Checkout CSS</summary>
<br>

![checkout.css](/readme_images/checkout-css-val.png)
</details>

<details>
<summary>Profile CSS</summary>
<br>

![profile.css](/readme_images/profile-css-val.png)
</details>

***
### JavaScript Validation

I used [JSHint](https://jshint.com/) to validate all JavaScript and JQuery files, you can find my results below:

<details>
<summary>Country Field JS</summary>
<br>

![countryfield.js](/readme_images/countryfield-js-val.png)
</details>

<details>
<summary>Quantity Input JS</summary>
<br>

![quantity input script](/readme_images/quantity-input-script-js-val.png)
</details>

<details>
<summary>Remove/Update buttons JS</summary>
<br>

![Remove/Update buttons JS](/readme_images/remove-update-buttons-js-val.png)
</details>

<details>
<summary>Scroll to top button JS</summary>
<br>

![Scroll to top button JS](/readme_images/scroll-to-top-button-js-val.png)
</details>

<details>
<summary>Sort selector box JS</summary>
<br>

![Sort selector box JS](/readme_images/sort-selector-box-js-val.png)
</details>

***
### Python Validation
I used [Code Institute's Python Linter](https://pep8ci.herokuapp.com/) to lint my Python code.
| File | Result | Validation Details & Screenshots |
| :-- | :-: | -------------------------- |
| custom_storages.py | All clear, no errors found | [custom_storages.py](/readme_images/custom_storages.py-val.png)|
| **FORE GOLF** |  |  |
| fore_golf/settings.py | All clear, no errors found | [settings.py validation](/readme_images/fore_golf-settings.py-val.png) |
| fore_golf/urls.py | All clear, no errors found | [urls.py validation](/readme_images/fore_golf-urls.py-val.png) |
| fore_golf/views.py | All clear, no errors found | [views.py validation](/readme_images/fore_golf-views.py-val.png) |
| **BAG APP** |  |  |
| bag/templatestags/bag_tools.py | All clear, no errors found | [bag_tools.py validation](/readme_images/bag-bag_tools.py-val.png) |
| bag/contexts.py | All clear, no errors found | [contexts.py validation](/readme_images/bag-contexts.py-val.png) |
| bag/urls.py | All clear, no errors found | [urls.py validation](/readme_images/bag-urls.py-val.png) |
| bag/views.py | Only a few "line too long" errors | [views.py validation](/readme_images/bag-views.py-val.png) |
| **CHECKOUT APP** |  |  |
| checkout/admin.py | All clear, no errors found | [admin.py validation](/readme_images/checkout-admin.py-val.png) |
| checkout/apps.py | All clear, no errors found | [apps.py validation](/readme_images/checkout-apps.py-val.png) |
| checkout/forms.py | All clear, no errors found | [forms.py validation](/readme_images/checkout-forms.py-val.png) |
| checkout/models.py | Only a few "line too long" errors | [models.py validation](/readme_images/checkout-models.py-val.png) |
| checkout/signals.py | All clear, no errors found | [signals.py validation](/readme_images/checkout-signals.py-val.png) |
| checkout/urls.py | Only a few "line too long" errors | [urls.py validation](/readme_images/checkout-urls.py-val.png) |
| checkout/views.py | Only a few "line too long" errors | [views.py validation](/readme_images/checkout-views.py-val.png) |
| checkout/webhook_handler.py | Only a few "line too long" errors | [webhook_handler.py validation](/readme_images/checkout-webhook_handler.py-val.png) |
| checkout/webhooks.py | Only one "line too long" error | [webhooks.py validation](/readme_images/checkout-webhooks.py-val.png) |
| **CONTACT APP** |  |  |
| contact/admin.py | All clear, no errors found | [admin.py validation](/readme_images/contact-admin.py-val.png) |
| contact/apps.py | All clear, no errors found | [apps.py validation](/readme_images/contact-apps.py-val.png) |
| contact/forms.py | All clear, no errors found | [forms.py validation](/readme_images/contact-forms.py-val.png) |
| contact/models.py | All clear, no errors found | [models.py validation](/readme_images/contact-models.py-val.png) |
| contact/urls.py | All clear, no errors found | [urls.py validation](/readme_images/contact-urls.py-val.png) |
| contact/views.py | All clear, no errors found | [views.py validation](/readme_images/contact-views.py-val.png) |
| **HOME APP** |  |  |
| home/apps.py | All clear, no errors found | [apps.py validation](/readme_images/home-apps.py-val.png) |
| home/urls.py | All clear, no errors found | [urls.py validation](/readme_images/home-urls.py-val.png) |
| home/views.py | All clear, no errors found | [views.py validation](/readme_images/home-views.py-val.png) |
| **PRODUCTS APP** |  |  |
| products/admin.py | All clear, no errors found | [admin.py validation](/readme_images/products-admin.py-val.png) |
| products/apps.py | All clear, no errors found | [apps.py validation](/readme_images/products-apps.py-val.png) |
| products/forms.py | Only a few "line too long" errors | [forms.py validation](/readme_images/products-forms.py-val.png) |
| products/models.py | Only a few "line too long" errors | [models.py validation](/readme_images/products-models.py-val.png) |
| products/urls.py | Only one "line too long" error | [urls.py validation](/readme_images/products-urls.py-val.png) |
| products/views.py | Only a few "line too long" errors | [views.py validation](/readme_images/products-views.py-val.png) |
| **PROFILES APP** |  |  |
| profiles/apps.py | All clear, no errors found | [apps.py validation](/readme_images/profiles-apps.py-val.png) |
| profiles/forms.py | Only one "line too long" error | [forms.py validation](/readme_images/profiles-forms.py-val.png) |
| profiles/models.py | Only a few "line too long" errors | [models.py validation](/readme_images/profiles-models.py-val.png) |
| profiles/urls.py | Only one "line too long" error | [urls.py validation](/readme_images/profiles-urls.py-val.png) |
| profiles/views.py | Only a few "line too long" errors | [views.py validation](/readme_images/profiles-views.py-val.png) |
