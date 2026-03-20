# Import the Flask class from the flask module
# Flask is the main class that will create your web application
from flask import Flask

# Create an instance of the Flask class
# __name__ is a special Python variable that gets the name of the current module
# Flask uses this to locate resources like templates and static files
app = Flask(__name__)

# At this point, you have a Flask application object called 'app'
# This object will handle all the routing and HTTP requests


# The @app.route() decorator binds a URL to a Python function
# "/" means this function will run when someone visits the root URL (homepage)
@app.route("/")
def hello_world():
    # This function is called a "view function"
    # Whatever it returns will be sent to the user's browser
    return "<h1>Hello, World!</h1>"

# You can create multiple routes for different pages
@app.route("/about")
def about():
    # This function runs when someone visits yoursite.com/about
    return "<h1>About Page</h1>"

# Routes can also accept variables from the URL
@app.route("/user/<username>")
def show_user(username):
    # <username> in the route captures the URL part and passes it to the function
    # Example: /user/john will pass "john" as the username parameter
    return f"<h1>User Profile: {username}</h1>"

# Add this at the end of your app.py file
# This ensures the code only runs when you execute this file directly
if __name__ == "__main__":
    # app.run() starts the development server
    # debug=True enables automatic reloading and shows detailed error messages
    # Never use debug=True in production!
    app.run(debug=True)
    
    # By default, the server runs on http://127.0.0.1:5000
    # You can customize the host and port like this:
    # app.run(debug=True, host='0.0.0.0', port=8080)
