from fastapi_users.authentication import CookieTransport, AuthenticationBackend, JWTStrategy
from config import SECRET_KEY


cookie_transport = CookieTransport(cookie_max_age=360)

SECRET = SECRET_KEY


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET, lifetime_seconds=3600, algorithm="HS256")

auth_backend = AuthenticationBackend(
    name="jwt_auth",
    transport=cookie_transport,
    get_strategy=get_jwt_strategy,
)
