# San Diego Art Outlet

San Diego Art Outlet is [deployed on Heroku](https://san-diego-art-outlet-2960cce580c0.herokuapp.com/) and available on [GitHub](https://github.com/ChristineEC/sd_art_outlet)
`https://san-diego-art-outlet-2960cce580c0.herokuapp.com/`
`https://github.com/ChristineEC/sd_art_outlet`

## Table of Contents

## Purpose and Business Model
San Diego Art Outlet is a business-to-consumer (B2C) e-commerce application designed to allow working artists in the San Diego area to market and sell their art to individuals and to market to potential collaborators, such as other artists who may wish to sell on the site.

The primary target audience consists of the consumer looking for local, affordable art that fits their style and living space. The cost of living is extremely high in San Diego, and most people don't have the budget to acquire high-end art. Except for those who live in single-dwelling homes, people also move around a lot, making it impractical to collect art. At the same time, no one wants to stare at their apartment's white walls, and many many people would be attracted to the idea of being able to choose art at a reasonable price that would fit their space. So while specific pieces of art are for sale on the site, a large part of the business is expected to come from custom orders. That is, a customer will see something they like on the site, or an artist they like, then ask that artist to make them something in a certain range of colors, a style, and a size that will fit the space they have in mind. Art-to-order, as it were.

The word "outlet" is used in the title because it connotes "inexpensive".

The business model is that of an artists' collective. Artists sell their work on this common platform, but they are responsible for setting their prices, adding their artworks for sale, keeping their artists' pages up to date, and so on. Artists ship their art directly to the consumer. Shipping costs are included in the price of each piece, as it would not be feasible to set reasonable shipping rates for objects that vary so wildly in size, shape, and weight and which may have other shipping considerations, such as fragility. The site ships only within the United States, and consumers who include non-U.S. addresses receive an email stating they will soon be contacted to arrange in-person pick-up or a refund, or shipping to U.S. territories (such as Puerto Rico) to be arranged at cost.

In addition to online sales, the site encourages interested customers to visit the artists' local events, where customers can meet the artists and see their works in person. The San Diego area has many outdoor art festivals throughout the year, in the different neighborhoods, but they are quite expensive for individual artists to access. As an artist collective, they can better afford to be represented at these events.



## UX
### First impressions
The first-time visitor to the site is immediately aware of the purpose of the site and the nature of goods offered through the use of an abstract-painting-like favicon and an identical icon in the title, a prominent shopping cart icon in the page header, clear headlines that emphasize the purpose, nature (mentioning, e.g., "San Diego local artists," "affordable art"), and an image of one of the artworks.
### Color scheme
The background for the website is a light-blue watercolor painting. It was originally planned to be white in order to let the artworks themselves provide the color, but after working with the project for a time, I decided that the white background was decidedly unartistic. Thus, the change. Text is black in order to provide a high contrast with the light-blue. Muted text is a charcoal gray.

### Fonts

### Structure and navigation
Site structure and navigation consist of elements that users have come to expect on e-commerce sites, with a prominent shopping cart and an overview of items for sale being the first stop on a journey that may include sorting available art by artform, size or artist, exploration of individual artists, making a custom-artwork enquiry, signing up for a newletter, or checking out events where the artists are exhibiting next.
Large buttons--espcially the "Shop Now", "Add to Cart" and "Checkout" buttons--and descriptive links make navigation intuitive, showing the user at a glance what they can do, where they can go, and what information is available on the site.
### Errors
The site has a custom 404 error page to prevent possible user frustration or annoyance and to guide the user's next step.
### Content
Text content is clear, concise, and sparse in order to keep the artwork (and purchasing capability) front and center. Images take up most of each screen in accordance with the nature of the product being sold and are of high quality.
### Accessibility
Semantic HTML is used throughout the site for SEO purposes, to give context to screen readers, as well as to enable keyboard-only navigation as far as possible. Each image has a descriptive alt attribute, and the contrast ratio is high across the site.

### Wireframes

Wireframes for the homepage, gallery (products) page, artwork detail and artists pages were completed prior to writing any html. While coding the first html files (homepage and gallery), I decided to slightly revise the wireframes to simplify the html code that would be needed and, more importantly, to make the wireframes more useful to me as visual aids while creating the html files. The homepage needed to be redesigned somewhat because the original design, in practice (I discovered), was not user-friendly: the 4 large images resulted in the user having to scroll to see the content lower on the page (laptop and mobile), and the images might have been thought by the user to be clickable, as all other images on the website are. They simply took up too much real estate on the landing page, so they were replaced with a single image stretching across the page. The result was much more aesthetically pleasing and better suited to the purpose of the page.

Homepage large screens wireframe

![Homepage large screens wireframe](documentation/wireframes/homepage-large.png)


Homepage tablet wireframe

![Homepage tablet wireframe](documentation/wireframes/homepage-tablet.png)


Homepage mobile wireframe

![Homepage mobile wireframe](documentation/wireframes/homepage-mobile.png)


Gallery mobile wireframe

![Gallery mobile wireframe](documentation/wireframes/gallery-mobile.png)


Artwork detail mobile wireframe

![Artwork detail mobile wireframe](documentation/wireframes/artwork-detail-mobile.png)


Artist page large screen wireframe

![Artist page large screen wireframe](documentation/wireframes/artist-page-large.png)

## User Stories

## Features
### Landing page
### Products page
#### Sorting and navigation
### Products detail page
### Artists' pages
#### Customer View
#### Artist's view
### Custom Order request form
### Events page
### Newsletter signup
### Register
### Login
### Customer Profile page
#### Update profile form
### Product management, front end
The product management, front-end, feature is robust. Attempting to add an artwork without an image results in the artwork being saved as "pending" so that it does not show up on the public site, even if the person adding it forgot to change the default status from "for sale" to "pending". The object can still be managed from the artist's page, and as soon as they include an image, the status can be easily changed from "pending" to "for sale" or "sold". Even if someone accidentally changes the status of an object with no image to "for sale" or "sold" on the back end, there is no way for a customer to add the object to their cart. At that point, a 500 error is raised. 

TO DO STILL: Write a custom 500 error.

## Data Models

![Entity Relationship Diagram](documentation/sd_art_outlet-erd.png)

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
**Fix:** At the suggestion of Oisin at Code Institute's tutor support, I copied the content of my json files to new files and was able to upload them to the new database.

- I encountered a number of bugs with the site's images following implementation of AWS S3 storage of my static files and media. 
First, in development, the homepage static image was in my main static folder in an images subfolder. Although that image was copied over to AWS, it was still in a static/images folder and not being served on the deployed website, even though I added the image to my S3 bucket's media folder. I wasn't able to add the image to the media folder in VS code so that I could use the appropriate tag in `{% MEDIA_URL%}<filename.jpg>` index html that would work in both development and in deployment, either. When I came up with that idea, though, Rebecca at Code Institute told me I could manually add that to my media folder.
**Fix:** Add the jpeg file to my project's media folder in Windows, which was then reflected in my VS code, allowing me to use the `MEDIA_URL` tag in the html as I wanted.
Secondly, some of my artist's images were not showing up in the deployed version. Adding them to the database through the admin panel in the deployed version after having already copied the image files to my S3 bucket was causing the images to be renamed in Postgres on the fly, yet I couldn't see the new renamed images in the bucket, and they were still not being rendered.
**Fix:** Rename all artist images on my computer to artists' names for easier identification. On the development site, change the artist objects' images to the new images. Dump the Artist model data from mySQL local database into a new json file and upload to Postgres locally. At this point, Heroku threw an error upon redeployment, so I set an environment variable `COLLECTSTATIC = 1` on Heroku, deployed, then removed that environment variable. Redeployment after that worked fine, with all images being served from my S3 bucket. In future projects, I would choose not to have different databases in development and deployment but would, rather, use Postgres or other suitable relational database from the beginning.


## Credits
### Helpful people
Many, many thanks to my course facilitator at Code Institute, Kay Welfare, and my Code Institute mentor for this project, Juliia Konn! Thanks also to to Code Institute tutors Oisin, Sarah, Rebecca, Roman; my apologies to any I may have missed.

### Code Institute
This project was developed based on Code Institute's Boutique Ado (BA) e-commerce walkthrough project. Some parts of the html and CSS of the present project--for example, the checkout, checkout_success and shopping cart pages--were heavily based on Boutique Ado, with only slight modifications for my own purposes. The navigation elements follow the BA example very closely, with only minor modifications . The UserProfile and Order models are nearly identical to those in BA; OrderLineItem, Artwork (products), and Medium (category) models are also very closely modeled on BA. The coding for the Stripe functionality relies heavily on BA, including webhooks and webhook handlers.

### Image credits
Many thanks to [Pexels](https://www.pexels.com/), from which most images were sourced.
Specific credits for each image from Pexels follow.
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
- [Photo by ClickerHappy from Pexels](https://www.pexels.com/photo/calm-clouds-fountain-garden-407083/)
- [Photo by Landiva Weber from Pexels](https://www.pexels.com/photo/a-close-up-of-a-green-and-pink-swirl-27376167/)
Artworks images sourced from [Pixabay](https://pixabay.com/):
- [Image by Lily DuVeau](https://pixabay.com/users/lilyduveau-4987876/?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=2290711) from [Pixabay](https://pixabay.com//?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=2290711)
- [Image by Juanita Mulder](https://pixabay.com/users/agnali-3087927/?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=1750014) from [Pixabay](https://pixabay.com//?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=1750014)
- [Image by Lily DuVeau](https://pixabay.com/users/lilyduveau-4987876/?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=2290713) from [Pixabay](https://pixabay.com//?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=2290713)
- [Image by Supichaya Sookprasert](https://pixabay.com/users/neangart-16005384/?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=5062356) from [Pixabay](https://pixabay.com//?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=5062356)

