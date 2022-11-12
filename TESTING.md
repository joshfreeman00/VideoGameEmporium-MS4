

# Testing

To return to the readme click [here.](README.md)

## Code validation

### HTML validation

* Validation for the HTML can be found [here.](https://validator.w3.org/nu/?doc=https%3A%2F%2Fvideo-game-emporium-ms4.herokuapp.com%2F)

![html_validation](docs/testing/html_validation.png)

### CSS validation

* Validation for the CSS can be found [here.](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fvideo-game-emporium-ms4.herokuapp.com%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en)

    - Note: any errors within this validation is to do with Bootstrap, if the CSS code is entered through direct input, no errors will show, as seen below:

    * ![css_validation](docs/testing/css_validation.png)

### JS validation

* Validation for the JS can be found [here.](https://jshint.com/)

![js_checkout](docs/testing/checkout_valid.png)

![js_profiles](docs/testing/profiles_valid.png)

### Python Validation

* Cart app
    - context.py
        ![cart_context](docs/python_validation/cart_context.png)
    - urls.py
        ![cart_urls](docs/python_validation/cart_urls.png)
    - views.py
        ![cart_views](docs/python_validation/cart_views.png)

* Checkout app
    - admin.py
        ![checkout_admin](docs/python_validation/checkout_admin.png)
    - apps.py
        ![checkout_apps](docs/python_validation/checkout_apps.png)
    - forms.py
        ![checkout_forms](docs/python_validation/checkout_forms.png)
    - models.py
        ![checkout_models](docs/python_validation/checkout_models.png)
    - signals.py
        ![checkout_signals](docs/python_validation/checkout_signals.png)
    - urls.py
        ![checkout_urls](docs/python_validation/checkout_urls.png)
    - views.py
        ![checkout_views](docs/python_validation/checkout_views.png)

* Home app
    - urls.py
        ![home_urls](docs/python_validation/home_urls.png)
    - views.py
        ![home_views](docs/python_validation/home_views.png)

* Profiles app
    - forms.py
        ![profiles_forms](docs/python_validation/profiles_forms.png)
    - models.py
        ![profiles_models](docs/python_validation/profiles_models.png)
    - urls.py
        ![profiles_urls](docs/python_validation/profiles_urls.png)
    - views.py
        ![profiles_views](docs/python_validation/profiles_views.png)

* Stock app
    - admin.py
        ![stock_admin](docs/python_validation/stock_admin.png)
    - forms.py
        ![stock_forms](docs/python_validation/stock_forms.png)
    - models.py
        ![stock_models](docs/python_validation/stock_models.png)
    - urls.py
        ![stock_urls](docs/python_validation/stock_urls.png)
    - views.py
        ![stock_views](docs/python_validation/stock_views.png)

## Defensive programming tests

* For defensive programming, if the user is not logged in when trying to view their profile, it will ask them to log in. Even if the user bypasses this by using the url, it will still ask them to log in.

* For superuser only features (i.e access to stock managment page), if the user is not a superuser, an error toast will show indicating that they are not authorised, and redirects the user back to the home page.

![error_toast](docs/testing/error_toast.png)

### Error handling

* Error: 404

![404_error](docs/testing/404_error.png)

* Error: 500

![500_error](docs/testing/500_error.png)

## Responsiveness

* The following images will showcase how the project is shown on different devices and shows the responsiveness of the project.

    - Mobile devices:

    ![mobile](docs/testing/mobile_view.png)
    ![mobile_products](docs/testing/mobile_products.png)

    - Tablet devices:

    ![tablet](docs/testing/tablet_view.png)
    ![tablet_poducts](docs/testing/tablet_products.png)

    - Desktop devices:

    ![desktop](docs/testing/home_page.png)
    ![product_page](docs/testing/products.png)

## Browser Compatibility

* The following images shows the project being tested in both Chrome and Safari browsers.

    - Chrome

    ![chrome](docs/testing/vge_chrome.png)

    - Safari

    ![safari](docs/testing/vge_safari.png)


## User story testing

### Viewing and navigation

* ![view_nav](docs/userstories/view_nav.png)
    * User Story ID 1:
        - ![products](docs/testing/products.png)
    * User Story ID 2:
        - ![product_detail](docs/testing/product_detail.png)
    * User Story ID 5:
        * The carts price has a default value of £0.00 until a product is added to the cart. After the cart changes colour and the prices updates accordingly.
            - ![cart_price](docs/testing/cart_price.png)

### Registration and accounts

* [accounts](docs/userstories/accounts.png)
    * User Story ID 6 & 7:
        * If the user interacts with the 'My Profile' nav link, options to register and log in can be found, each taking them to their respective page.
            - ![login_page](docs/testing/login.png)
            - ![signup_page](docs/testing/signup.png)
    * User Story ID 8:
        * If the user has forgotten their password, they can interact with 'Forgot password?' where they would be asked to fill in their email address, interacting with the reset button will send a email with a link to reset their password.
            - ![login_page](docs/testing/login.png)
            - ![password_reset](docs/testing/password_reset.png)
    * User Story ID 10:
        - ![profile](docs/testing/profile.png)

### Product searching and sorting

* ![product_search](docs/userstories/product_search.png)
    * User Story ID 11:
        * Interacting with the 'Sort By' dropdown allows the user to sort by either price or alphabetically in ascending or descending order
            - ![sorting](docs/testing/sorting.png)
    * User Story ID 12:
        * The user can interact with the products nav link and select any category they would like, doing so opens the product page with all of the current products in the category they have chosen.
            - ![categories](docs/testing/categories_example.png)
    * User Story ID 13 & 14:
        * The user can use the search bar at the top of the site and search for a specific term, the search query will return anything that has the users search query within the products name or description and the amount of products returned.
            * An example of a user searching for 'po' returns 4 products is show below.
            - ![search_query](docs/testing/search_query.png)

### Purchases and checkout

* ![purchases](docs/userstories/purchases.png)

    * User Story ID 15:
        * The user can select the quantity and size of the product on the products details page.
            - ![products_detail](docs/testing/product_detail.png)
    * User Story ID 16 & 17:
        * The User can achieve all of this from the shopping cart.
            - ![cart_example](docs/testing/cart_example.png)
    * User Story ID 18, 19, 20 & 21:
        * The User can achieve all of this from the checkout page.
        * The website uses stripe for easy payments, located at the bottom of the checkout form.
            - ![order_example](docs/testing/order_example.png)
    * User Story ID 22:
        - ![order_confirm](docs/testing/order_confirm.png)
    * User Story ID 23:
        - ![email_confirm](docs/testing/email_confirm.png)

### Management

* ![management](docs/userstories/management.png)
    * User Story ID 24:
        * The admin can add products by navigating themselves to the 'Stock Management' page.
            - [stock_management](docs/testing/stock_management.png)
        * Here, the admin or superuser can interact with the 'Add product' button, which takes them to the add product page.
            - ![add_product](docs/testing/add_product.png)
    * User Story ID 25:
        * The admin can edit products by either navigating themselves to the 'Stock Management' page or from the 'products' page.
            - [stock_management](docs/testing/stock_management.png)
            - ![product_page](docs/testing/products.png)
        * Here, the admin or superuser can interact with the blue Edit text, which takes them to the edit product page for the specific product.
            - ![edit_product](docs/testing/edit_product.png)
    * User Story ID 26:
        * The admin can edit products by either navigating themselves to the 'Stock Management' page or from the 'products' page.
            - [stock_management](docs/testing/stock_management.png)
            - ![product_page](docs/testing/products.png)
        * Here, the admin or superuser can interact with the red Delete text, which causes a defensive modal to pop up, asking if they would like to continue, interacting with the 'delete' button will delete the product.
            - ![delete_modal](docs/testing/delete_modal.png)

### Site information

* ![site_info](docs/userstories/site_info.png)
    * User Story ID 27:
        - ![welcome_text](docs/testing/welcome_text.png)

### Contact information

* ![contact_info](docs/userstories/contact_info.png)
    * User Story ID 28:
        - ![footer](docs/testing/footer.png)

## Environment testing

* The following images are within two seperate environments, they have different URLs to validate this.

### Local environment

* The images below show the game within the local (development) environment of gitpod.

![local_env](docs/testing/local_env.png)

### Production environment

* The images below show the game within the production (deployed) environment of Heroku.

![delpoyed_env](docs/testing/deployment_env.png)

## Bugs



### Unfixed bugs

* There are no unfixed bugs that I am currently aware of.