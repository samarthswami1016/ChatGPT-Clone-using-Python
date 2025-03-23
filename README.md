## ChatGPT Clone
feel free to improve the code / suggest improvements

<img width="1470" alt="image" src="https://github.com/samarthswami1016/ChatGPT-Clone-using-Python/blob/main/images/Demo.png">


## Getting Started
To get started with this project, you'll need to clone the repository and set up a virtual environment. This will allow you to install the required dependencies without affecting your system-wide Python installation.

### Prequisites
Before you can set up a virtual environment, you'll need to have Python installed on your system. You can download Python from the official website: https://www.python.org/downloads/

### Cloning the Repository
Run the following command to clone the repository:
```
git clone https://github.com/samarthswami1016/ChatGPT-Clone-using-Python.git
```

### Setting up a Virtual Environment
To set up a virtual environment, follow these steps:

1. Navigate to the root directory of your project.
```
cd ChatGPT-Clone-using-Python
```
2. Run the following command to create a new virtual environment:
```
python -m venv venv
```
3.  Activate the virtual environment by running the following command:
```
source venv/bin/activate
```
If you are using fish shell, the command will be slightly different:
```
source venv/bin/activate.fish
```
If you're on Windows, the command will be slightly different:
```
venv\Scripts\activate
```
4. Install the required dependencies by running the following command:
```
pip install -r requirements.txt
```

### Running the Application
To run the application, make sure the virtual environment is active and run the following command:
```
python run.py
```
