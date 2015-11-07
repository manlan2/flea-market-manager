# Calalog App Description
The Franklin Flea Market app will display what is available at the various booths by booth and item by category.  Each booth owner with have the ability to create their booth page and add items to it.  They will have no ability to change or delete any other booths or items.

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
* App uses Flask, SQLite, Bootstrap.
* Use errorhandler() decorator to create custom error pages.

# Site Map and Status
* Layout - open items
  * Header with navigation          - complete
  * SEO metadata                    - open items
  * Footer with copyright           - open items
* Main page - open items
  * List of booths with links       - open items
  * List of recent items with links - open items
  * Link to all items page          - complete
  * Link to add booth               - complete
* Booth page
  * List of all items with pictures - open items
  * Link to single item page        - open items
  * Add new item button with link   - complete
  * Edit item button with link      - open items
  * Delete item button with link    - complete
  * Edit booth button with link     - open items
  * Delete booth button with link   - open items    
* Add booth page - open items
  * Form for all booth info         - open items
  * Cancel button                   - complete
* Edit booth page - open items
  * Fields to update                - open items
  * Cancel button with link         - open items
* Delete booth page - open items
  * Delete button                   - open items
  * Cancel button with link         - open items
* All items page - open items
  * Links to each item available    - open items
  * Picture of each item            - open items
* Single item page - open items
  * Listing of items                - open items
  * Link to booth page              - open items
* Add item page
  * Form to add item                - open items
  * Cancel button linked to booth   - open items
* Edit item page - open items
  * Form to edit item               - open items
  * Button to cancel with link      - open items
* Delete item page - open items
  * Delete Button                   - open items
  * Cancel Button                   - open items
* Login page - open items
  * Google login button             - open items
  * Cancel button linked to main    - open items
* Contact page - open items

# Catalog App TODO's
* Create page list
* Create routes from page list
* Add JSON endpoints for each page
* Add Google OAuth2.0

# Issues to Resolve
* Sizing unknown images sources of unknown sizes.
  * Pick a default size
  * Test images that are both larger and smaller than default
* Validating phone number in form field using JS.
