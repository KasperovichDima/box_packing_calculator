# PREREQUISITES
* install **Python 3.11**

# HOW TO DEPLOY
* Download the repo
* Cd to root app folder on your machine
* create virtual environment in root folder using **python3.11 -m venv venv**
* activate your virtual environment using **. /venv/bin/activate**
* Make sure you have **pip** installed in your system using **pip --version**
* If not - install **pip**
* Cd to **/src** folder
* Install dependencies using **pip install -r requirements.txt**
* Run app using **uvicorn main:app**

# HOW TO USE
* When your app is running, open your browser and open **http://127.0.0.1:8000/docs**
* Click on **/calculate** endpoint
* You can see an endpoint description with request and responde examples
* Enjoy!
