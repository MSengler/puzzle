from flask import Flask, render_template, redirect, url_for
import os
import divide

app = Flask(__name__)

print(os.getcwd())

@app.route('/')
def index():
    return render_template('pageaccueil.html')


@app.route('/puzzle')
def puzzle():
    return render_template('puzzle.html')

# Route pour exécuter
@app.route('/run-monde')
def run_monde():
    #os.system("python divide.py static/images/Monde.png")
    image_path = "static/images/Monde.png"
    divide.divide_image(image_path, "static/images", 2, 4)
    return redirect(url_for('puzzle'))

@app.route('/run-asie')
def run_asie():
    #os.system("python divide.py static/images/Asie.png")  
    image_path = "static/images/Asie.png"
    divide.divide_image(image_path, "static/images", 2, 4)
    return redirect(url_for('puzzle'))


if __name__ == '__main__':
    app.run(debug=True)
