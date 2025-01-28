from app import create_app
from waitress import serve

app = create_app()

if __name__ == '__main__':
    print("Server is running on http://localhost:8080")
    serve(app, host='localhost', port=8080)