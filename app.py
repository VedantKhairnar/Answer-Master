from flask import Flask, render_template, redirect, request
import QA as qa

app = Flask(__name__)


@app.route('/')
def redirection():
    return redirect('/home')


@app.route('/home')
def homePage():
    return render_template('index.html')


@app.route('/qapage')
def qapage():
    return render_template('work.html')


@app.route('/predict', methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    passage = request.form['para']
    question = request.form['que']

    sol = qa.findAnswer(passage, question)

    return render_template('ans.html', prediction_text='Answer is: {}'.format(sol))


@app.route('/ans', methods=['POST'])
def ans():
    return render_template('work.html')


if __name__ == "__main__":
    app.debug = True
    app.run()
