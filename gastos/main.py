from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from routes import expenses_router
from database import connect_to_database, disconnect_from_database


app = FastAPI()

# Configuración CORS para permitir solicitudes desde cualquier origen
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Ruta raíz para verificar que el servidor esté en funcionamiento
@app.get("/")
async def root():
    return {"message": "¡La aplicación de seguimiento de gastos está en funcionamiento!"}

# Registrar las rutas relacionadas con los gastos
app.include_router(expenses_router, prefix="/expenses", tags=["Expenses"])

if __name__ == "__main__":
    connect_to_database()  # Conectarse a la base de datos antes de iniciar el servidor
    uvicorn.run(app, host="0.0.0.0", port=8000)
    disconnect_from_database()  # Desconectarse de la base de datos después de detener el servidor
    