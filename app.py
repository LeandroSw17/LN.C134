# importe os módulos necessários
from flask import Flask, render_template, request, jsonify

# importando arquivo sentiment_analysis como sa
import sentiment_analysis as sa

app = Flask(__name__)

# rota do aplicativo para a página index
@app.route('/')
def home():
    return render_template('index.html')

# escreva uma rota para requisição POST
@app.route('/review', methods=['POST'])
def review():
    # Extraia a avaliação do cliente escrevendo a "chave" apropriada dos dados JSON
    data = request.get_json()
    review = data.get('review')

    # Verifique se a avaliação do cliente está vazia, então retorne o erro
    if not review:
        return jsonify({'status': 'error', 'message': 'Avaliação em branco'})

    # Se a avaliação não estiver vazia, passe-a pela função 'predict'.
    # A função predict retorna 2 coisas: o sentimento e o caminho da imagem na pasta static
    sentiment, image_path = sa.predict(review)

    return jsonify({'sentiment': sentiment, 'image_path': image_path})

if __name__ == "__main__":
    app.run(debug=True)
