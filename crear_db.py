import sqlite3

def crear_bd():
    # Conexion a la base de datos
    conexion = sqlite3.connect("web2.sqlite3")
    cursor = conexion.cursor()

    # Eliminar tabla si existe
    cursor.execute("""
        DROP TABLE IF EXISTS libros;
    """)

    # Creacion de la tabla
    cursor.execute("""
        CREATE TABLE libros(
            id INTEGER PRIMARY KEY,
            titulo TEXT NOT NULL,
            autor TEXT NOT NULL,
            genero TEXT NOT NULL,
            fecha_publicacion TEXT NOT NULL,
            precio INTEGER NOT NULL
            cantidad TEXT NOT NULL,
            stock INTEGER NOT NULL
        );
    """)

    # Datos iniciales
    datos = [
        (1, "Cien años de soledad", "Gabriel García Márquez", "Realismo mágico", "1967", 20, 10),
        (2, "El Señor de los Anillos", "J.R.R. Tolkien", "Fantasía", "1954", 25, 8),
        (3, "1984", "George Orwell", "Distopía", "1949", 18, 12),
        (4, "Don Quijote de la Mancha", "Miguel de Cervantes", "Novela", "1605", 22, 5),
        (5, "Harry Potter y la piedra filosofal", "J.K. Rowling", "Fantasía", "1997", 21, 15),
        (6, "Orgullo y prejuicio", "Jane Austen", "Romance", "1813", 19, 9)
    ]

    # Insercion de datos
    cursor.executemany("""
        INSERT INTO libros VALUES(?, ?, ?, ?, ?, ?, ?, ?);
    """, datos)

    # Grabar
    conexion.commit()
    conexion.close()

# Cargar los datos
def cargar_datos():
    crear_bd()
    conexion = sqlite3.connect("web2.sqlite3")
    conexion.row_factory = sqlite3.Row
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT * FROM productos;
    """)

    productos =[dict(producto) for producto in cursor.fetchall()]
    cursor.close()
    conexion.close()

    return productos


