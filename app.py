from flask import Flask, render_template, request, redirect, url_for
import os
import divide
import write_html as wh


"""
col_f, row_f = 4, 2
col_m, row_m = 6, 3
col_d, row_d = 8, 4
"""

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/images/'
print(os.getcwd())

@app.route('/')
def index():
    return render_template('pageaccueil.html')



@app.route('/puzzle')
def puzzle():
    return render_template(f'puzzles.html')



# Route pour exécuter
# Niveaux facile
@app.route('/run-monde_f')
def run_monde_f():
    image_path = "static/images/Monde.png"
    img_width, img_height, rows, cols = divide.divide_image(image_path, "static/images", "Facile")
    wh.generate(rows, cols, img_width, img_height)
    return redirect(url_for('puzzle'))

@app.route('/run-asie_f')
def run_asie_f():
    image_path = "static/images/Asie.png"
    img_width, img_height,rows, cols = divide.divide_image(image_path, "static/images", "Facile")
    wh.generate(rows, cols, img_width, img_height)
    return redirect(url_for('puzzle'))


# Niveau moyen
@app.route('/run-monde_m')
def run_monde_m():
    image_path = "static/images/Monde.png"
    img_width, img_height, rows, cols = divide.divide_image(image_path, "static/images", "Moyen")
    wh.generate(rows, cols, img_width, img_height)
    return redirect(url_for('puzzle'))

@app.route('/run-asie_m')
def run_asie_m():
    image_path = "static/images/Asie.png"
    img_width, img_height, rows, cols = divide.divide_image(image_path, "static/images", "Moyen")
    wh.generate(rows, cols, img_width, img_height)
    return redirect(url_for('puzzle'))

# Niveau difficile
@app.route('/run-monde_d')
def run_monde_d():
    image_path = "static/images/Monde.png"
    img_width, img_height, rows, cols = divide.divide_image(image_path, "static/images", "Difficile")
    wh.generate(rows, cols, img_width, img_height)
    return redirect(url_for('puzzle'))

@app.route('/run-asie_d')
def run_asie_d():
    image_path = "static/images/Asie.png"
    img_width, img_height, rows, cols = divide.divide_image(image_path, "static/images", "Difficile")
    wh.generate(rows, cols, img_width, img_height)
    return redirect(url_for('puzzle'))


# Import d'images
@app.route("/upload", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        return redirect(url_for("index"))

    file = request.files["file"]
    if file.filename == "":
        return redirect(url_for("index"))

    if file:
        print(file.filename)
        image_path = os.path.join(app.config["UPLOAD_FOLDER"], "Import" )#file.filename
        file.save(image_path)
        img_width, img_height, rows, cols = divide.divide_image(image_path, "static/images", "Moyen")
        wh.generate(rows, cols, img_width, img_height)
        return redirect(url_for("puzzle"))  # Redirige vers la page d'accueil



if __name__ == '__main__':
    app.run(debug=True)
