from passlib.context import CryptContext

hash= CryptContext(schemes=["bcrypt"],deprecated="auto")


def Hash(password):
    
    return hash.hash(password)



def vertify(plain_password,userpassword):
    return hash.verify(plain_password,userpassword)