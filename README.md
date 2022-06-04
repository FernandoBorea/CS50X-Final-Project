# CS50X Final Project 🎆

Hello everyone and welcome to the Readme file of my final project for the CS50X course! 😀

First and foremost, let me introduce myself. My name is Fernando Borea (you can call me Nando 🤓), my birthdate is July 31st 1998 (23 years old at the time of this writing), and I live in El Salvador, Central America. 

Even though I do have some background in software development, CS50X is the first formal contact I have with web development. It has indeed been a challenge in some aspects (yep, I've thought of throwing  either the computer or myself out of the window at times haha), but an overall amazing and enjoyable experience.

Here is the video summary: https://youtu.be/IbZPAqjF71g.

Enough side chat, let's get to the project! 😎
## Project introduction 📓

I had a ton of ideas for my final project in mind, and I learnt the hard way that a simple first version that is completed is better than a massive project that has tons of things missing or in development for months and months.

Even though this project is being submited for the CS50X course, it is a real-life project for the company where I work! So most likely it will continue to see further improvements and features being added to the platform. In summary, it is starting out as a basic web application that will work as the landing page for the company, with back-end functionality enabling the processing of contact or quote requests that will get forwarded to our team for review.

The main objective is to come up with a clean and modern design for the index page, that is also responsive to any device. The technology sandwich used on the intiial version of the platform is:

* Flask for the back-end functionality
* HTML, CSS, and JavaScript for the front-end
* Bootstrap 5 as the CSS framework

Even though the temptation of choosing a theme instead of building the website from scratch was definitely present, I decided to take on the challenge of creating the website layout from scratch using various components!

## Project structure 🏗

One of the challenges I faced was the project structure. Even though Flask doesn't require a specific project layout, I definitely wanted to use the best practices and set a solid foundation for later development of the platform without having to bang my head on the keyboard —that much— in the process.

I found various tutorials from the [Flask team](https://flask.palletsprojects.com/en/2.1.x/tutorial/), [Microsoft](https://code.visualstudio.com/docs/python/tutorial-flask), among others, however, the one that I used to learn how to structure a Flask project that is able to scale is [this one](https://hackersandslackers.com/series/build-flask-apps/) from Hackers And Slackers, and [this other one](https://www.digitalocean.com/community/tutorial_series/how-to-create-web-sites-with-flask) from Digital Ocean. Also, I made use of [this other](https://www.digitalocean.com/community/tutorial_series/how-to-create-web-sites-with-flask) Spanish tutorial series for some aspects of the platform.

One of the predominant common advice that I found though the material I used as reference is that in order to structure a Flask project that uses the industry best practices is to use a package structure, meaning that the web application itself can be treated as a Python package, as well as the use of virtual environments to easily handle external Python modules.

Speaking of external modules, these are the ones that I used on the project:
* Flask
* Flask-WTF (Yes, I thought the same, but it stands for WhatTheForms 😂)
* Flask-Mail 

Even though the initial version of the platform is a single-page website, I also used Jinja templating to be able to easily add the other features I want to include in the future, such as a log-in page. This is also the reason why within the project structure I make use of a separate folder for the index of the platform.

## Project design 🔥

Let's first start with some screenshots of the first version of the platform! Note that at the moment of creating it, I kept text placeholders and images as I didn't wanted to delay the submission of the project for the CS50X course by waiting until we gather some pictures and material around the office.

![Homepage screenshot](/images/screenshot01.png)

![Form screenshot](/images/screenshot02.png)

I used the various components available on the [Bootstrap documentation](https://getbootstrap.com/) to create the website layout, as well as some snippets from other sources. For example, I used the timeline at the bottom of the website from [this source](https://startbootstrap.com/theme/agency), as well as the design of some of the cards used though the site, which were found on [this other source](https://webpixels.io/).

Lastly, one of the core functionalities is the ability of the back-end to receive forms from the website to then forward the information received on them to an email address. All of the configuration for Flask-Mail and Flask is set into environment variables. Here is an example of the email sent once a form was submitted:

![Email screenshot](/images/screenshot03.png)

## Summary 👨‍🎓

From start to finish, the project took me around 4 weeks (and yep, I was expecting it to take about half of that 👽), taking into account a decent portion of the time was reading through tutorials to learn about the proper way to structure a Flask project as well as using the best practices. Also, another big source of time consumption was in the design of the layout, which was tricky at first but it was well worth the learning experience! 

I hope this repo creates inspiration for you if you are starting out in web development just as I am, and also provides you with useful resources you can check out and use for your future projects too! As David J. Malan would say, this was CS50X Final Project! 🎉