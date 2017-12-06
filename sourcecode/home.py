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

@app.route('/about') #Redirects to the about page
def about():
  return render_template('about.html') # Renders the master template

@app.route('/contact')
def contact():
  return render_template('contact.html') #Renders the contact template

@app.route('/services') #Redirects to the appropriate page
def services():
  return render_template('services.html') #Renders the master template

@app.errorhandler(404) #Error handing, redirects to error screen
def page_not_found(error):
  return "Couldn't find the page you requested.", 404

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
