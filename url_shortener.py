from flask import Flask, redirect, request
import string
import random

app = Flask(__name__)
url_mapping = {}

def generate_short_url():
    characters = string.ascii_letters + string.digits
    short_url = ''.join(random.choice(characters) for _ in range(6))
    return short_url

@app.route('/', methods=['GET', 'POST'])
def shorten_url():
    if request.method == 'POST':
        url = request.form['url']
        if url:
            short_url = generate_short_url()
            url_mapping[short_url] = url
            return f'Short URL: {request.host}/{short_url}'
        return 'Invalid URL'

    return '''
    <form method="post">
        <input type="text" name="url" placeholder="Enter URL" />
        <input type="submit" value="Shorten" />
    </form>
    '''

@app.route('/<short_url>')
def redirect_to_url(short_url):
    if short_url in url_mapping:
        return redirect(url_mapping[short_url])
    return 'URL not found'

if __name__ == '__main__':
    app.run()