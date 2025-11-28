import os\nfrom dotenv import load_dotenv\nfrom jose import jwt\nfrom datetime import datetime, timedelta\n
# load environment variables\nload_dotenv()\n

# get environment variables\nSECRET_KEY = os.getenv("SECRET_KEY")\nALGORITHM = os.getenv("ALGORITHM")\nACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))\n

# create a JWT token\ndef create_access_token(data: dict, expires_delta: timedelta | None = None):\n    to_encode = data.copy()\n    if expires_delta:\n        expire = datetime.utcnow() + expires_delta\n    else:\n        expire = datetime.utcnow() + timedelta(minutes=15)\n    to_encode.update({"exp": expire})\n    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)\n    return encoded_jwt\n\n\n# authenticate token\ndef get_user(db: Session, user_id: int):\n    return db.query(models.User).get(user_id)