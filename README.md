# The Older and Wider Podcast

Older and Wider is a humorous (and [real](https://shows.acast.com/older-and-wider-podcast)) podcast, where two friends chat and share their day-to-day experiences as “women of a certain age”. It is hosted by retired television producer/writer, Judith Holder, and award-winning comedian, Jenny Eclair.

The purpose of the website is to give interested parties insights and information about the podcast, and will include an embedded podcast player, details on live events, and access to the popular Instagram page; it also provides a way to contact the podcast directly, share stories, and make suggestions for the show.

## Site Preview

![Preview of the Older & Wider website at different screen sizes](assets/images/site-preview.webp)

## Site Link

[here]: https://dvfrancis.github.io/older-and-wider
The Github Pages live site can be accessed [here].

## UXD

### Strategy

#### User Experience

- Target audience

    - Women over 60 (but anyone welcome).
    - Are mature individuals, with lots of life experience.
    - May have children and grandchildren.
    - Might still be working or retired.
    - Could be anyone looking for information about the podcast.
 
### User Expectations

- An accessible and responsive website.
- Easy access to relevant information.
- A standardised navigation system on each page.
- A way to get in touch with the podcast, to share experiences.
- An experience that matches existing expectations of what to expect from a website; for example, links are easy to identify and function as expected.
- An appealing visual design that is kind to the eyes.

#### User Stories

- First time visitor goals:

    - "What is the Older and Wider podcast about?"
    - "Who is Jenny Eclair?"
    - "Who is Judith Holder?"
    - "Where can I listen to the Older and Wider Podcast"
    - "When are episodes of the Older and Wider podcast released?"

- Returning visitor goals:

    - "I want to find out more background information about the Older and Wider podcast"
    - "What was mentioned during the 'Culture Corner' segment of this week's show?"
    - "Has the podcast won any awards?"
    - "What is the 'Message Board' - it was mentioned by Jenny and Judith in this week's episode, but where can I access it?"

- Frequent visitor goals:

    - "How can I contact Jenny and Judith to share my experiences, or comment on an item that was mentioned in the show?"
    - "Is there any podcast merchandise available?"
    - "Can I watch the podcast being performed live?"

### Scope

#### Existing Features

- Browser Tab Icon:

    - A custom HTML favicon will be shown to aid users' identification of the site. It will also appear whenever someone adds the site as a bookmark or favourite.

- Header:

    - Fixed at the top of each page - contains logo and navigation.
    - The header allows the user to identify where they are on the site.
    - Plain background colour.
    - Site name will be centred in the first row, and link back to the home page when clicked.
    - Navigation bar will be centred in the second row, beneath the site name:
        - Home - takes the user back to the home page when clicked.
        - About - takes the user to a page with information about the podcast and both hosts.
        - Message Board - takes the user to a page with the podcast's embedded Instagram profile.
        - Contact - takes the user to a contact form that can be completed to send a message to the podcast hosts.
    - The currently active page is indicated on the navigation bar.
    - The header is responsive to different device sizes, and changes layout accordingly.

- Footer:

    - Fixed at the bottom of each page - contains the social media icons, and legal\copyright information.
    - The footer allows the user to jump to the social media properties of the podcast (on a new page).
    - Plain background colour.
    - Social media icons are centred in the first row.
    - Legal information is centred in the second row.
    - On mouseover, each social media icon will change to colour, and also when clicked.
    - The footer is responsive to different device sizes, and changes layout accordingly.

- Home (index):

    - This is the first page a user sees when they enter the site. It contains all pertinent information regarding the podcast, with links to other pages where required.
    - The 'Home' page allows the user to get a good overview of the purpose of the podcast and gives them glimpses of associated activities.
    - The page will feature an introduction to the podcast featuring a carousel of images, podcast player, details about the live shows, link to an external merchandise website, and a mailing list signup form.
    - The live shows section has details about upcoming live shows, with a link to buy available tickets.
    - The merchandise section has a link that takes the user to the merchandise website (in a new tab).
    - In the mailing list section, the user has the opportunity to sign-up for a regularly released newsletter.
    - The 'Home' page is responsive to different device sizes, and changes layout accordingly.

- Mailing List Completion:

    - A custom completion page appears once 'Send' is clicked on the mailing list signup form on the home page, with suggested links to other parts of the site.
    - After 30 seconds, the page will redirect automatically to the home page.
    - The mailing list completion page is responsive to different device sizes, and changes layout accordingly.

- About:

    - This section contains more detailed information, with a "deeper dive" into the podcast's purpose and the people behind it. It helps the user to understand the motivations behind the creation and continuation of the podcast.
    - Sections:
        - Information about the podcast.
        - Biography of Jenny Eclair.
        - Biography of Judith Holder.
    - The 'About' page is responsive to different device sizes, and changes layout accordingly.

- Message Board:

    - The "Message Board" page allows the user to read posts on the Instagram page without having to navigate away from the site, so keeping them on the site for longer.
    - The podcast's Instagram profile is embedded on this page.
    - The "Message Board" page is responsive to different device sizes, and changes layout accordingly.

- Contact:

    - The 'Contact' page allows the user to send a message to the podcast hosts, helping them to feel involved in the podcast, it contains:
        - First Name field - for user's first name.
        - Last Name field - for user's last name.
        - Age field (that allows fractions – which is a running joke on the podcast).
        - Message field - for users to enter their message.
        - Send button - users can click this button to send their message.
        - Reset button - users can click this button to clear any information already entered on the form.
    - All fields have validation where appropriate.
    - Text input fields all have placeholder text.
    - All inputs are required.
    - A custom completion page appears once 'Send' is clicked, with links to other parts of the site. It will also redirect the user to the home page automatically after 30 seconds.
    - The 'Contact' page is responsive to different device sizes, and changes layout accordingly.

- Contact Completion:

    - Custom completion page appears once 'Send' is clicked on the Contact page, with suggested links to other parts of the site.
    - After 30 seconds, the page will redirect automatically to the home page.
    - The contact completion page is responsive to different device sizes, and changes layout accordingly.

- Custom 404:
    - A custom 404 error page appears whenever a user attempts to navigate to a non-existent page.
    - The custom 404 error page will add humour to the site while offering suggested links to other pages on the site.
    - After 30 seconds, the page will redirect automatically to the home page.
    - The custom 404 page page is responsive to different device sizes, and changes layout accordingly.

#### Future Features

- The addition of a website forum would allow fans of the podcast to interact, discuss the show, and share their life experiences.

### Structure

#### User Flow diagram

- TBA

### Skeleton

#### Wireframes

##### Mobile

- [Home (index)](documentation/wireframes/mobile/index.png)
- [About](documentation/wireframes/mobile/about.png)
- [Message Board](documentation/wireframes/mobile/message-board.png)
- [Contact](documentation/wireframes/mobile/contact.png)
- [Contact Completion](documentation/wireframes/mobile/contact-completion.png)
- [Custom 404](documentation/wireframes/mobile/custom-404.png)

##### Mobile (with menu)

- [Home (index)](documentation/wireframes/mobile/index-menu.png)
- [About](documentation/wireframes/mobile/about-menu.png)
- [Message Board](documentation/wireframes/mobile/message-board-menu.png)
- [Contact](documentation/wireframes/mobile/contact-menu.png)
- [Contact Completion](documentation/wireframes/mobile/contact-completion-menu.png)
- [Custom 404](documentation/wireframes/mobile/custom-404-menu.png)

##### Tablet

- [Home (index)](documentation/wireframes/tablet/index.png)
- [About](documentation/wireframes/tablet/about.png)
- [Message Board](documentation/wireframes/tablet/message-board.png)
- [Contact](documentation/wireframes/tablet/contact.png)
- [Contact Completion](documentation/wireframes/tablet/contact-completion.png)
- [Custom 404](documentation/wireframes/tablet/custom-404.png)

##### Desktop

- [Home (index)](documentation/wireframes/desktop/index.png)
- [About](documentation/wireframes/desktop/about.png)
- [Message Board](documentation/wireframes/desktop/message-board.png)
- [Contact](documentation/wireframes/desktop/contact.png)
- [Contact Completion](documentation/wireframes/desktop/contact-completion.png)
- [Custom 404](documentation/wireframes/desktop/custom-404.png)

### Surface

#### Colours

The following colours will be used to add interesting backgrounds to site sections, while white (#FFF) will be used for all contrasting text:

![colours](https://github.com/dvfrancis/older-and-wider/assets/30801098/2085c8f6-269d-427b-bb4a-20d0ed51ab30)

[Facebook Light Blue (#17A9FD) and Facebook Dark Blue (#0165E1)]:https://brandpalettes.com/facebook-colors
[Instagram Rose (#E1306C) and Instagram Purple Red (#C13584)]: https://brandpalettes.com/instagram-color-codes

For the Facebook social media icon I used [Facebook Light Blue (#17A9FD) and Facebook Dark Blue (#0165E1)] for the hover and active link states.

For the Instagram social media icon I used [Instagram Rose (#E1306C) and Instagram Purple Red (#C13584)] for the hover and active link states.

#### Typography

- Fonts were obtained from Google Fonts, and are applied as follows:
  
    - For H1 and H2 tags it is [Marcellus](https://fonts.google.com/specimen/Marcellus).
    - For all other body text it is [Pontano Sans](https://fonts.google.com/specimen/Pontano+Sans).

#### Imagery

- TBA

## Caveats

- A list of useful points regarding the podcast will be added here, to explain the references on the live site.

## Testing


- Please refer to [TESTING.md](TESTING.md) for details.

## Deployment

- TBA

## Credits

- TBA
    
## Content

- TBA

## Media

- TBA

## Technologies Used

- TBA

## Acknowledgements

- TBA
