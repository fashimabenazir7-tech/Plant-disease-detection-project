import os
class Config:
    # Flask configuration
    SECRET_KEY = os.environ.get('SECRET_KEY', 'leaf-disease-detector-super-secret-key-1293')
    
    # Upload folder for leaf images
    UPLOAD_FOLDER = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'static', 'uploads')
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16 MB limit
    
    # Database Settings
    # MySQL default settings (change these for your deployment database)
    MYSQL_HOST = os.environ.get('MYSQL_HOST', 'localhost')
    MYSQL_USER = os.environ.get('MYSQL_USER', 'root')
    MYSQL_PASSWORD =  'fashimaot-7'
    MYSQL_DB = os.environ.get('MYSQL_DB', 'leaf_disease_db')
    
    # SQLite fallback file path if MySQL connection is unavailable
    SQLITE_DB_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'leaf_disease.db')
    
    # Toggle SQLite fallback automatically if True
    AUTO_FALLBACK_SQLITE = True
    # Setup directories
    @staticmethod
    def init_app(app):
        if not os.path.exists(Config.UPLOAD_FOLDER):
            os.makedirs(Config.UPLOAD_FOLDER)
