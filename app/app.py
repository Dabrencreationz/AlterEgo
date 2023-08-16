from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def landing():
    return render_template('landing.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/sponsor')
def sponsor():
    return render_template('sponsor.html')

@app.route('/donation')
def donation():
    return render_template('donation.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')


if __name__ == '__main__':
    app.run(debug=True)

