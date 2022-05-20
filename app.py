from flask import Flask

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return "Oi Amore -- Amo vc!!!! obrigado por fazer parte da minha vida"

if __name__ == '__main__':
    app.run()