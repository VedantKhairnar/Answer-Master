from flask import Flask, render_template, redirect, request
import QA as qa

app = Flask(__name__)


@app.route('/answer', methods=['POST'])
def recommend():
    if request.method == "POST":
        passage = request.form['passage']
        question = request.form['question']
        answer = qa.findAnswer(passage, question)
    return render_template('index.html', answer=answer)


@app.route('/')
def redirection():
    return redirect('/home')


@app.route('/home')
def homePage():
    return render_template('index.html')


if __name__ == '__main__':
    app.debug = True
    app.run()
