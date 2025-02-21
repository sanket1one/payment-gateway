import jwt
import time

from app.core.database import JWT_ALGORITHM, JWT_SECRET

class AuthHandler(object):

    @staticmethod
    def sign_jwt(user_id: int) -> str:
        payload = {
            "user_id" : user_id,
            "expires": time.time() + 900
        }

        token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
        return token

    @staticmethod
    def decode_jwt(token: str)-> dict:
        try:
            decoded_token = jwt.decode(token, JWT_SECRET, algorithms = [JWT_ALGORITHM])
            return decoded_token if decoded_token["expires"] >= time.time() else None
        except jwt.ExpiredSignatureError:
            print("Token has expired")
            return None
        except jwt.DecodeError:
            print("Invalid token")
            return None
        except Exception as e:
            print(f"An error occurred: {e}")
            return None