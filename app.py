from flask import Flask
import os, psutil, platform, json


aluno = {
    "aluno 1": "Juliano Teles Tolomini Biasotto",
    "aluno 2": "Geandro Marques da Silva",
    "aluno 3": "Alisson Daledone Hass de Lima"
}


APP = Flask(__name__)

@APP.route("/")
def index():
    return f"""
    <html>
        <head>
            <title>S.O. em Cloud</title>
        </head>
        <body>
            <h1>Caminhos:</h1>
            <ul>
                <li><b>/info</b></li>
                <li><b>/metrica</b></li>
            </ul>
        </body>
    </html>
    """

@APP.route("/info")
def info():
    json_data = json.dumps(aluno, ensure_ascii=False)

    return f"""
    <html>
        <head>
            <title>S.O. em Cloud</title>
        </head>
        <body>
            <h2>{json_data}</h2>
        </body>
    </html
    """

@APP.route("/metrica")
def metrica():
    metricas = {
        "so":platform.platform(),
        "pid":os.getpid(),
        "cpu":psutil.cpu_percent(),
        "memoria_mb":psutil.virtual_memory().used // 1024 ** 2
    }
    json_data = json.dumps(metricas, ensure_ascii=False)
    return f"""
    <html>
        <head>
            <title>S.O. em Cloud</title>
        </head>
        <body>
            <h2>{json_data}</h2>
        </body>
    </html
    """