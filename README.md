Study blog project for school Python/Django elective course
===========================================================

Course was read in [Liceum #40, Nizhniy Novgorod, Russia](http://www.lic40nn.edusite.ru/ "Liceum 40 website")

##A short course program description:
* Intoduction to web techlonogies (HTML, Forms, Styles)
* Django basics (templates, models, views)
* Deploying applications. Deploying to Heroku
* Authorization and security
* Caching

##All code is tagged with 'step-x' tags accordign to steps we developed the blog:
* step-0.1 - Just showinng a list of posts. Ability to create posts with admin site.
* step-0.2 - Adding ability to log in and log out from the main page
* step-1 - Prettify frontend. Use bootstrap css framework.
* step-2 - Adding ability to view single post and frontend post editing.
* step-3 - Prettifying frontend. Adding 'cerulean' bootstrap theme
* step-4 - Some minor frontend style changes.
* step-5 - Adding CKEditor WYSIWYG editor in post editing form.
* step-6 - Comments added.
* step-7 - User registration and tracking author of comment.

##How to run this blog on local machine?
* Install [Python 2.x](https://www.python.org/downloads/) (if not already done) 
* Install [PIP (Python Package Index)](https://pip.pypa.io/en/latest/installing.html) Note: 
PIP is already included in Python 2.7.9+
* Install [GIT](http://git-scm.com/downloads)
* Clone this repository
    git clone https://github.com/AlexDobrushskiy/simple_blog.git
* Go to repository directory 
    cd simple_blog
* Install dev-dependencies:
    pip install -r requirements-dev.txt
* Run application
    python manage.py runserver --settings=settings.dev
* Blog should be available on [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
* Note that there is default login/password pair "root//123"    