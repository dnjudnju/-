from flask import Flask, render_template, request
from flask_wtf.csrf import CSRFProtect
import random

app = Flask(__name__)
csrf = CSRFProtect(app)

def shuffle_words(input_text):
    words = input_text.split()  # 単語に分割
    random.shuffle(words)  # 単語をシャッフル
    shuffled_text = ' '.join(words)  # シャッフルされた単語を連結
    return shuffled_text

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        input_text = request.form['input_text']
        shuffled_text = shuffle_words(input_text)
        return render_template('result.html', input_text=input_text, shuffled_text=shuffled_text)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=8888)


