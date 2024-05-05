from flask import Flask, render_template, redirect
from crear_db import cargar_datos

libros = cargar_datos()

#App
app = Flask(__name__)

#Ruta
@app.route('/')
def index():
    return render_template('index.html', datos = libros)


@app.route('/libro/<int:pid>')
def libro(pid):
    for libro in libros:
        if pid == libro["id"]:
            return render_template('libro.html', libro=libro)
        #print(libro["id"])
    return redirect('/')



#Programa princiupal
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
