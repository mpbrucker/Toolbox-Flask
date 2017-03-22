"""
A simple flask app.
"""

from flask import Flask, request, render_template
app = Flask(__name__)
all_names = ["MattyB"]

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_name = request.form['name']
        user_age = request.form['age']
        if user_name is not '' and user_age is not '':
            return render_template('profile.html', name=user_name, age=user_age)
        else:
            return render_template('error.html')


if __name__ == '__main__':
    app.run()
