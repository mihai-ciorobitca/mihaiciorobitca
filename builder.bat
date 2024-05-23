@echo off

:: Create directory and navigate into it
mkdir Testing
cd Testing

:: Create and populate the uploader.bat file
echo git init > uploader.bat
echo git add . >> uploader.bat
echo git remote add origin https://github.com/mihai-ciorobitca/Testing >> uploader.bat
echo git push origin master >> uploader.bat

:: Create a gitignore amd populate it
echo .venv > .gitignore
echo __pycache__ >> .gitignore

:: Create and populate the vercel.json file
echo {^
    "rewrites":[ { ^
            "source": "/(.*)",^
            "destination": "/api/main"^
        }^
    ]^
} > vercel.json

:: Create and populate the package.json file
echo {^
    "engines": {^
        "node": "18.x"^
    }^
} > package.json

:: Create and populate the requirements.txt file
echo Flask > requirements.txt

:: Set up the Python virtual environment and install requirements
python -m venv .venv
.venv\Scripts\activate

pip install -r requirements.txt

:: Create the api directory and main.py file
mkdir api
cd api
echo from flask import Flask > main.py

:: Create the templates directory and index.html file
mkdir templates
cd templates
echo > index.html

:: Navigate back to the inital directory and run uploader.bat
cd ../..
call uploader.bat
