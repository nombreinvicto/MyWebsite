from flask import Flask, render_template, request

app = Flask(__name__)
app.env = "development"
app.jinja_env.globals['zip'] = zip
app.jinja_env.globals['enumerate'] = enumerate

flaskKwargs = {'debug': True, 'host': '0.0.0.0', 'port': 5005}


@app.route('/')
def get_home_page():
    context = {
        'title': 'Mahmud\'s Homepage'
    }
    return render_template('home.html', **context)


@app.route('/education')
def get_education_page():
    context = {
        'title': 'Education',
    }
    return render_template('education.html', **context)


@app.route('/research')
def get_research_page():
    context = {
        'title': 'Research',
    }
    return render_template('research.html', **context)


@app.route('/experience')
def get_experience_page():
    context = {
        'title': 'Experience',
    }
    return render_template('experience.html', **context)


if __name__ == '__main__':
    app.run(debug=flaskKwargs['debug'],
            host=flaskKwargs['host'],
            port=flaskKwargs['port'])
