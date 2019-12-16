from . import app

@app.route('/')
def index():
    return "To je Index"