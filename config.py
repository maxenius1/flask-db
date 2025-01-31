import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY',os.urandom(24))
    SQLALCHEMY_DATABASE_URI = os.getenv('Database_URL','postgresql://neondb_owner:npg_J4fSgT3uRrhY@ep-muddy-scene-a4v8e60v-pooler.us-east-1.aws.neon.tech/neondb?sslmode=require')
    SQLALCHEMY_TRACKMODIFICATIONS = False
