import mysql.connector

conexion1=mysql.connector.connect(host="localhost", user="root", passwd="", database="unlamdb")
cursor=conexion1.cursor()
cursor.execute("show databases")
for base in cursor:
    print(base)
#conexion1.close() 

# Instalar con pip install Flask
from flask import Flask, request, jsonify, render_template
from flask import request

# Instalar con pip install flask-cors
from flask_cors import CORS

print(0)

#--------------------------------------------------------------------

from flask import Flask, render_template, request
app = Flask(__name__)




app = Flask(__name__)
CORS(app)  # Esto habilitará CORS para todas las rutas
host="localhost"
user="root"
password=""
database="unlamdb"
print(1)
#--------------------------------------------------------------------
class Catalogo:
    #----------------------------------------------------------------
    # Constructor de la clase
    def __init__(self, host, user, password, database):
        print(2)
        # Primero, establecemos una conexión sin especificar la base de datos
        self.conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            
        )
        
        self.cursor = self.conn.cursor()

        # Intentamos seleccionar la base de datos
        try:
            self.cursor.execute(f"USE {database}")
        except mysql.connector.Error as err:
            # Si la base de datos no existe, la creamos
            if err.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
                self.cursor.execute(f"CREATE DATABASE {database}")
                self.conn.database = database
                print(3)
            else:
                raise err
            print(4)

        # Una vez que la base de datos está establecida, creamos la tabla si no existe
        self.cursor.execute('''CREATE TABLE `libros` (
            `id` varchar(8) NOT NULL,
            `descripcion` text NOT NULL,
  `idioma` text NOT NULL,
  `tipo` text NOT NULL,
  `ubicacion` text NOT NULL,
  `instrumento_asociado` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

)''')
        self.conn.commit()

        # Cerrar el cursor inicial y abrir uno nuevo con el parámetro dictionary=True
        self.cursor.close()
        self.cursor = self.conn.cursor(dictionary=True)
        print(5)
    #----------------------------------------------------------------
    def agregar_libro(self, libro_id, descripcion, idioma, tipo, ubicacion, instrumento_asociado ):
               
        sql = "INSERT INTO libros (id, descripcion, idioma, tipo, ubicacion, instrumento_asociado) VALUES (%s, %s, %s, %s, %s)"
        valores = (libro_id, descripcion, idioma, tipo, ubicacion, instrumento_asociado)

        self.cursor.execute(sql, valores)        
        self.conn.commit()
        return self.cursor.lastrowid
    

    #----------------------------------------------------------------
    def consultar_libro(self, libro_id):
        # Consultamos un producto a partir de su código
        self.cursor.execute(f"SELECT * FROM libros WHERE codigo = {libro_id}")
        return self.cursor.fetchone()

    #----------------------------------------------------------------
    def modificar_libro(self, n_libro_id, n_descripcion, n_idioma, n_tipo, n_ubicacion, n_instrumento_asociado):
        sql = "UPDATE libros SET descripcion = %s, cantidad = %s, precio = %s, imagen_url = %s, proveedor = %s WHERE codigo = %s"
        valores = (n_libro_id, n_descripcion, n_idioma, n_tipo, n_ubicacion, n_instrumento_asociado)
        self.cursor.execute(sql, valores)
        self.conn.commit()
        return self.cursor.rowcount > 0

    #----------------------------------------------------------------
    def listar_libros(self):
        self.cursor.execute("SELECT * FROM libros")
        libros = self.cursor.fetchall()
        return libros

    #----------------------------------------------------------------
    def eliminar_libros(self, libro_id):
        # Eliminamos un producto de la tabla a partir de su código
        self.cursor.execute(f"DELETE FROM libros WHERE codigo = {libro_id}")
        self.conn.commit()
        return self.cursor.rowcount > 0

    #----------------------------------------------------------------
    def mostrar_libro(self, libro_id):
        # Mostramos los datos de un producto a partir de su código
        libro = self.consultar_libro(libro_id)
        if libro:
            print("-" * 40)
            print(f"Id.....: {libro['libro_id']}")
            print(f"Descripción: {libro['descripcion']}")
            print(f"Idioma...: {libro['idioma']}")
            print(f"Tipo.....: {libro['tipo']}")
            print(f"Ubicacion.....: {libro['ubicacion']}")
            print(f"Instrumento Asociado..: {libro['instrumento_asociado']}")
            print("-" * 40)
        else:
            print("librp no encontrado.")

# # Rutas para el menú de opciones
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def form():
    return render_template('cambio-bib.html')

@app.route('/')
def menu():
    return render_template('index_admin.html')

@app.route('/libros/insertar', methods=['POST'])
def insertar_libro():
    if request.method == 'POST':
        nid = request.form['id']
        ndesc= request.form['descripcion']
        nidioma= request.form['idioma']
        ntipo = request.form['tipo']
        nubicacion= request.form['ubicacion']
        ninst_asoc= request.form['instrumento_asociado']
# Insertar datos en la tabla de libros
        sql = "INSERT INTO libros (titulo, autor) VALUES (%s, %s)"
        val = (nid,ndesc,nidioma,ntipo,nubicacion,ninst_asoc)
        cursor.execute(sql, val)
        return 'Libro insertado correctamente'

@app.route('/modificar', methods=['POST'])
def modificar_libro():
    if request.method == 'POST':
        nid = request.form['id']
        ndesc= request.form['descripcion']
        nidioma= request.form['idioma']
        ntipo = request.form['tipo']
        nubicacion= request.form['ubicacion']
        ninst_asoc= request.form['instrumento_asociado']
        # Modificar datos en la tabla de libros
        sql = "UPDATE libros SET titulo = %s, autor = %s WHERE id = %s"
        val = (nid,ndesc,nidioma,ntipo,nubicacion,ninst_asoc)
        cursor.execute(sql, val)
    # self.conn.commit()
        return 'Libro modificado correctamente'

@app.route('/borrar', methods=['POST'])
def borrar_libro():
    if request.method == 'POST':
        id_libro = request.form['id']
        # Borrar libro de la tabla de libros
        sql = "DELETE FROM libros WHERE id = %s"
        val = (id_libro,)
        cursor.execute(sql, val)
        # db.commit()
        return 'Libro borrado correctamente'

# # if __name__ == '__main__':
# #     app.run() """
