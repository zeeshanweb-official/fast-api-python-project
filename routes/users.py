from fastapi import APIRouter, Response, status

from config.database import connection
from models.users import users
from schemas.users import UserSchema, UserSchemaWithToken, UserLoginSchema
from utils.password import signJWT, decodeJWT
user = APIRouter()


@user.post("/signup", tags=["user", "signup"], status_code=200)
async def create_user(user: UserSchema, response: Response):
    try:
        connection.execute(users.insert().values(
            name=user.name,
            email=user.email,
            password=user.password
        ))
        response.status_code = status.HTTP_201_CREATED
        return user
    except Exception as err:
        print(err)
        response.status_code = status.HTTP_406_NOT_ACCEPTABLE
        return {"message": err.statement, "params": err.params}


@user.post("/signup-with-oauth", tags=["user", "signup", "oauth"], status_code=200)
async def create_user(user: UserSchemaWithToken, response: Response):
    try:
        fuser = connection.execute(users.select().where(
            users.c.email == user.email)).first()
        if fuser is None:
            connection.execute(users.insert().values(
                name=user.name,
                email=user.email
            ))
            response.status_code = status.HTTP_201_CREATED
        else:
            if (fuser.email == user.email):
                response.status_code = status.HTTP_200_OK
        return {"message": 'success'}
    except Exception as err:
        print(err)
        response.status_code = status.HTTP_406_NOT_ACCEPTABLE
        return {"message": err.statement, "params": err.params}


@ user.post("/login", tags=["user", "login"], status_code=200)
async def login_user(user: UserLoginSchema, response: Response):
    fuser = connection.execute(users.select().where(
        users.c.email == user.email)).first()
    if (fuser):
        if (user.password == fuser.password):
            response.status_code = status.HTTP_200_OK
            return fuser
        else:
            response.status_code = status.HTTP_401_UNAUTHORIZED
            return {"message": "password missmatch"}
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"message": "user not found"}
