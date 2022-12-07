# CodeClan Project - AdventureGrid Admin Panel

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#adventuregrid-admin-panel">Project Brief</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- PROJECT BRIEF -->
### AdventureGrid Admin Panel

Build an app which allows the admin of the website AdventureGrid to manage their users and experiences. AdventureGrid is an ecommerce site that shares/sells local experience packages in a B2C format. As an extension, also build the landing page for AdventureGrid which displays the data.

#### MVP

* It should store and track individual experiences, including a name, description, location, image and whether or not it is the featured experience (displayed at the top of the landing page).
* It should store and track users, including a name, email and username.
* The admin should be able to create and edit users and experiences separately.
* Show an dashboard page, listing all the details for all the experiences in a single view.
* The admin should be able to edit these items, change the featured experience, and delete experiences and users.

#### Inspired by

Shopify, Itison, Groupon, etc.

#### Possible Extensions

* Add reviews of experiences from the members, which can be viewed in the admin panel, but should not be allowed to edit or delete.
* Within a user, view the list of experiences, and vice versa.

### Advanced Extension
* Create a landing page for the AdventureGrid site, pulling a grid of experiences, a list of users showing how many experiences they have been on, and displaying the featured experience, and a review as well.


## Design
I designed the Figma file for AdventureGrid in 2021 whilst practicing UX design in Figma for the Google UX Design certification. You can view the landing page here:
* Design File - [Figma](https://www.figma.com/file/6y3NfwIqNHi1d9CFf0avwn/AdventureGrid-Design-File?node-id=0%3A1&t=LkN4g6GFA7sTKZwt-1)

This project was a continuation of this project, building out the admin dashboard for AdventureGrid, which I built and designed from scratch, using inspiration from the design file above. As an extension, I also built out the landing page shown.


<!-- BUILT WITH -->
## Built With

* HTML
* CSS
* Python
* Flask
* Postgresql



<!-- GETTING STARTED -->
## Getting Started
### Prerequisites

To run this app, you must install: 
* psychopg
  ```sh
  pip3 install psycopg2
  ```

* Flask
  ```sh
  pip3 install Flask
  ```

* Postgresql



### Installation

1. Clone the repository
   ```sh
   git clone https://github.com/kelsiesmurphy/CC_Project_AdventureGrid.git
   ```
2. Navigate to the folder using terminal
3. Create the database
   ```sh
   psql -d experience_manager -f db/experience_manager.sql
   ```
4. Seed the database with pre-set data by running the console.py file
   ```sh
   python3 console.py
   ```
5. Run Flask
   ```sh
   flask run
   ```
6. Open in browser (Google Chrome is recommended): http://127.0.0.1:4999
7. To stop the server enter ctrl + c in your Terminal



<!-- CONTACT -->
## Contact

Kelsie Murphy - [LinkedIn](https://www.linkedin.com/in/kelsiesmurphy/) - [Twitter](https://twitter.com/kelsiesmurphy)

Project Link: [https://github.com/kelsiesmurphy/CC_Project_AdventureGrid](https://github.com/kelsiesmurphy/CC_Project_AdventureGrid)

<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements

Support, guidance and instructors at [CodeClan](https://codeclan.com/)

All images from [Pexels.com](https://www.pexels.com/)

All icons from [UntitledIcons](https://www.untitledui.com/icons)