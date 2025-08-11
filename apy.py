from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/info')
def info():
    return jsonify({
        "nombre": "Carlos José Blanco Guzmán",
        "cancion_favorita": "Gary vs David (un show mas xd)"
    })

if __name__ == '__main__':
    app.run(debug=True)