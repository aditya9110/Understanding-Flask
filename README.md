## Simple Flask Program

## What is Flask?
- Flask is a web framework for Python users.
- It is based on Werkzeug WSGI toolkit and Jinja2 template engine.
- It has a development server to testing and debugging.

**The code looks like this:**
```py
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('weather.html')


if __name__ == "__main__":
    app.run(debug=True)
```

## Output:
- I have linked a html file which provides the following output:

![output](https://github.com/aditya9110/Understanding-Flask/blob/main/output.PNG)


