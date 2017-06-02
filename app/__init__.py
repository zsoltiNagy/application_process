from flask import Flask

app = Flask(__name__)

# these import statements were put on the end of the file to avoid circular import error
# cause the view module needs to import the app variable defined above
from app import views
