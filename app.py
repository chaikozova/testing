from flask import Flask, render_template, url_for
app = Flask(__name__)


abouts = [
    {
        'name': 'Elena Chegibaeva',
        'position': 'Co-founder'
    },
    {
        'name': 'Nazira Sheraly',
        'position': 'Co-founder'
    },
    {
        'name': 'Jazgul',
        'position': 'Coordinator'
    }
]


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/news')
def news_page():
    text = 'Привет, я Роза'
    return render_template('news.html', titel='News', text=text)


@app.route('/about')
def about_page():
    return render_template('about.html',titel='About us', abouts=abouts)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="8000")
