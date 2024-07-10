from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# Conexión a la base de datos MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="unlamdb"
)
cursor = db.cursor()

# Rutas para el menú de opciones
@app.route('/')
def menu():
    return render_template('index_admin.html')

@app.route('/insertar', methods=['POST'])
def insertar_libro():
    if request.method == 'POST':
        titulo = request.form['titulo']
        autor = request.form['autor']
        # Insertar datos en la tabla de libros
        sql = "INSERT INTO libros (titulo, autor) VALUES (%s, %s)"
        val = (titulo, autor)
        cursor.execute(sql, val)
        db.commit()
        return 'Libro insertado correctamente'

@app.route('/modificar', methods=['POST'])
def modificar_libro():
    if request.method == 'POST':
        id_libro = request.form['id']
        nuevo_titulo = request.form['nuevo_titulo']
        nuevo_autor = request.form['nuevo_autor']
        # Modificar datos en la tabla de libros
        sql = "UPDATE libros SET titulo = %s, autor = %s WHERE id = %s"
        val = (nuevo_titulo, nuevo_autor, id_libro)
        cursor.execute(sql, val)
        db.commit()
        return 'Libro modificado correctamente'

@app.route('/borrar', methods=['POST'])
def borrar_libro():
    if request.method == 'POST':
        id_libro = request.form['id']
        # Borrar libro de la tabla de libros
        sql = "DELETE FROM libros WHERE id = %s"
        val = (id_libro,)
        cursor.execute(sql, val)
        db.commit()
        return 'Libro borrado correctamente'

if __name__ == '__main__':
    app.run()
