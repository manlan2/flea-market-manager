# Calalog App Description
The Franklin Flea Market app will display what is available at the various booths by booth and item by category.  Each booth owner with have the ability to create their booth page and add items to it.  They will have no ability to change or delete any other booth or item.

# Catalog App Specification
* Homepage listing all the booths at the flea market
* Page for each booth with items available.
  * The default view will show most recent items.
  * Categories will be listed on the left side of the app.
  * Clicking on a category will switch the main view to just those items in the category.
* Login page that uses Google OAuth2
* Login button on every page changes to logout when logged in.
* Create a list of authorized users so that only known booth renters can log in.
* Create a booth owner profile page that shows what they are renting and how much they are paying.
* When booth owner logs in they are redirected to their booth page with active links to modify.
* The booth owner admin page shows sold items.
* Create an admin user that can see and modify all fields.
* Create an admin page that can add and delete booths and owners.
* The site should be mobile first and responsive.
* App uses Flask, Postgres, Bootstrap.
* Use errorhandler() decorator to create custom error pages.

# Catalog App TODO's

* Update README to include installation and use instructions
* Create database schema
* Create folder structure
* Create page list
* Create routes from page list
* Add JSON endpoints for each page
* Add Google OAuth2.0
* Review Udacity 330 app repo

# Issues to Resolve
* Sizing unknown images sources of unknown sizes.
  * Pick a default size
  * Test images that are both larger and smaller than default
* Validating phone number in form field using JS.
