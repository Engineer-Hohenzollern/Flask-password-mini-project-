from flask import *
# welcome page

app=Flask(__name__)

@app.route('/')
def hello_flask():
 x = "Welcome you have successfully logged in to your account  █▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█"
 return x

if __name__=="__main__":
    app.run(debug=True)
    
"""the output of this code will generate an address when we enter this address in the browser or click on the link, 
The python/flask program which is running on the desktop will check if the route exists in our program if found the function right underneath the rout would be executed 
and the output would be sent to the browser to be displayed."""
