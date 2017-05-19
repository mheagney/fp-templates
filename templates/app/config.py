# Statement for enabling the development environment
DEBUG = True

# Define the application directory
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Define the database - we are working with
#SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://username:password@localhost/database'
#SQLALCHEMY_DATABASE_URI = 'mysql://username:password@localhost/database'
#SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'app.db')
DATABASE_CONNECT_OPTIONS = {}
SQLALCHEMY_TRACK_MODIFICATIONS = True

# Application threads. A common general assumption is
# using 2 per available processor cores - to handle
# incoming requests using one and performing background
# operations using the other.
THREADS_PER_PAGE = 2

# Enable protection agains *Cross-site Request Forgery (CSRF)*
WTF_CSRF_ENABLED = True

# Use a secure, unique and absolutely secret key for
# signing the data.
CSRF_SESSION_KEY = "secret"

# Secret key for signing cookies
SECRET_KEY = "secretkey"
TOKEN_SALT = 'tokensalt'

# Reset config
# RESET_URL = ''
# ACK_URL = ''
# MAX_AGE = 3600

# EMAIL SETTINGS
# MAIL_SERVER = ''
# MAIL_PORT = 25
# MAIL_USE_SSL = False
# MAIL_USE_TLS = True
# MAIL_USERNAME = ''
# MAIL_PASSWORD = ''
# MAIL_DEFAULT_SENDER = ''

# Site Branding and Title Setup
SITE_HEADER = "Site Header"
SITE_TITLE = "Site Title"
