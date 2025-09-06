from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/info')
def info():
    return jsonify({
        "nombre": "Carlos José Blanco Guzmán",
        "album_favorito": "The Revenge Of Alice Cooper"
    })

if __name__ == '__main__':
    app.run(debug=True)