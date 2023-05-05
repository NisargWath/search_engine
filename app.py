from flask import Flask, render_template, request
import wikipediaapi
import wikipedia

app = Flask(__name__)
wiki = wikipediaapi.Wikipedia('en')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search')
def search():
    query = request.args.get('query')
    summary = wikipedia.summary(query)
    print(summary)
    return render_template('results.html', summary=summary)

if __name__ == '__main__':
    app.run(debug=True)
