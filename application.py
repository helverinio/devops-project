from app import create_app
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

app = create_app()

# Elastic Beanstalk expects `application`
application = app

if __name__ == '__main__':
    # Get port with fallback handling
    port = os.environ.get('FLASK_PORT', '5000')
    if not port or port == '':
        port = '5000'
    
    app.run(
        host=os.environ.get('FLASK_HOST', '0.0.0.0'),
        port=int(port),
        debug=os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'
    )
