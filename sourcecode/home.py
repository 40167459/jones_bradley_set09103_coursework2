#SET09103 CW2
#40167459
#Bradley Jones
#20/11/2017
#Imports from the flask
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/home') #Redirects to homepage
def home():
  return render_template('home.html') #Renders the appropriate templates

@app.errorhandler(404) #Error handing, redirects to error screen
def page_not_found(error):
  return "Couldn't find the page you requested.", 404

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
