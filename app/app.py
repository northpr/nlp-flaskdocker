from flask import Flask,jsonify,request
from ultilities import predict_pipeline

app = Flask(__name__)


@app.post('/predict')
def predict():
    data = request.json
    # Error Checking Input
    try:
        sample = data['text'] # json file with the key text
    except KeyError:
        return jsonify({'error': 'no text sent'})

    sample = [sample]
    predictions = predict_pipeline(sample)

    # Error Checking Output
    try:
        result = jsonify(predictions[0])
    except TypeError as e:
        return jsonify({'error':str(e)})
    return result

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)