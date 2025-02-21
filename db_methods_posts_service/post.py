import abstractions.data_access.data_entity
import abstractions.data_transfer
import uuid
import datetime

DATE_FORMAT = "%y/%m/%d %H:%M:%S"


class Post(abstractions.data_access.data_entity.AbstractEntity, abstractions.data_transfer.Exchangeable):
    """
    Data persistence class for persist a 'posts' data from database. Also for 'dto' producing for web exchange.

    @see method 'to_dto'.

    @see service.PostService class

    @see abstractions.data_access.repository

    """

    def __init__(self, id: str, login: str, email: str, signature_string: str, date: datetime.datetime) -> None:
        self.id = id
        self.login = login
        self.email = email
        self.signature_string = signature_string
        self.date = date

    def from_web_dto(dto: dict):
        if dto.keys().__contains__("id") == True:
            if (dto.get("id") != None) or (dto.get("id") != ""):
                return Post(dto.get("id"), dto.get("login"), dto.get("email"), dto.get("signature_string"),
                            datetime.datetime.strptime(dto.get("date"), DATE_FORMAT))

        return Post(uuid.uuid1(), dto.get("login"), dto.get("email"), dto.get("signature_string"),
                    datetime.datetime.now())

    def get_id_str(self) -> str:
        return str(self.id)

    def to_web_dto(self) -> dict:
        return {
            "id": self.get_id_str(),
            "login": self.login,
            "email": self.email,
            "signature_string": self.signature_string,
            "date": self.date.strftime(DATE_FORMAT)
        }

    def to_db_dto(self) -> dict:
        return {
            "_id": self.get_id_str(),
            "login": self.login,
            "email": self.email,
            "signature_string": self.signature_string,
            "date": self.date.strftime(DATE_FORMAT)
        }


def from_db_dto(dto: dict) -> Post:
    return Post(dto.get("_id"), dto.get("login"), dto.get("email"), dto.get("signature_string"),
                datetime.datetime.strptime(dto.get("date"), DATE_FORMAT))
