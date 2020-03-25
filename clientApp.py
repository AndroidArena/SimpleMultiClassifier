from flask import Flask, request, jsonify, render_template
import os
from flask_cors import CORS, cross_origin
from com_utils.utils import decodeImage
from predict import Fruits


os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

app = Flask(__name__)
CORS(app)




#@cross_origin()
class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"
        self.classifier = Fruits(self.filename)



@app.route("/", methods=['GET'])
@cross_origin()
def home():
    return render_template('index.html')
    


@app.route("/predict", methods=['POST'])
@cross_origin()
def predictRoute():
    image = request.json['image']
    decodeImage(image, clApp.filename)
    print("prediction===>>")
    result = clApp.classifier.predictionfruits()
    return jsonify(result)


port = int(os.getenv("PORT",5000))
if __name__ == "__main__":
    clApp = ClientApp()
    app.run(host='127.0.0.1', port=port,threaded=False)
    #app.run(host='127.0.0.1', port=5000, debug=False,threaded=False)
