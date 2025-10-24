from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

fundraisers = []

@app.route('/')
def index():
    return render_template('index.html', fundraisers=fundraisers)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        name = request.form['name']
        goal = request.form['goal']
        description = request.form['description']
        fundraisers.append({'name': name, 'goal': goal, 'description': description})
        return redirect(url_for('index'))
    return render_template('add.html')

@app.route('/fundraiser/<name>')
def fundraiser(name):
    f = next((item for item in fundraisers if item["name"] == name), None)
    return render_template('fundraiser.html', fundraiser=f)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
