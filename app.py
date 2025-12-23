from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
load_dotenv()
import os
from controllers.login_controller import login_bp
from controllers.registration_controller import registration_bp
from controllers.query_controller import query_bp
from controllers.voice_query_controller import voice_query_bp
app = Flask(__name__)
CORS(app)
# Enable CORS for all routes
# Register blueprints
app.register_blueprint(login_bp)
app.register_blueprint(registration_bp)
app.register_blueprint(query_bp, url_prefix='/api')
app.register_blueprint(voice_query_bp, url_prefix='/api')
@app.route('/')
def home():
    return {
        "message": "MCP RAG Service API",
        "endpoints": {
            "POST /api/query": "Submit a query",
            "GET /api/health": "Health check"
        }
    }
if __name__ == '__main__':
    # Ensure documents directory exists
    os.makedirs('documents', exist_ok=True)
    
    print(" Starting MCP RAG Service...")
    print(" Documents directory: ./documents")
    print(" Server running on http://localhost:5000")
    
    app.run(debug=True, host='0.0.0.0', port=5000)