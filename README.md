# Sentiment Analysis and Machine Learning App with Python

Building Machine Learning App by using original data on Kaggle (Link below) to understand the process of NLP and deploy by using Flask framework.

If you have any questions, do not hesitate to ask. I'm willing to help.

### Environment
- "requirements.txt" file in "/app" directory is for using with Docker.
- Creating pipeline and others, you could check in "/notebook"


### How to Use
Run with Docker in Terminal to test Sentiment
```
# Pull from my Docker Hub
docker pull northpr/sentiment-flask
# Run the image
docker container run -d -p 5000:5000 northpr/sentiment-flask
# Test the model or you can use with Postman by using 0.0.0.0:5000/predictions
curl -X POST -H "Content-Type: application/json" -d '{"text": "I hate Twitter"}' 0.0.0.0:80/predict
```
Result
```
curl -X POST -H "Content-Type: application/json" -d '{"text": "I hate twitter"}' 0.0.0.0:5000/predict
{
  "label": "Negative",
  "pred": 0,
  "text": "I hate twitter"
}
```

Thanks for watching

Original Data: [Kaggle](https://www.kaggle.com/datasets/kazanova/sentiment140) <br>
Reference: [Youtube - Python Engineer](https://www.youtube.com/watch?v=S--SD4QbGps&t=903s)
