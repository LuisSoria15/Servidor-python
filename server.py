from fastapi import FastAPI
import mysql.connector

app = FastAPI()

# Tus credenciales centralizadas
DB_CONFIG = {
    "host": "127.0.0.1",
    "user": "root",
    "password": "Cucusoria1515!",
    "database": "preguntaslocaldisco"
}

@app.get("/categorias")
def obtener_todas_las_categorias():
    conexion = None
    try:
        conexion = mysql.connector.connect(**DB_CONFIG)
        cursor = conexion.cursor(dictionary=True)
        
        cursor.execute("SELECT id, nombre, IMAGEN FROM categorias ORDER BY id ASC")
        return cursor.fetchall()
        
    except Exception as e:
        return {"error": str(e)}
    finally:
        if conexion and conexion.is_connected():
            cursor.close()
            conexion.close()

@app.get("/opciones")
def obtener_todas_las_opciones():
    conexion = None
    try:
        conexion = mysql.connector.connect(**DB_CONFIG)
        cursor = conexion.cursor(dictionary=True)
        
        cursor.execute("SELECT id, categoria_id, enunciado, formato FROM opciones ORDER BY id ASC")
        return cursor.fetchall()
        
    except Exception as e:
        return {"error": str(e)}
    finally:
        if conexion and conexion.is_connected():
            cursor.close()
            conexion.close()