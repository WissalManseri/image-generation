from flask import Flask, render_template, request
from PIL import Image
import numpy as np
import io
import base64
import matplotlib.pyplot as plt
import tensorflow as tf

# Chargement du modèle
model = tf.keras.models.load_model('model.h5')

app = Flask(__name__)

# Page d'accueil
@app.route('/')
def index():
    return render_template('index.html')

# Traitement du formulaire
@app.route('/', methods=['POST'])
def generate_image():
    # Récupération des données du formulaire
    size = int(request.form['size'])
    color = request.form['color']

    # Génération de l'image
    img = generate_random_image(size, color)
    
    # Préparation de l'image pour l'affichage sur la page
    plt.imshow(img)
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    img_base64 = base64.b64encode(buf.read()).decode('utf-8')
    return render_template('index.html', img_data=img_base64)

# Génération de l'image aléatoire
def generate_random_image(size, color):
    img = np.random.rand(size, size, 3) * 255
    if color == 'red':
        img[:, :, 1] = 0
        img[:, :, 2] = 0
    elif color == 'green':
        img[:, :, 0] = 0
        img[:, :, 2] = 0
    elif color == 'blue':
        img[:, :, 0] = 0
        img[:, :, 1] = 0
    else:
        img = np.random.rand(size, size, 3) * 255
    img = img.astype(np.uint8)
    return img

if __name__ == '__main__':
    app.run(debug=True)
