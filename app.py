from flask import Flask, render_template, redirect, url_for
import os
import divide
import write_html as wh

col_f, row_f = 4, 2
col_m, row_m = 8, 4
col_d, row_d = 16, 8


app = Flask(__name__)

print(os.getcwd())

@app.route('/')
def index():
    return render_template('pageaccueil.html')



@app.route('/puzzle_f')
def puzzle_f():
    return render_template(f'puzzles_{row_f}_{col_f}.html')

@app.route('/puzzle_m')
def puzzle_m():
    return render_template(f'puzzles_{row_m}_{col_m}.html')

@app.route('/puzzle_d')
def puzzle_d():
    return render_template(f'puzzles_{row_d}_{col_d}.html')




# Route pour exécuter
# Niveaux facile
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


#Niveau moyen
@app.route('/run-monde_m')
def run_monde_m():
    image_path = "static/images/Monde.png"
    divide.divide_image(image_path, "static/images", row_m, col_m)
    wh.generate(row_m,col_m)
    return redirect(url_for('puzzle_m'))

@app.route('/run-asie_m')
def run_asie_m():
    image_path = "static/images/Asie.png"
    divide.divide_image(image_path, "static/images", row_m, col_m)
    wh.generate(row_m,col_m)
    return redirect(url_for('puzzle_m'))

#Niveau difficile
@app.route('/run-monde_d')
def run_monde_d():
    image_path = "static/images/Monde.png"
    divide.divide_image(image_path, "static/images", row_d, col_d)
    wh.generate(row_d,col_d)
    return redirect(url_for('puzzle_d'))

@app.route('/run-asie_d')
def run_asie_d():
    image_path = "static/images/Asie.png"
    divide.divide_image(image_path, "static/images", row_d, col_d)
    wh.generate(row_d,col_d)
    return redirect(url_for('puzzle_d'))


if __name__ == '__main__':
    app.run(debug=True)
