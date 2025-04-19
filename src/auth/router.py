from fastapi import APIRouter, Request

import requests

router = APIRouter(
    prefix="/auth",
)

CLIENT_ID = "m1AvMGC45JfxilxZV1nc0EjlOn7PJuWt"
CLIENT_SECRET = (
    "ATOANgo7barHzQqx3nmD7iqXd9pnt_RTeAuhIxZGwxInaiRYguKMWLa02dUylhadF6moC8E90AC1"
)
REDIRECT_URI = "myapp://oauth2redirect"


@router.post("/token")
async def get_access_token(request: Request):
    authorization_code = request.headers.get("Authorization")
    response = requests.post(
        url="https://auth.atlassian.com/oauth/token",
        data={
            "grant_type": "authorization_code",
            "client_id": CLIENT_ID,
            "client_secret": CLIENT_SECRET,
            "code": authorization_code,
            "redirect_uri": REDIRECT_URI,
        },
    )
    return {
        "access_token": response.json()["access_token"],
        "expires_in": response.json()["expires_in"],
    }
