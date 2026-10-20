#Importar el módulo flask
import os
from flask import Flask, render_template, url_for, request, redirect
from dotenv import load_dotenv
from werkzeug.utils import secure_filename
#importar MySQL de flask-mysqldb
from flask_mysqldb import MySQL

app = Flask(__name__)

load_dotenv()

db_host = os.getenv("MYSQL_HOST")
db_user = os.getenv("MYSQL_USER")
db_pssw = os.getenv("MYSQL_PASSWORD")
db_name = os.getenv("MYSQL_DATABASE")

#Conexión a la base de datos
app.config['MYSQL_HOST'] = db_host
app.config['MYSQL_USER'] = db_user
app.config['MYSQL_PASSWORD'] = db_pssw
app.config['MYSQL_DB'] = db_name

#Crear un objeto para el uso de métodos de bd en python flask
mysql = MySQL(app)

#port
p = 8000

#rutas
@app.route('/', methods=['GET'])
def index():
    return redirect(url_for('productos'))

@app.route('/productos', methods=['GET'])
def productos():
    #crear un cursor
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM productos')
    #objeto para guardar los resultados que se obtienen de la consulta
    productos = cursor.fetchall()
    #renderizar videojuegos.html y enviar datos de videojuegos en objeto v
    return render_template('productos.html', productos = productos)

@app.route('/agregar_producto', methods=['GET'])
def agregar_producto():
    return render_template('registrar_producto.html')

@app.route('/registrar_producto', methods=['POST'])
def registrar_producto():
    nombre = request.form['nombre']
    descripcion = request.form['descripcion']
    categoria = request.form['categoria']
    precio = request.form['precio']
    imagen = request.files['imagen']

    carpeta_imagenes = os.path.join(app.static_folder, 'imagenes')
    os.makedirs(carpeta_imagenes, exist_ok=True)

    imagen_filename = secure_filename(imagen.filename)

    if imagen_filename:
        imagen.save(os.path.join(carpeta_imagenes, imagen_filename))

    cursor = mysql.connection.cursor()
    cursor.execute(
        "INSERT INTO productos (nombre, categoria, precio, imagen, descripcion) VALUES (%s, %s, %s, %s, %s)", 
        (nombre, categoria, precio, imagen_filename, descripcion)
    )
    mysql.connection.commit()
    
    cursor.close()
    return redirect(url_for('productos'))



#Correr la app
if __name__ == '__main__':
    app.run(debug=False, port=p)