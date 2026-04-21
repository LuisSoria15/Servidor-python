from fastapi import FastAPI
import mysql.connector

print("Server is running... Press Ctrl+C to stop.")

app = FastAPI()

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="Cucusoria1515!",
    database="preguntaslocaldisco"
)

