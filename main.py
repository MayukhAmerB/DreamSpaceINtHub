import os
from app import create_app
from waitress import serve

app = create_app()

if __name__ == '__main__':
    # Retrieve the port dynamically from the PORT environment variable
    # Default to 8080 if not provided
    port = int(os.environ.get("PORT", 11000))

    print(f"Server is running on port {port}")
    # Bind to '0.0.0.0' to allow external access
    serve(app, host='0.0.0.0', port=port)