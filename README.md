# PREREQUISITES
1. install **Python 3.11** if not installed

# HOW TO DEPLOY
2. Download the repo
3. Cd to root app folder on your machine
4. create virtual environment in root folder using **python3.11 -m venv venv**
5. activate your virtual environment using **. /venv/bin/activate**
6. Make sure you have **pip** installed in your system using **pip --version**
7. If not - install **pip**
8. Cd to **/src** folder
9. Install dependencies using **pip install -r requirements.txt**
10. Run app using **uvicorn main:app**

# HOW TO USE
11. When your app is running, open your browser and open **http://127.0.0.1:8000/docs**
12. Click on **/calculate** endpoint
13. You can see an endpoint description with request and response examples
14. Enjoy!