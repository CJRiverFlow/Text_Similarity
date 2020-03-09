from flask import Flask,render_template,url_for,request
from nlp_functions import calculate_similarity

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/find_similarity", methods=['POST'])
def find_similarity():
    if request.method == 'POST':
        sentence1 = request.form['sentence1']
        sentence2 = request.form['sentence2']

        similarity_result, error_message = calculate_similarity(sentence1, sentence2)

        return render_template('index.html', result=similarity_result, error_message=error_message)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)





