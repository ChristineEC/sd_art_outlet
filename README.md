# San Diego Art Outlet

[San Diego Art Outlet](https://san-diego-art-outlet-2960cce580c0.herokuapp.com/) is deployed on Heroku. The code is publicly available on [GitHub](https://github.com/ChristineEC/sd_art_outlet).

## Table of Contents
1. [Purpose and Business Model](#purpose-and-business-model)
    - [Purpose](#purpose)
    - [Business Model](#busines-model)
        - [Custom Orders](#custom-orders)
    - [Target Audience](#target-audience)
    - [Summary of Site Functionality](#summary-of-site-functionality)
2. [UX](#ux)
    - [First impressions](#first-impressions)
    - [Color scheme](#color-scheme)
    - [Fonts](#fonts)
    - [Artworks Images](#artworks-images)
    - [Structure and Navigation](#structure-and-navigation)
    - [Wireframes](#wireframes)
    - [Error handling and messages](#error-handling-and-messages)
    - [Content](#content)
    - [Responsiveness](#responsiveness)
    - [Accessibility](#accessibility)
3. [Features and User Stories](#features-and-user-stories)
    - [User Stories Table](#user-stories-table)
    - [Homepage, Navigation and Footer](#homepage-navigation-and-footer)
    - [Shop and Gallery](#shop-and-gallery)
    - [Artwork Detail Page](#artwork-detail-page)
    - [The Shopping Cart](#the-shopping-cart)
    - [Artists page](#artists-page)
    - [Artists' pages](#artists-pages)
    - [Product Management: Full CRUD](#product-management-full-crud)
    - [Custom Order Request](#custom-order-request)
    - [Contact Form](#contact-form)
    - [Events Page](#events-page)
    - [Newsletter Signup](#newsletter-signup)
    - [Register, Login and Logout](#register-login-and-logout)
    - [Customer Profile Page](#customer-profile-page)
    - [Checkout App](#checkout-app)
        - [Email Purchase Confirmations](#email-purchase-confirmations)
        - [Checkout Success](#checkout-success)
    - [Webhooks](#webhooks)
4. [Data Models](#data-models)
    - [Entity Relationship Diagram](#entity-relationship-diagram)
    - [The Models](#the-models)
5. [Agile Methods](#agile-methods)
    - [GitHub Project](#github-project)
    - [Issues Based on User Stories](#issues-based-on-user-stories)
    - [Epics](#epics)
    - [Milestones](#milestones)
    - [Kanban Board](#kanban-board)
    - [MoSCoW Labels](#moscow-labels)
    - [Timeline](#timeline)
6. [Testing](#testing)
7. [Tools and Technologies Used](#tools-and-technologies-used)
8. [SEO and Web Marketing](#seo-and-web-marketing)
9. [Future Enhancements](#future-enhancements)
10. [Deployment](#deployment)
11. [Credits and Thanks](#credits-and-thanks)


## Purpose and Business Model
### Purpose
San Diego Art Outlet is a business-to-consumer (B2C) e-commerce application designed to 
- encourage and allow site visitors to buy from the available selection or put in a custom-order request;
- allow working artists in the San Diego area to market and sell their art to individuals;
- market to potential collaborators, such as other artists who may wish to sell on the site; and
- publicize local events where art lovers can meet the artists in person and see their art.
### Business Model
The business model is that of an artists' collective. The word "outlet" is used in the title because it strongly connotes "inexpensive".

Artists sell their own work on this common platform and are responsible for setting their prices, adding their artworks for sale (to be verified by site-owner or authorized admin before publishing), providing the content for their artist's page, and so on. 

Artists ship their art directly to the consumer. Shipping costs are included in the price of each piece, as it would not be feasible to set reasonable shipping rates for objects that vary so wildly in size, shape, and weight, and which may have other shipping considerations, such as fragility. The site ships only within the United States, and consumers who place orders on the site receive an email confirmation stating they, if they have provided an address outside the 50 states, they will soon be contacted to arrange in-person pick-up or a refund, or shipping to U.S. territories (such as Puerto Rico) to be arranged at cost. 

Most individual artists are not able to receive credit card payments, so they have limited choices for selling online, and most of those choices involve platforms such as Etsy, which have become overcrowded (and overwhelming for the shopper) and which take a cut for each piece sold. (The site owner of San Diego Art Outlet, or the collective, could choose to charge a monthly fee instead, if they wished. This aspect is flexible.) 

Other sites offer little or no extra marketing value for the artists. SD Art Outlet would market locally, on social media, through email newsletters, and through presence at local art events and neighborhood street fairs, which are held throughout the year in San Diego due to the excellent weather but which are often financially out of reach for many individual artists. In addition, the collective could place art on commission in local cafes, bars, restaurants, etc., as is frequently done, though this aspect is not addressed in the project. Please refer to [SEO and Marketing](SEO.md) for more on the topic.

#### Custom Orders
While specific pieces of art are for sale on the site, a large part of the business is expected to come from custom orders. That is, a customer will see something they like on the site, or an artist they like, then ask that artist to make them something in a certain range of colors, a style, and a size that will fit the space they have in mind, with a price to fit their budget: art-to-order, as it were. 


### Target Audience
The primary target audience is the San Diego consumer looking for local, affordable art that fits their style, living space and budget. The cost of living is extremely high in San Diego, and most people don't have the budget to acquire high-end art. Many people would be attracted to the idea of being able to choose art at a reasonable price that would fit their space.
### Summary of Site Functionality
Visitors to the site can log in using their email address, browse the shop or the full gallery containing past and presently available work, visit the artists' individual pages, sort artworks by medium, add items to a shopping cart, and make secure purchases. The site has a login system and employs webhooks to ensure handling of potential user error during checkout, and added functionality for artists (create, read, and delete their own artwork, with creation and deletion limited to works with status "pending" for better control by the site owner). Artist functionality is dependent upon superuser prior approval on the back end, where a registered user (the artist or their representative) is assigned as "user" in the artist model. The superuser has full CRUD functionality for managing artworks on the front end. All users can message the business through the contact us form (non-logged in) or through the custom-order request form, which requires log in. Finally, the site has an events page and a newsletter signup form using MailChimp.

The section [Features and User Stories](#features-and-user-stories) contains a comprehensive discussion of site features with accompanying images.

The testing section, available at [TESTING.md](TESTING.md), contains the results of thorough testing of all site functionality in table form.

## UX
### First impressions
The first-time visitor to the site is immediately aware of the purpose of the site and the nature of goods offered through the use of a colorful art-easel favicon and an identical icon in the title, a prominent shopping cart icon in the page header, and clear headlines and navigation, with an attractive image of one of the artworks.
![homepage](documentation/screenshots/homepage-desktop-screenshot.png)

### Color scheme
The background for the website is a light-blue watercolor painting, one of the works for sale on the site. It was originally planned to be white in order to let the artworks themselves provide the color, but after working with the project for a time, I decided that the white background was decidedly unartistic and unpleasant to look at for long periods of time; thus, the change. Text is black in order to provide a high contrast with the light-blue. Muted text is a dark, charcoal gray. The major buttons are styled in the same dark indigo/purple as the header and footer, and contrast nicely with the background and images.

### Fonts
In keeping with the laid-back Southern California lifestyle and surfing culture, the logo font is "Original Surfer." It is used in the logo header as well as for the header in the full gallery (as opposed to the shop). This latter difference helps to differentiate the two pages (gallery vs. shop), as they are otherwise quite similar. The rest of the site's headlines use Josephine Sans, which gives the site an artsy, welcoming, relaxed feel. The body is set to Lato, as Josephine Sans is only for larger font sizes. (I discovered part way through that non-headers were simply rending as the default browser font, so Lato was added, as it matches well with Josephine Sans and is a clear, easy-to-read font.) The original surfer font had to be removed from the newsletter signup form because, even on laptop, the font at that small font size made it hard for the user to see if they had entered their email address correctly.

Original Surfer is the logo font:

![Original Surfer](documentation/screenshots/original-surfer.png)

Josephine Sans for headlines:

![Josephine-sans](documentation/screenshots/josephine-sans.png)

Lato for other text:

![Lato](documentation/screenshots/lato.png)

### Artworks Images
The images of artworks shown in the shop, the gallery and on artists' pages are shown in their original proportions, as site visitors are expected to already have in mind where they want to place a new piece of art. That is, they might be looking for something high and narrow, or square, or wide and not very high.  The original design and early implementation displayed all images in a square format, but then the artwork detail and the full images would not be able to show their true dimensions, given that the model included only one image field. Future enhancement would require more image fields for the works of art (or at least two): one image of a specific dimension common to all artworks to feature on the shop, gallery and artists' pages, and the other to display the artwork on the artwork detail page and the full-image view in the artworks' true proportions. On the other hand, it could waste users' time if all pieces were presented with the exact same dimensions, only for them to discover later, after clicking through to the artwork's detail, that the piece did not suit their needs at all because of its actual proportions. In the end, it was decided that for this iteration of the project, it was best to show the artworks in their true proportions, even though the pages where they are all shown together might appear a bit uneven in places. For this reason, I added an explanation at the top of those pages so that users would understand that the choice was intentional.

![proportional artwork display](documentation/screenshots/proportional-artwork-display.png)

### Structure and Navigation
Site structure and navigation consist of elements that users have come to expect on e-commerce sites, with a prominent shopping cart, a homepage showing the two major options--to explore the gallery or go straight to the shop--with the overview of artworks on either the shop or gallery page being the first stop on a journey that may include sorting available art by artform, exploration of individual artists, making a custom-artwork inquiry, signing up for a newletter, or checking out events where the artists are exhibiting next. 

![main-nav](documentation/screenshots/main-nav.png)

![sorting](documentation/screenshots/sorting.png)

![mobile nav](documentation/screenshots/mobil-nav.png)

Navigation options depend on whether a user is logged in, as appropriate. Further details about this are available in the Features section. Although a user does need to be logged in to send a custom-order inquiry, they are still able to navigate to the page, even if they are not logged in, where they then have the option to log in to send a custom request or just send a message through the contact form (link provided), which does not require login. This was done to keep the custom-order feature of the website visible to all site visitors, not just in the text but in navigation options as well. In addition, future enhancements would likely include more and better content here to really encourage users to consider making custom orders.

![register or login](documentation/screenshots/register-or-login.png)

![profile or logout](documentation/screenshots/profile-or-logout.png)

![superuser account options](documentation/screenshots/superuser-account-options.png)

Large buttons--especially the "Shop Now", "Add to Cart" and "Checkout" buttons--and descriptive links make navigation intuitive, showing the user at a glance what they can do, where they can go, and what information is available on the site. User's actions, such as an artist adding an artwork, end in useful and expected redirects, with the artist, for example, being redirected back to their own page rather than to the homepage or other option.

Hover effects are used to help the user identify when they hover over a clickable item, such as an artwork image or card, button or link. This is especially useful for the artworks, as it is difficult to see that the cursor changes to a pointer over these. I've added in a thick border that surrounds the artwork card when it is hovered over.

The site has a large footer with helpful links to privacy policy, contact information, contact link and newsletter signup.

![the-footer](documentation/screenshots/the-footer.png)

### Wireframes
Wireframes for the homepage, gallery (products) page, artwork detail and artists pages were completed prior to writing any html. While coding the first html files (homepage and gallery), I decided to slightly revise the wireframes to simplify the html code that would be needed and, more importantly, to make the wireframes more useful to me as visual aids while creating the html files. The homepage needed to be redesigned somewhat because the original design, in practice (I discovered), was not user-friendly: the 4 large images resulted in the user having to scroll to see the content lower on the page, even on a laptop, and the images might have been thought by the user to be clickable, as all other images on the website are. They simply took up too much real estate on the landing page, so they were replaced with a single image stretching across the page. The result was much more aesthetically pleasing and better suited to the purpose of the page.

#### Homepage large screens wireframe

![Homepage large screens wireframe](documentation/wireframes/homepage-large.png)


#### Homepage tablet wireframe

![Homepage tablet wireframe](documentation/wireframes/homepage-tablet.png)


#### Homepage mobile wireframe

![Homepage mobile wireframe](documentation/wireframes/homepage-mobile.png)


#### Gallery mobile wireframe

![Gallery mobile wireframe](documentation/wireframes/gallery-mobile.png)


#### Artwork detail mobile wireframe

![Artwork detail mobile wireframe](documentation/wireframes/artwork-detail-mobile.png)


#### Artist page large screen wireframe

The final design for this page differs somewhat, as the logic involving the display of artists' works and the ability to place them in a shopping cart made it necessary. As with artworks in the shop or gallery, clicking on an artwork brings the user to an artwork detail page, where, if and only if an artwork has the status of "for-sale" will it appear with a button to add it to the shopping cart, otherwise, the user sees the button "back to gallery." This could be improved: users accessing a "sold" work from the gallery should see a button for "back to gallery", and users who access a "sold" work from the artist's page should see a button for "back to artist's page." Ideally, there would be both buttons (to gallery and to artist's page) in both scenarios, so this is an issue for future development.

![Artist page large screen wireframe](documentation/wireframes/artist-page-large.png)


### Error handling and messages
- The site has a custom 404 error page to prevent possible user frustration or annoyance and to guide the user's next step.

![Custom 404 message](documentation/screenshots/custom404.png)

- A future enhancement would be to include a custom 500 error as well to enable the user to get back to the site at the click of a button.
- Forms include built-in validation.
![alt text](documentation/screenshots/built-in-validation.png)

- Where necessary, safeguards are coded in the views and in the html templates to ensure that, for example, an artwork saved without an image cannot appear publicly on the site, even though the form is valid (coded that way so it can be saved to the artist's page and accessed from there by superuser or authorized artist); an artwork that is not *for sale* cannot end up in a shopping cart; or an artist cannot save an artwork under a different artist's name by mistake.

![add success](documentation/screenshots/add-success.png)

- Users receive feedback on their actions in the form of pop up messages, or toasts, informing them what that action was and whether it was successful, and what will (or can) happen next. 

![delete from cart success](documentation/screenshots/after-deletion-from-cart.png)

Images of most of the messages can be seen throughout the [Features and User Stories](#features-and-user-stories) section.

### Content
Text content is clear and concise in order to keep the artwork (and purchasing capability) front and center. Images take up most of each screen in accordance with the nature of the product being sold and are of high quality. Future enhancement would involve adding more text content for SEO purposes, especially to give visitors more of a feel for the artists' collective as a group and as a concept, as well as to encourage new artists to sign up for the collective to sell on the site.
### Responsiveness
The website is fully responsive on all viewports, from mobile through desktop size.
Please see the [TESTING.md](#TESTING.md) for results of responsiveness testing.

![homepage-mobile-screenshot](documentation/screenshots/homepage-mobile-screenshot.png)

### Accessibility
Semantic HTML is used throughout the site for SEO purposes, to give context to screen readers, as well as to enable keyboard-only navigation as far as possible, with autofocus used for forms on the site. Each image has a descriptive alt attribute, all links are aria-labelled, and the contrast ratio is high across the site. 

Please see the [TESTING.md](#TESTING.md) file for results of accessibility testing.




## Features and User Stories

For a full discussion of the features and user stories, with extensive images and the results of manual testing, please refer to [TESTING.md](TESTING.md).

Here, the user stories and features are simply summarized.

### User Stories Table

| User Story | User Story Title | Fulfilling app or feature |
|------------|------------------|---------------------------|
| #1 | As a site visitor I can view a list of available art to see if there is something I want to purchase | Artworks app, Artworks page (Shop) |
| #3 | As a user I can easily access full product details, including price, artist, size, medium, etc., so that I can make an informed decision about whether to buy the item | Artwork detail page |
| #4 | A first time visitor can quickly determine the purpose and offerings of the site so they can decide if they want to explore further | Home app, Homepage |
| #5 | As a site visitor, I can sort the available art by medium so I can quickly find what I am looking for | Artworks app, Shop and Gallery pages, navbar |
| #7 | As a user, I can submit a custom order inquiry without submitting an order so that an artist can contact me later about my requirements | Communications App, Custom Order page and form, Admin |
| #9 | As a user I want to be able to add items to a shopping cart so that I can create a running list of things I want to buy before I proceed to checkout | Cart App |
| #12 | As a shopper I want to review the order information on the checkout page so I can ensure it is correct before making my purchase | Checkout App, checkout page |
| #13 | As a shopper I can review my shopping cart so that I can see which items I have added and what the current grand total is so I don't overspend | Cart App |
| #14 | As a shopper, I want to be able to delete items from my cart so that I can revise my order before purchasing | Cart App |
| #21 | As a site owner or artist, I can add, update and delete items for sale from the front end so that the inventory shown to users is accurate | Product Management Function, Artist's Page |
| #23 | As a site owner I can display information about the artists of the works for sale to drive user engagement and promote the artists | Artists page, Artists' pages |
| #24 | As a site owner, I can display a custom 404 message so that my website maintains a professional look | Custom 404 page |
| #27 | (Future Feature) As a contributing artist I can update and delete my artist information on the front end so that I can optimize my artist page | Future Feature in Artworks App and Artist's page |
| #28 | As a user, I want to be able to see my current total at all times so I can stay within my budget or just easily keep track of my spending | Cart App, Navbar |
| #31 | As a new user, I can create an account using my email and password so I can enjoy full site functionality | Login form (and real emails) |
| #32 | As a user I want to know that my account is secure and has been created so I can be sure that only I have access using my credentials | User Registration and real emails |
| #34 | As a logged-in user, I can save the information I enter during checkout to my account profile so that I don't have to re-enter my information each time I make a purchase | Profile App, checkbox on checkout page |
| #35 | As a user, I can update my account information so that it remains accurate | Profile App |
| #36 | As a user, I can enter my shipping and payment information so that I can complete my order | Checkout App |
| #37 | As a user I can receive an email confirmation of my completed order so I have a record of my purchase and order information | E-mail confirmations |
| #38 | (Future Enhancement) As an artist or site owner, I can create a custom order based on an online inquiry and make the product available only to a specific user for purchase online | Custom Order Inquiry, Artworks, and User models suitably related to provide future functionality (with probable addition of a CustomOrder model) |
| #41 | As a site owner, I can handle webhooks from Stripe to ensure that payment and order processes are fully handled | Checkout App |
| #44 | As a business owner, I want to be able to receive messages from customers or collaborators so I can respond as required by my business | Communications App, Contact Us nav and form, Admin |
| #45 | As a visitor to the site I can sign up for a newsletter so I can be aware of upcoming shows or other news | Newsletter signup in footer through MailChimp |


### Homepage, Navigation and Footer
**User story 4: A first time visitor can quickly determine the purpose and offerings of the site so they can decide if they want to explore further**

The homepage is shown below. Prominent buttons for the shop and gallery, a shopping cart, a pretty piece of art, and the single headline and the clear nav items show the user at glance exactly what the site is for, with the subheading further emphasizing the site's possibilities. The nav elements that are expandable have small arrows to indicate that those menus are expandable. Without leaving the homepage, just by toggling the shop or gallery nav elements, the user can see what types of art are available.

![homepage on laptop](documentation/screenshots/homepage-laptop-screenshot.png)


Mobile Navigation dropdown from hamburger menu:

![Mobile Nav](documentation/screenshots/mobil-nav.png)


Mobile dropdown navigation:

![mobile dropdown navigation](documentation/screenshots/mobil-dropdown.png)


Nav elements are different for logged in or non-logged-in users, and for superusers, as follows:

Not logged in: The My Account dropdown menu shows the options to register or login

![not logged in](documentation/screenshots/not-logged-in.png)


Logged in user: The My Account dropdown menu shows the options **My Profile** and **Logout** (as in the image for the superuser, except without the Product Management option).

Superuser: In addition to the logged in user, the superuser sees **Product Management** in the dropdown menu under My Account.

![superuser navigation](documentation/screenshots/superuser-nav.png)


**User story 45: As a visitor to the site I can sign up for a newsletter so I can be aware of the upcoming shows or other news**

The footer includes a MailChimp sign-up form for the newsletter, displayed prominently, as well as other links to actions the user might take, such as contacting the business or sending a custom-order request. The privacy policy and social media links are there as well, all three of which open in new tabs.

![the footer](documentation/screenshots/footer1.png)

 
### Shop and Gallery
**User story 1: As a site visitor I can view a list of available art to see if there is something I want to purchase** 

The user who visits the shop page finds a list of all available artworks.

![User view of shop](documentation/screenshots/shop.png)


**User Story 5: As a site visitor, I can sort the available art by medium so I can quickly find what I am looking for**
The user can sort artworks even before they get to the shop or gallery or from inside the shop and gallery, as the navbar is visible all the same.
When the user chooses a medium, only artworks of that medium show in the shop until they choose a different medium, all artworks, or navigate away.

![Sorting by medium](documentation/screenshots/sorting-by-medium.png)


The gallery is nearly identical to the shop, except that users can also see works that have already been sold. This is designed to help them come up with ideas for custom orders.

![Gallery](documentation/screenshots/gallery.png)


### Artwork detail page
**User story 3: As a user I can easily access full product details, including price, artist, size, medium, etc., so that I can make an informed decision about whether to buy the item**

In the shop or gallery, when a user hovers over a piece of artwork, that card gets a thick border (and jumps a bit) to indicate it is clickable. On the artwork detail page, users can see all relevant information about an artwork. 

No hover:

![no hover on artpiece](documentation/screenshots/no-hover.png)


Hovered:

![hovered artwork](documentation/screenshots/hover-art.png)

On the artwork detail page, the individual artwork that is *for sale* appears with a button to add it to the shopping cart and buttons to return to the shop or the gallery.

![alt text](documentation/screenshots/for-sale-detail.png)


An artwork that is already *sold*, however, appears only with a button to return to the gallery (as the user will have come from there unless they came from the artist's page, but in any case, they won't have come from the shop, as no sold artworks appear in the shop).

![sold artwork detail](documentation/screenshots/sold-artwork-detail.png)


Clicking on "view full image" opens the image in another tab so the user can get a good look at the piece.

### The Shopping Cart
**User story 7: As a user I want to be able to add items to a shopping cart so that I can create a running list of things I want to buy before I proceed to checkout**

The user is able to add an artwork to the shopping cart by clicking the Add to Cart button on the artwork detail page. When the user does this, they receive a pop up success message near the shopping cart icon containing the contents of their cart.

![add to cart](documentation/screenshots/add-to-cart.png)



**User story 13: As a shopper I can review my shopping cart so that I can see which items I have added and what the current grand total is so I don't overspend**

The user can click the shopping cart icon from any page to review the contents of their cart.

![shopping cart](documentation/screenshots/shopping-cart.png)


**User story 14: As a shopper, I want to be able to delete items from my cart so that I can revise my order before purchasing**

The image above shows the delete link for items in a shopping cart. When a user clicks the link, the item is deleted from their cart, and they receive a success message and stay on the cart page to see what remains, if anything, with a button to return to the shop or go to secure checkout.

![after deletion](documentation/screenshots/after-deletion-from-cart.png)


### Artists page
** User story 23: As a site owner I can display information about the artists of the works for sale to drive user engagement and promote the artists**

The artists page displays all artists with artworks on the site, with a photo of them, a short bio, and a link to their individual artist's page. Full bios appear on the individual **artists' pages**, described in the next subsection. The content for these pages is not yet fully developed but would be one of the first elements to enhance, both for SEO and user engagement. Each artist would be expected to provide a colorful, interesting bio to attract customers, as well as more photos of their past works, not to mention photos of their works hanging in actual homes.

![Artists page](documentation/screenshots/artists-page.png)


### Artists' pages
*User story 23, as above*
**User story 21: As a site owner or artist I can add, update and delete items for sale from the front end so that the inventory shown to users is accurate**

This user story is fulfilled in two ways: 1. for the artist, and 2. for the superuser. See also the [Product Management](#product-management-front-end) section below for more about superuser functionality.

Seen by the regular user, the artist's page simply displays the artist's works that have the status *for sale* or *sold*, as opposed to *pending*.

![artist's page seen by site visitor](documentation/screenshots/artist-page.png)


The artist's individual pages have the following functionality: 

An artist who has been *linked to a user account manually on the back end*, thus at the site owner's discretion, will see a link just under their bio for **adding** their artworks. The superuser sees the same. From the artist's page, no matter how they fill in the form (i.e., if they mistakenly choose another artist as artist), any artwork they add is added with the artist whose page it is as the *artist* of the artwork and as status *pending*, so that it won't appear immdediately on the site. This is so that the site owner has a chance to review the image and content and approve it before publication. On the same page, the site owner can simply update the artwork to change its status to *for sale* if they wish. (If the owner does not want to go through this extra step, they can use the Manage Artworks functionality that only they have access to, available in the dropdown menu under My Account. See the [Product Management](#product-management-front-end) section below for more on this.)

![Artist Kayla's page](documentation/screenshots/kaylas-page.png)


![add by artist success](documentation/screenshots/add-success.png)


Clicking on the pending artwork to view its details brings the artist or superuser to the artwork detail page, where, instead of seeing the usual card containing the artwork details and buttons for adding to cart or returning to gallery or shop, they see the following message, designed to allow the artist or superuse to find the art they just added, even if they mistakenly entered the wrong artist (or simply forgot which artist it was). The link brings them to the artist's page where the artwork can be found.

![pending artwork detail](documentation/screenshots/pending-art1.png)


The artist who tries to **update** an image receives an error message and is redirected back to the homepage. Future enhancement would involve sending the artist back to their own page.

![update error message](documentation/screenshots/update-error1.png)


An (authorized) artist can delete their own artwork from their artist page, but *only if that artwork's status is still pending*. Trying to delete an artwork with status *sold* or *for sale* results in an error message. This is to prevent artists from deleting objects related to already processed orders or users' shopping carts.

![delete error for artist](documentation/screenshots/delete-error1.png)


#### Customer View
The customer does not see any update or delete links and has no access to the product management menu.

#### Artist's view

The artist sees what the superuser sees on their own page only. They have no access to the product management menu.


### Product Management: Full CRUD
**User story 21: As a site owner** (or artist, see above section for artist functionality) **I can add, update and delete items for sale from the front end so that the inventory shown to users is accurate**

The superuser can create, read, update and delete artworks from the Product Management link, for adding a new artwork, or through links below each artwork image, anywhere it appears on the site.

![Product management link](documentation/screenshots/superuser-nav.png)

Accessing the form from the menu:

![accessing the form from the menu](documentation/screenshots/manage_artwork-form.png)

Accessing the form by clicking on "update artwork" under an artwork image, where the form is pre-filled and the user receives a toast message informing them of the artwork being updated:

![Update artwork](documentation/screenshots/manage-artwork.png)


![Superusr view of artwork](documentation/screenshots/superuser-view-of-artwork.png)

![Superuser update artwork](documentation/screenshots/superuser-update-artwork.png)

When the superuser adds an artwork without an image, it is saved as pending, and they are redirected to the artist's page for easy access, as that is the only place it is accessible on the front end.

![superuser saves art as pending](documentation/screenshots/superuser-saved-pending.png)

If the superuser saves an artwork with an image and a status of *for sale*, it is saved and the superuser is redirected to the artwork detail page and presented with a success message.

![add artwork success](documentation/screenshots/add-artwork-success.png)

Attempting to add an artwork without an image results in the artwork being saved as "pending" so that it does not show up on the public site, even if the person adding it forgot to change the default status from "for sale" to "pending". Below is the message received by the superuser who has done so, having been redirected at the same time to the artist's page so they can continue working with the object.

![superuser saved pending](documentation/screenshots/superuser-saved-pending.png)

The object can still be managed from the artist's page, and as soon as they include an image, the status can be easily changed from "pending" to "for sale" or "sold". Even if someone accidentally changes the status of an object with no image to "for sale" or "sold" on the back end, there is no way for a customer to add the object to their cart because no object without an image appears to a regular user anywhere on the site. (This final feature was added during testing. More on this under [Fixed bugs](#fixed-bugs)!).

Artwork can only be updated by the superuser by clicking the update artwork link whereever an artwork is displayed to the superuser.

![superuser view of artwork](documentation/screenshots/superuser-view-of-artwork.png)

The form is prefilled with the object's current data:

![Manage artwork update](documentation/screenshots/manage-artwork.png)

Successful update brings the user to the artwork detail page for that artwork.

![superuser update success](documentation/screenshots/superuser-update-artwork.png)


### Custom Order Request
**User story 7: As a user, I can submit a custom order inquiry without submitting an order so that an artist can contact me later about my requirements**

To send a custom order inquiry, the user has only to click on Custom Order in the navbar or in the footer. It was decided that only logged in users should be able to submit custom orders for several reasons: to prevent casual requests from users who are merely curious but not likely to follow through, and more importantly, to prevent the user typing in a wrong email and the business losing an opportunity. The user can still enter a different name and email, but on the back end the site owner can see which user sent the form, just in case. (Some users might prefer to use a different email in any case, such as when "asking for a friend".) It was also decided that the user, whether logged in or not, should be directed to a page containing the form (although the form is hidden for non-logged in users). This is so that more content can be added at a later date and to present the non-logged in user with the option to either log in or send a message through the contact form, which does not require logging in.

![custom request page for non-logged-in user](documentation/screenshots/not-li-custom-req.png)

A user who is not logged in receives the following message, with an invitation to log in or send a message through the contact form (which does not require login):

![custom request form](documentation/screenshots/custom-req-li.png)

The admin view for the custom order request, allowing for extra functionality and in preparation for future enhancements, perhaps with a Custom Order model.

![custom-order-request-backend](custom-order-backend.png)


### Contact Form
**User story 44: As a business owner, I want to be able to receive messages from customers or potential collaborators so I can respond as required by my business**
![contact form](documentation/screenshots/contact-form.png)

The information is received on the back end.



### Events page
The inclusion of an object with no image is intention and meant to display how an event appears if it does not have a flyer.

![Events page](events-page.png)

### Newsletter signup
**User story 45: As a visitor to the site I can sign up for a newsletter so I can be aware of upcoming shows or other news**

Users can sign up for a newsletter through a MailChimp form embedded in the footer.
![footer](documentation/screenshots/footer1.png)

### Register, Login and Logout
**User story 31: As a new user I can create an account using my email and password so I can enjoy full site functionality**

**User story 32: As a user I want to know that my account is secure and has been created so I can be sure that only I have access using my credentials**

Clicking on register in the nav menu brings the user to the signup form:

![sign-up form](documentation/screenshots/sign-up-form.png)

Filling in the form with valid data results in a message as follows:

![sign-up confirmation message](documentation/screenshots/sign-up-confirmation-msg.png)

After the user submits the sign-up form, they receive an email asking them to confirm that they signed up:

![signup confirmation email](<documentation/screenshots/sign-in confirmation-email.png>)

Clicking on the link brings them to this page on the website:

![confirm email](documentation/screenshots/confirm-email.png)

And clicking on that brings them to the sign-in form with a success message that their account was verified, at which point they can sign in.:

![sign-up confirmed](sign-up-confirmation-msg.png)

![Success new user](documentation/screenshots/success-newuser.png)

A user can log out by clicking on logout in the My Account menu, where they are brought to this page asking for confirmation:

![verify signout](documentation/screenshots/verify-signout.png)

![signout success](documentation/screenshots/signout-success.png)

A user can also reset their password if they have forgotten it. Clicking on the forgot password link sends an email to the user which, when clicked on, brings them to a page to reset their password.

![password reset email](documentation/screenshots/password-reset-email.png)

![password reset form](documentation/screenshots/password-reset-form.png)

![password reset success](documentation/screenshots/password-reset-success.png)

### Customer Profile page
**User story 35: As a user, I can update my account information so that it remains accurate**
#### Update profile form
![update-profile-form](documentation/screenshots/update-profile-form.png)

The form is prepopulated with the user's data if the user has purchased something and checked the "save my info" checkbox during checkout.


### Checkout App
**User story 34: As a logged-in user, I can save the information I enter during checkout to my account profile so that I don't have to re-enter my information each time I make a purchase**
and 
**User story 36: As a user, I can enter my shipping and payment information so that I can complete my order**

![save my info](documentation/screenshots/save-my-info.png)

**User story 12: As a shopper I want to review the order information on the checkout page so I can ensure it is correct before making my purchase**

![checkout page](documentation/screenshots/checkout-page.png)

#### Email purchase confirmations
**User story 37: as a user I can receive an email confirmation of my completed order so I have a record of my purchase and order information**

Users receive an email confirmation after each purchase.

![email order confirmation](documentation/screenshots/email-order-confirmation.png)

#### Checkout Success
The checkout success view:
![checkout success view](documentation/screenshots/checkout-success-view.png)

### Webhooks
**User story 41: As a site owner, I can handle webhooks from STripe to ensure that payent and order processes are fully handled**

Webhooks are employed on the site in order to prevent errors such as a user hitting the back button right after clicking on the payment button but perhaps before the order is created in the database.

When the user navigates to the checkout page (which is always from the cart or the cart toast, which also contains the cart contents), Stripe sends a webhook that a payment intent has been created that is handled in the project's code, which results in the message in the Stripe dashboard "unhandled webhook received":

![Unhandled webhook received](documentation/screenshots/unhandled-webhook-received.png)

When a user clicks on the Complete Order button on the checkout page after filling in their valid information and the test credit card number 4242 4242 42424 4242, Stripe sends the webhook for payment intent succeeded, and the project's webhook handler handles that webhook by ensuring that the order is in the database (or creating it, if not) before sending back a 200 message to Stripe that the order was already in the database or has been created, as the case may be.

![Webhook payment intent succeeded](documentation/screenshots/webhook-pi-succeeded.png)


(Please see the testing section for images from the final deployed version.)

## Data Models
### Entity Relationship Diagram
Following is the ERD used in development. Some models have additional or slightly different fields now--and these are noted in [The Models](#the-models) subsection below--but the relationships are the same between the models. The diagram does not include the Contact Us model, as I realized only later in development that it was crucial for good UX, so non-logged in users could send a message, as well as anyone not wanting to make a custom order inquiry, or an artist interested in contacting the group. That model does not connect to any other model.

![Entity Relationship Diagram](documentation/sd_art_outlet-erd.png)

### The Models
 There are nine models altogether.

 - Artworks app has three models: Artwork, Artist, and Medium
 - Cart app has no models
 - Checkout app has two models: Order and OrderLineItem
 - Communications app has three models: ContactUs, CustomOrderRequest and Events
 - Home app has no models
 - Profiles app has one model: UserProfile

 #### In the Artworks App

The choices in the Artworks app allow for conditional treatment of the objects, both in the views and in the templates, especially in combination with the user privileges or capabilities that can be afforded an artist-user if the superuser connects their user account to their Artist object as the user attribute. In practice, any user account could be assigned as an Artist object's user attribute, though it would normally be expected to be the artist themself.

So the user attribute in Artist just means "that user who has special privileges on that artist's page and in working with that artist's artworks from the artist's page.

In the Artwork model, the BooleanField "custom-made" and the "custom-orderer" field as a foreign key to a user are intended to provide future functionality, together with the CustomOrderRequest model's foreign keys to "artwork" (optional) and to "user", perhaps doing away with the need for a future CustomOrder model.

For the time being, it is the fields "status" and "artist" that provide much of the interesting functionality of the application, as described in the [Features and User Stories](#features-and-user-stories) section.

 ![Artwork choices (status)](documentation/screenshots/models/artwork-status-choices.png)

 ![Artwork Model](documentation/screenshots/models/artwork-model.png)


Note that the Artwork model has null=True but blank=False for its artist attribute. This is to allow for the case where you might want to delete an artist from the database, which means you would want to set the artist attribute on the Artwork object to null. That is, unless you are going to delete an artwork, too, you'd still want the artwork object to be a valid entity, as it could be connected to orders or in shopping cart. At the same time, you really wouldn't want to be adding artworks to the database without artists, not least because they would become quite difficult to work with on the front end, due to the various logic and safeguards in place concerning the display of artwork to the public.

 ![Artist Model](documentation/screenshots/models/artist-model.png)

![Medium Model](documentation/screenshots/models/medium-model.png)

#### In the Checkout App

![Order Model first half](documentation/screenshots/models/order1.png)

![Order Model second half](documentation/screenshots/models/order2.png)

![OrderLineItem Model](documentation/screenshots/models/orderlineitemmodel.png)

#### In the Communications App

For the moment, the CustomOrderRequest Model looks rather boring (and much like the ContactUs model on the front end). However, it does have some extra functionality on the back end for the business owner to keep track of things. More importantly, it has the beginnings of a design to connect users, artworks, and custom-order requests for future custom-order processing (and conditional, role-based displaying) capabilities, *probably without the need for a further model like CustomOrder,* which would be preferable.

![Contact Us and CustomOrderRequest Models](documentation/screenshots/models/comms-models.png)

The event model is a stand-alone model.

![Event Model](documentation/screenshots/models/event.png)

#### In the Profiles App

![UsrProfile Model](documentation/screenshots/models/profile.png)


## Agile Methods
Agile methods were used throughout planning and development of the project.
### GitHub project
A GitHub project, [San Diego Art Outlet Project](https://github.com/users/ChristineEC/projects/6), was created and linked it to the application's repository.
### Issues Based on User Stories
User stories were transferred from the original excel file to GitHub for tracking as follows:  Inside the respository, an issue was created for each user story and then connected to the project. Issues were further broken down into tasks, which were checked off as completed.
![issue](documentation/screenshots/issue.png)

### Epics
Epics were also transferred from excel in the same way, with user stories linked to them as applicable, and they were also linked to the GitHub project.
### Milestones
Milestones were created in the repository, with user stories and epics connected to them, and they were also connected to the project. I made limited use of milestones in the earlier stages and middle stages of the project. At the end, I realized I had forgetten to set later milestones, such as for the Communications App, although many of those features were included in other Epics or Milestones. At the end ofthe project I found I had forgotten to link many activities to the milestones, though in general, the main epics were linked. At the end, I created a few catch-all milestones for the final tasks and linked the tasks to those. I could have made better use of the milestones, as I never connected them to a timeline. In the future, I will surely do so, as it would surely have helped my workflow to have sprints in mind, and I found myself adding certain functionalities (for artists) to the project before completing absolutely required features. On the other hand, I felt the artist-related functionalities were important for the overall purpose of and rationale for the site.

![some-milestones](documentation/screenshots/some-milestones.png)


### MoSCoW Labels
All user stories and epics were assigned a MoSCoW label, and these were used to prioritize work as the project was being developed.
### Kanban Board
All issues and epics started out in the ToDo column of a Kanban board in the project. Other columns included In Progress, In Styling, Done, and Won't Do. The styling column was deleted later in development when it was no longer useful. I made regular use of the Kanban board throughout development (together with the helpful MoSCoW labels), and I can't imagine trying to develop a project without it. I found it so indispensable that the last issue I created was not based on a user story but contained just the remaining tasks that needed to be completed, such as creating a robots.txt file. See image below.
![kanban](documentation/screenshots/kanban.png)
![last tasks](documentation/screenshots/last-tasks.png)
### Timeline
I didn't make use of the timeline feature in my GitHub project, but I will surely do so in the future, as I now better understand the need for a visual representation of sprints as part of an efficient (and healthy!) workflow.
## Tools and Technologies Used
### Languages
- Python 3.12.8
- JavaScript
- HTML
- CSS
### Databases
- SQLite: the databased used in development
- PostgreSQL: used in deployment
### Frameworks and Libraries
- Django, a python framework, was used as the primary tool for developing the application.
- JQuery
### Other Tools
- GitHub: repository for the code
- Git: for version control
- Amazon Web Services (AWS S3)
- Balsamiq - used to create the wireframes
- Boto3: for serving static and image files from AWS S3
- Chrome DevTools - for debugging and for checking site responsiveness on the fly
- Django-allauth - authentication library for user accounts
- DrawSQL - for the Entity Relationship Diagram
- Crispy-bootstrap and 
- Django-crispy-forms - for form layout
- Django-countries - for the dropdown countries in the checkout form
- Django storages - to allow for storage of images and static files in AWS S3
- Font Awesome - for icons
- Google Fonts - for serving the site's fonts
- Gunicorn - the WSGI HTTP server for the application
- JShint - to validate the JavaScript code
- PEP8 - to validate the python code
- Pillow - a python library providing support for working with images in python
- Pip - package manager used to install the dependencies in my local environment
- Privacy Policy Generator - to generate the privacy policy and to allow site users to acccess it in a new tab
- Psycopg2 - for connecting the SQLite database with PostreSQL
- Sitemap Generator - to create the sitemap.xml file
- Stripe - for the payment system, including webhooks
- VSCode: for coding and storing the code locally
- WC3 Validator - to validate the HTML5 code
- WC3 CSS Validator - to validate the CSS code



## SEO and Web Marketing
Please refer to [SEO.md](SEO.md) for documentation about SEO and Web Marketing

## Future Enhancements

While the functionality of the custom request form is acceptable, and the back end contains more functionality than is visible on the front end, future enhancements would include more content and images, and an enhanced form with optional fields for the user to enter their requirements for style, medium, genre, preferred artist, etc. The enhancements would be important both for SEO and to help users understand what the possibilities might be, such as custom art in the same price range as already available art (or even cheaper). This aspect of the site has good marketing potential that is not addressed at this stage of the project. Testimonials and wishlists are really needed to make this part of the project whole, as customers can be inspired by others and by their own "collections" in their wishlists.

The custom order request model is set up to be able to record some extra information on the back end, such as if an order was eventually made and which artwork (subsequently entered in to the system) that custom request and eventual order are linked to. This would be an important feature, and would be part of creating the functionality to allow the user (the "orderer") and only that user to access the item for purchase from their profile page. A third model "custom order" would probably be required.

![custom order backend view](documentation\screenshots\custom-order-backend.png)

Another important enhancement would be to allow for each artwork to have multiple images and to show the artwork hanging on a wall, preferrably in a home setting.

The events page would benefit from photos of the past events and the artists engaging with event attendees.

Artists' bios should be enhanced and made more personal. More artworks and artists should be added.

Delete modals should be put in place for deleting artworks on the front end. This applies especially to deleting by the superuser, as artists can only delete pending objects, so it is less crucial there. In any case, both of these features would be among the very first enhancements in a new iteration of this project.

Delete modals should also be put in place for users deleting objects from their cart. This has not been done yet because a future feature is envisioned wherein the user who goes to delete an object from their cart receives a modal popup wherein they are invited to add it to their wishlist at the same time. In any case, this is an important feature that would be one of the first enhancements in a new iteration.

## Deployment
Please refer to [DEPLOYMENT.md](DEPLOYMENT.md)
## Testing
Please refer to the [TESTING.md](TESTING.md) file for a full write-up of testing prodedures and results.

## Bugs Fixed
- Links for the Account dropdown menu were invisible, except for the one with a currently valid href.
**Fix:** I removed the link to Bulma CSS files in the base.html, as it was not needed and was causing the error.

- The MEDIA_URL template tag was not working for files that were added manually to the project's media folder, such as the homepage images or the 'noimage.jpg' file, although it was working for images added to the media folder when objects with image attributes were added to the database (in development).
**Fix:** Added `django.template.context_processors.media` in the context_processors option of TEMPLATES in settings.py.

- Orders were being created in the database, but line items were not being added to the orders, so they were empty, although charges for the correct amounts were being processed. This led me to research my code involving the Order and OrderLineItem models and views.
**Fix:** I added one save method that I had accidentally left out (or possibly accidentally deleted) and revised the other in the Order and OrderLineItem models. I also fixed a typo where the line items were being summed in a method in the Order model.

- For the cancel button (an anchor tag styled as a button) on the artist's "add an artwork" form (as a non-superuser but as the artist of the artwork to be added), from the url `/artworks/artist_add_art/1/`, I was trying to inject the desired href for returning the artist-user to their page by using javascript to get the artist id from the url and set it in the href, but I struggled to get the link to work as expected, even though it looked fine in the rendered html. It would either add the contents of the href to the current url (for a path that didn't exist), or it would start the url with just the href (and not the preceding `/artworks/` needed). Even when I added in the preceding part of the url that was needed (or so I thought), it then added that on to the end of the `/artworks/artist_add_art/1/` url. Awaiting tutoring assistance, I discovered a solution that worked: hardcoding the href to `javascript:history.back(-1);`. It worked beautifully! However, as I was implementing that, I thought of one more thing to try that I have decided to implement as the fix:
**Fix:** The href needed to be set, not as `artist/${artistId}/` or `/artist/${artistId}/` or `artworks/artist/${artistId}/` but as `/artworks/artist/${artistId}/'. So much trouble over one little forward slash, but a worthwhile learning experience!

- Contact Us Form labels appeared above the input areas, despite having tried to remove the auto-generated labels. I was able to find a solution as follows in the django-crispy-forms documentation:
**Fix:** In the forms.py file include: from crispy_forms.helper import Form Helper, then assign the helper to the form object using `self.helper = FormHelper(self)`, then call the helper with the following: `self.helper.form_show_labels = False`

- Uploading json files to Postgres threw the following error: UnicodeDecodeError: 'utf-8' codec can't decode byte 0xff in position 0: invalid start byte
**Fix:** At the suggestion of Oisin at Code Institute's tutor support, I copied the content of my json files to new files and was able to upload them to the new database. This fix was required each time I needed to upload a json file created through a dumpdata command, interestingly.

- I encountered a number of bugs with the site's images following implementation of AWS S3 storage of my static files and media.

    1. First, in development, the homepage static image was in my main static folder in an images subfolder. Although that image was copied over to AWS, it was still in a static/images folder and not being served on the deployed website, even though I added the image to my S3 bucket's media folder. I wasn't able to add the image to the media folder in VS code so that I could use the appropriate tag in `{% MEDIA_URL%}<filename.jpg>` index html that would work in both development and in deployment, either. When I came up with that idea, though, Rebecca at Code Institute told me I could manually add that to my media folder.

    **Fix:** Add the jpeg file to my project's media folder in Windows, which was then reflected in my VS code, allowing me to use the `MEDIA_URL` tag in the html as I wanted.

    2. Secondly, some of my artist's images were not showing up in the deployed version. Adding them to the database through the admin panel in the deployed version after having already copied the image files to my S3 bucket was causing the images to be renamed in Postgres on the fly, yet I couldn't see the new renamed images in the bucket, and they were still not being rendered.

    **Fix:** Rename all artist images on my computer to artists' names for easier identification. On the development site, change the artist objects' images to the new images. Dump the Artist model data from mySQL local database into a new json file and upload to Postgres locally. At this point, Heroku threw an error upon redeployment, so I set an environment variable `COLLECTSTATIC = 1` on Heroku, deployed, then removed that environment variable. Redeployment after that worked fine, with all images being served from my S3 bucket. In future projects, I would choose not to have different databases in development and deployment but would, rather, use Postgres or other suitable relational database from the beginning.

- Lighthouse scores were initially poor for page-rendering speed.

    **Fix**: Remove the setting of the site's background image from CSS and include it as an attribute in the html (on the body element) and also ensure that it was being served from the AWS S3 bucket, rather than my static images folder. At the same time I checked to make sure all images that had previously been served from static images during development were coded so that they would be served from the media folder locally and thus AWS S3 bucket in deployment. The static/images folder was then deleted. This sped up page-load times significantly.

- During testing it was discovered that the superuser adding an artwork on the front end could cause a 500 error by trying to save the form without choosing an artist as the artist for that artwork. The model field for artist in the Artwork model was set to null=True and blank=True so that an artwork bought at some point could still be tracked and have valid data even if the artist was deleted from the system, with on_delete for that field set to SET_NULL in the Artwork model. I didn't want to change this, and I also wanted the superuser to be able to save an artwork on the back end, at least temporarily, without an artist. 

    **Fix: I set the artist field in the Artwork model as null=True and blank=False so that the form would simply prevent a user on the front end from saving an artwork without an artist. (Otherwise, the superuser or other authorized user would be unable to access that artwork at all on the front end and would have to go to the back end to find it.) Now the form will not validate on the front end without the user choosing an artist, which is what I wanted.

![Must choose artist](documentation/screenshots/must-choose-artist.png)

        As an aside, earlier in development I had had to work to get that form not to show the first artist as the placeholder text, as it had been doing (for some reason I still don't quite understand, as it is a drop-down choice), because it was too easy for the user to accidentally leave the current artist's name in place and thus potentially save the artwork to the wrong artist. That then led me to put in the safeguard of adding the artist's name and a link to their page to the template the user is redirected to when an artwork is saved as pending so that the user could find the artwork again on the front end (as it would then only appear on that artist's page). Not choosing the artist, even though artist is not a required field in the artwork model, was leading to the 500 error precisely because I had set that safeguard in place: to redirect the user after form submission to the artist's page in case of the artwork's not having an image or being saved as pending: no artist means there was no way for django to redirect to the artist's page. It's fun when it all comes together like this! I had no idea what blank=False was for before this. It would be a bad idea to let a front end user, even a superuser, save artwork on the front end without the artist, even if that is desired for the back end.

- The superuser could change the status of an artwork without an image to *sold* or *for sale* on the back end, and then that artwork would appear in the shop or gallery and with an *add to cart* button on the artwork detail page.

    **Fix:** Template logic had to be adjusted in all three templates so that even if an artwork had a status of sold or for sale, it still wouldn't appear in the shop or gallery if it didn't have an image. Although it wasn't possible for this error to arise from front-end management, as any object without an image is saved as *pending*, back end management allowed the superuser to change that status without adding an image, so the extra template logic was needed. For the artist's page, a similar adjustment was needed, though the artwork still needed to be available to the superuser or authorized artist there.

## Credits and Thanks
### Helpful people
Many, many thanks to my course facilitator at Code Institute, **Kay Welfare**, and to my Code Institute mentor for this project, **Juliia Konn**! 

Thanks also to to Code Institute tutors **Oisin, Sarah, Rebecca** and **Roman** (and my sincere apologies to any I may have missed, as each of you has been of invaluable help).

A heartfelt thanks to Jacob Rocha and to [ArtWalk San Diego](#https://www.artwalksandiego.org). Jacob generously took the time to reply to my email and provide me with the ArtWalk San Diego event flyers used in the events section of my project, and he and the organization gave me permission to use the flyers. Some people are so nice!

Thanks to all of the developers out there making available all of the open-source code I've used in this project!

### Code Institute
Thanks to **Code Institute** for their great full-stack-developer program! It's been a challenging and rewarding journey. I learned so much and received all the support I could have asked for. Thank you!

This project was developed based on Code Institute's Boutique Ado (BA) e-commerce walkthrough project. Some parts of the basic html layout and CSS of the present project--for example, the checkout, checkout_success and shopping cart pages--were heavily based on Boutique Ado, with only slight modifications for my own purposes. The navigation elements such as the dropdown menus follow the BA example very closely, with only minor modifications. The UserProfile and Order models are nearly identical to those in BA; OrderLineItem, and Medium (category) models are also very closely modeled on BA. The coding for the Stripe functionality relies heavily on BA, including webhooks and webhook handlers.

The instructions for creating an AWS bucket and permissions are largely taken from Code Institute's pdf walkthrough that they provided us, though many of the images are my own, taken as I was redoing the steps during debugging.

### Image credits
Many thanks to [Pexels](https://www.pexels.com/), from which most images were sourced.
Specific credits for each image from Pexels follows.

Photos for the artists:
- [Photo by Aleaid Kozik](https://www.pexels.com/photo/a-woman-watercolor-painting-7181853/)
- [Photo by Nataliya Vaitkevic]( https://www.pexels.com/photo/a-woman-with-paint-on-her-hands-5641812/)
- [Photo by Matheus Bertelli](https://www.pexels.com/photo/silhouette-of-woman-photographer-using-camera-at-night-2376991/)
- [Photo by Mikhail Nilov](https://www.pexels.com/photo/woman-in-green-long-sleeve-shirt-holding-white-printer-paper-6932520/)

Photos for artworks:
- [Photo by Efrem  Efre](https://www.pexels.com/photo/northern-lights-27734078/)
- [Photo by Steve Johnson](https://www.pexels.com/photo/multicolored-abstract-painting-1266808/)
- [Photo by Steve Johnson](https://www.pexels.com/photo/multicolored-abstract-painting-1266808/)
- [Photo by Steve Johnson](https://www.pexels.com/photo/multicolored-abstract-painting-1269968/)
- [Photo by Steve Johnson](https://www.pexels.com/photo/photo-of-blue-abstract-painting-2123666/)
- [Photo by Dan Cristian Pădureț](https://www.pexels.com/photo/photo-of-multicolored-abstract-painting-1193743/)
- [Photo by Zaksheuskaya](https://www.pexels.com/photo/teal-white-and-pink-paint-1561020/)
- [Photo by Steve Johnson](https://www.pexels.com/photo/photo-of-abstract-painting-on-canvas-1626364/)
- [Photo by Steve Johnson](https://www.pexels.com/photo/multicolored-abstract-painting-1787242/)
- [Photo by Steve Johnson](https://www.pexels.com/photo/multicolored-abstract-painting-1856456/)
- [Photo by Steve Johnson](https://www.pexels.com/photo/multicolored-abstract-painting-1856455/)
- [Photo by Steve Johnson](https://www.pexels.com/photo/photo-of-abstract-painting-1843716/)
- [Photo by Steve Johnson](https://www.pexels.com/photo/multicolored-abstract-painting-1985682/)
- [Photo by Steve Johnson](https://www.pexels.com/photo/red-and-yellow-floral-textile-1787243/)
- [Photo by Steve Johnson](https://www.pexels.com/photo/photo-of-blue-abstract-painting-2123667/)
- [Photo by Steve Johnson](https://www.pexels.com/photo/multicolored-abstract-painting-1985664/)
- [Photo by Steve Johnson](https://www.pexels.com/photo/multicolored-abstract-painting-2085588/)
- [Photo by Quang Nguyen Vinh](https://www.pexels.com/photo/landscape-mountains-nature-water-6348018/)
- [Photo by Marek Piwnicki](https://www.pexels.com/photo/white-smoke-in-grayscale-photography-11032516/)
- [Photo by Niklas Jeromin](https://www.pexels.com/photo/a-close-up-of-a-blurry-christmas-tree-19562594/)
- [Photo by Marek Piwnicki](https://www.pexels.com/photo/white-smoke-in-dark-room-13327735/)
- [Photo by Marek Piwnicki](https://www.pexels.com/photo/ghost-15499506/)
- [Photo by ClickerHappy](https://www.pexels.com/photo/calm-clouds-fountain-garden-407083/)
- [Photo by Landiva Weber](https://www.pexels.com/photo/a-close-up-of-a-green-and-pink-swirl-27376167/)

Thank you to [Pixabay](https://pixabay.com/), as well, from which the following images were sourced:
- [Image by Lily DuVeau](https://pixabay.com/users/lilyduveau-4987876/?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=2290711) from [Pixabay](https://pixabay.com//?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=2290711)
- [Image by Juanita Mulder](https://pixabay.com/users/agnali-3087927/?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=1750014) from [Pixabay](https://pixabay.com//?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=1750014)
- [Image by Lily DuVeau](https://pixabay.com/users/lilyduveau-4987876/?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=2290713) from [Pixabay](https://pixabay.com//?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=2290713)
- [Image by Supichaya Sookprasert](https://pixabay.com/users/neangart-16005384/?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=5062356) from [Pixabay](https://pixabay.com//?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=5062356)
