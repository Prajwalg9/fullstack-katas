from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/images")
def images():
    app.config['UPLOAD_FOLDER'] = os.path.join('static')
    pic=os.path.join(app.config['UPLOAD_FOLDER'], 'forest.avif')
    return render_template('image.html',user_image=pic)

if __name__ == '__main__':
    app.run(debug=True)