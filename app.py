from flask import Flask, render_template, redirect, url_for
import os
import divide
import write_html as wh

col_tf, row_tf = 4, 2
col_f, row_f = 8, 4
col_m, row_m = 16, 8
col_d, row_d = 32, 16
col_td, row_td = 64, 32

app = Flask(__name__)

print(os.getcwd())

@app.route('/')
def index():
    return render_template('pageaccueil.html')



@app.route('/puzzle_tf')
def puzzle_tf():
    return render_template(f'puzzles_{row_tf}_{col_tf}.html')

@app.route('/puzzle_f')
def puzzle_f():
    return render_template(f'puzzles_{row_f}_{col_f}.html')





# Route pour exécuter
# Niveaux très facile
@app.route('/run-monde_tf')
def run_monde_tf():
    image_path = "static/images/Monde.png"
    divide.divide_image(image_path, "static/images", row_tf, col_tf)
    wh.generate(row_tf,col_tf)
    return redirect(url_for('puzzle_tf'))

@app.route('/run-asie_tf')
def run_asie_tf():
    image_path = "static/images/Asie.png"
    divide.divide_image(image_path, "static/images", row_tf, col_tf)
    wh.generate(row_tf,col_tf)
    return redirect(url_for('puzzle_tf'))


#Niveau facile
@app.route('/run-monde_f')
def run_monde_f():
    image_path = "static/images/Monde.png"
    divide.divide_image(image_path, "static/images", row_f, col_f)
    wh.generate(row_f,col_f)
    return redirect(url_for('puzzle_f'))

@app.route('/run-asie_f')
def run_asie_f():
    image_path = "static/images/Asie.png"
    divide.divide_image(image_path, "static/images", row_f, col_f)
    wh.generate(row_f,col_f)
    return redirect(url_for('puzzle_f'))


if __name__ == '__main__':
    app.run(debug=True)
