Hacker News Clone
===================

This exercise is to create your own [Hacker News](http://news.ycombinator.com) clone from scratch (i.e. creating the Django project, setting up DB, creating models, settings up static files, etc). So to get started, let's install Windows and get Dreamweaver fired up, we're on a time travel trip back to 1999! Just kidding. Using modern conventions and technologies, ours will be better than the real thing - other than the users and content and respected name of course. How you want to design your hacker news clone is mostly up to you, but here are some suggestions:

* It is meant to incorporate many of the skills we learned this month.
* If you can do this, you can **most likely** pass the assessment and move on to phase 3.
* Feel free to work together for the planning / pseudo coding / wireframing
* HOWEVER, I would like for this prompt to be done solo on your own branches.

### Models

Go through Hacker News thoroughly and get the flow. We're going to need at least these models from Hacker News that need to built out and displayed:

    Posts
    Users
    Comments

### Things to keep in mind

- Go through Hacker News thoroughly and get the flow.
- Make sure you are using PostgrsSQL
- Create a seeds file so you have some data to work with. Use [Faker](https://github.com/joke2k/faker) and random numbers. (!!!! this will save you a lot of time when resetting your DB)
- Work on your CSS skills - make your site as visually close to Hacker News as possible.
- Make a simple user login / registration or integrate one of your other user modules.
- Implement AJAX for a seamless UI/UX


### BONUS:
- Are your comments commentable? That is, can a user comment on a comment? If not, implement this feature! What knid of relation can we use to implement nested comments? Do some googling, but definitely, don't use any built in libraries. Build it from scratch!
