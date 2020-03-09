# Text Similarity App
## NLP dockerized Flask app

This Flask app measure the cosine of similarity using spaCy.

The app could be deployed with docker cloning this repo and executing the Dockerfile.

From the cloned repository run:

`docker build -t flaskapp .`

Once done you can run the docker with:

`docker run -it -p 5000:5000 flaskapp`

The app can be tested accessing to **localhost:5000** 

It is easy to use, just write two sentences and click on Meassure button to run the function.

![image](https://drive.google.com/uc?export=view&id=1nRJJct-DoyRx8Moe3lPBOSK-OccXUw-h)

Several Unit test can be done by executing:

`python tests.py`

