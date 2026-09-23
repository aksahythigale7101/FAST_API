from datetime import timezone

import jwt
from pwdlib import PasswordHash

from app.core.config import settings
from datetime import datetime, timedelta, timezone

password_hash = PasswordHash.recommended()


def hash_password(password: str) -> str:
    return password_hash.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return password_hash.verify(plain_password, hashed_password)


def create_access_token(user_id: int, role: str) -> str:
    expire = datetime.now(timezone.utc) + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)

    payload = {
        "sub": str(user_id),  # sub म्हणजे subject.User ID = 1
        "role": role,  # Authorization साठी पुढे वापरू:
        "exp": expire,  # Token expiry. JWT standard claims मध्ये exp expiration दर्शवतो.
    }
    token = jwt.encode(payload, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return token
