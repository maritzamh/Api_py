from fastapi import FastAPI, HTTPException, Form
from fastapi.responses import HTMLResponse

app = FastAPI()

# Lista de nombres inicial
nombres = ["Juan", "María", "Pedro", "Rosa", "Alvaro"]

# Obtener la lista de nombres en formato HTML
def get_html_nombres():
    html_content = """
    <html>
    <head>
        <title>Lista de Nombres</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f0f0f0;
                padding: 20px;
            }
            h1 {
                color: #333333;
            }
            ul {
                list-style-type: none;
                padding: 0;
            }
            li {
                background-color: #ffffff;
                padding: 10px;
                margin-bottom: 5px;
                border-radius: 5px;
                box-shadow: 2px 2px 5px #888888;
            }
        </style>
    </head>
    <body>
        <h1>Lista de Nombres</h1>
        <ul>
    """

    for nombre in nombres:
        html_content += f"<li>{nombre}</li>"

    html_content += """
        </ul>
        <form action="/agregar_nombre" method="post">
            <input type="text" name="nombre" placeholder="Ingrese un nombre">
            <button type="submit">Agregar Nombre</button>
        </form>
    </body>
    </html>
    """

    return html_content

# Endpoint para obtener la lista de nombres
@app.get("/nombres", response_class=HTMLResponse)
async def obtener_nombres():
    return get_html_nombres()

# Endpoint para agregar un nombre a la lista
@app.post("/agregar_nombre", response_class=HTMLResponse)
async def agregar_nombre(nombre: str = Form(...)):
    if nombre:
        nombres.append(nombre)
        return get_html_nombres()
    else:
        raise HTTPException(status_code=400, detail="El nombre no puede estar vacío")

# Ejecutar la aplicación
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)
