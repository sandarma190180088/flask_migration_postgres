from app import app

@app.route('/')
def home():
    return f'Hello world'

