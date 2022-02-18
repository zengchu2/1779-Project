import os


class DevConfig(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    UPLOAD_FOLDER = './image_library'
    ALLOWED_FORMAT = {'jpg', 'jpeg', 'png', 'gif', 'tiff'}
    FILENAME_SEPARATOR = '_'
    DB_CONFIG = {
        'user': 'root',
        'password': 'oplk1998',
        'host': 'localhost',
        'database': 'Assignment_1',
        'table': 'keylist',
        'memcache_stat_table': 'cache_stats',
        'memcache_config_table': 'memcache_config'
    }
    # For initializing connect to mysql
    MYSQL_DATABASE_USER = 'root'
    MYSQL_DATABASE_PASSWORD = 'oplk1998'
    MYSQL_DATABASE_DB = 'Assignment_1'
    MYSQL_DATABASE_HOST = 'localhost'
    # Memcache related macro
    MEMCACHE_SERVER = 'localhost:5001'
