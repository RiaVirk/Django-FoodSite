## HarvardX CS50W: Web Programming with Python and JavaScript

### Course's link

See [here](https://www.edx.org/course/cs50s-web-programming-with-python-and-javascript).

### Final project

My final project is a restaurant website. Users are able to register and after login, user taken to a personalised dashboard where user can edit profile, change password, see orders and logout.

The project was built using Django as a backend framework and JavaScript as a frontend programming language. All generated information are saved in database (SQLite by default).

All webpages of the project are mobile-responsive.

#### Distinctiveness and Complexity

I have make models for all the relevant data and all the data including Profile, Team, Menu Categories, Menu Dishes, Orders and Contact details coming from database instead of just putting all the data in html file. This system makes easier for Superuser to add and delete data from its main dashboard.

Normal client or user without staff level or superuser clearance have its own dashboard with profile update, password change and order details can be viewed there.

Have a message page with nav tab in navbar, but this nav tab can only activate when user is superuser, otherwise this tab is hidden from normal users.

I tried to mix many features in this website like text, pictures, video, google maps. Website is totally responsive and utilize bootstrap framework.

#### Installation

- Install project dependencies by running `pip install -r requirements.txt`. Dependencies include Django and Pillow module that allows Django to work with images.
- Make and apply migrations by running `python manage.py makemigrations` and `python manage.py migrate`.
- Create superuser with `python manage.py createsuperuser`. This step is not optional as superuser is main website admin and controls all data import and booking and feedback messages.

- Go to website address and register an account.

#### Files and directories

- `foodzone` - main application directory.
  - `categories\2023\10` contains all static content for category menu datewise.
    - `14` - Pics loaded on 14th date.
    - `18` - Pics loaded on 18th date.
    - `19` - Pics loaded on 19th date.
  - `dishes\2023\10` contains all static content for dishes datewise.
    - `14` - Pics loaded on 14th date.
    - `18` - Pics loaded on 18th date.
    - `19` - Pics loaded on 19th date.
  - `foodzone` contains all project files.
    - `__pycache__` - All .pyc files of project.
    - `__init__.py` - Init File of the project.
    - `asgi.py` - ASGI config file for project.
    - `setting.py` - Setting file for project. Added app name in INSTALLED_APPS, DATABSE Link, TIME_ZONE, STATIC PATH.
    - `urls.py` - All URLs of the project here.
    - `wsgi.py` - WSGI config file for project.
  - `myapp` - Main APP of the project.
    - `__pycache__` - All .pyc files of app.
    - `migrations` - All migration files of project.
    - `__init__.py` - Init File of the project.
    - `admin.py` - Admin site header, title and index_title changed to foodzone. All models registered here.
    - `apps.py` - App config file.
    - `modals.py` - All database models created here.
    - `tests.py` - App test file.
    - `views.py` - App all data manipulation. All tasks and missions happened here.
  - `profiles\2023\10` - Main folder for profiles static files.
    - `13` - 13th date folder.
    - `14` - 14th date folder.
  - `static` - Main folder for static files.
    - `auth` - Main folder for static files after authentication.
    - `css` - Main CSS folder.
    - `fonts` - Main Fonts folder.
    - `img` - Main Image folder.
    - `js` - Main JavaScript folder.
    - `lib` - Main Libraries folder.
    - `mail` - Main Contact Mail folder.
  - `team` - Main Team Pictures folder.
  - `template` - Main HTML Template folder.
    - `about.html` - About Page for website.
    - `all_dishes.html` - Main Menu page with all the dishes shown here.
    - `base.html` - Base file with all required file tags and Navbar and footer.
    - `contact.html` - Contact page with contact details.
    - `dashboard.html` - Dashboard file for normal user who don’t have staff level account and not a superuser.
    - `dish.html` - Single dish page with availability shown and ordering option.
    - `index.html` - Main homepage file.
    - `login.html` - Login Page.
    - `message.html` - Message page where superuser can see all the booking and feedback messages with name, email, subject and message.
    - `register.html` - User Register Page.
    - `team.html` - Main restaurant team page which is getting data from database..
  - `db.sqlite3` - Main database file.
  - `manage.py` - Main Manage.py file.
  - `README.md` - Main readme file.
  - `requirements.txt` - Main requirements file with all the required packages listed.
  - `README.md` - Main readme file.

#### Running of App

Go to base directory where manage.py located and run command `python manage.py runserver`. Remember to migrate and createsuperuser before this. Live server will be run on addredd : `http://127.0.0.1:8000/`.

#### Ending

It was a fun project but still have alot of room to improvement. I especially thankful to CS50 team and Brian Yu for such a wonderful program. I learned a lot from it. THANK YOU.
