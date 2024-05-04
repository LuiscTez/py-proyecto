from flask import Flask, render_template, redirect
from crear_db import cargar_datos

libros = cargar_datos()

#App
app = Flask(__name__)

#Ruta
@app.route('/')
def index():
    return render_template('index.html', datos = libros)


# @app.route('/producto/<int:pid>')
# def producto(pid):
#     for producto in productos:
#         if pid == producto['id']:
#             return render_template('producto.html', producto=producto)
#     return redirect('/')



#Programa princiupal
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
