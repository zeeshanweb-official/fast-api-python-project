from pydantic import BaseModel


class UserSchema(BaseModel):
    name: str
    email: str
    password: str

    class Config:
        schema_extra = {
            "example": {
                "name": "M A Zeeshan",
                "email": "zeeshanweb.official@gmail.com",
                "password": "zeeshanPassword"
            }
        }


class UserSchemaWithToken(BaseModel):
    name: str
    email: str
    token: str

    class Config:
        schema_extra = {
            "example": {
                "name": "M A Zeeshan",
                "email": "zeeshanweb.official@gmail.com",
                "token": "alongstringgotfromgoogleoauth"
            }
        }


class UserLoginSchema(BaseModel):
    email: str
    password: str

    class Config:
        schema_extra = {
            "example": {
                "email": "zeeshanweb.official@gmail.com",
                "password": "zeeshanPassword"
            }
        }
