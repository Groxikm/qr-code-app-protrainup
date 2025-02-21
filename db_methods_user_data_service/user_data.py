import abstractions.data_access.data_entity
import abstractions.data_transfer
import uuid
import datetime

DATE_FORMAT = "%y/%m/%d %H:%M:%S"


class UserData(abstractions.data_access.data_entity.AbstractEntity, abstractions.data_transfer.Exchangeable):
    """
    Data persistence class for persist a 'posts' data from database. Also for 'dto' producing for web exchange.

    @see method 'to_dto'.

    @see service.PostService class

    @see abstractions.data_access.repository

    """

    def __init__(self, id: str, name: str, surname: str, login: str, password: str,
                 visit_frequency: str, valid_due: datetime.datetime, login_sessions: list, avatar_link: str) -> None:
        self.id = id
        self.name = name
        self.surname = surname
        self.login = login
        self.password = password
        self.visit_frequency = visit_frequency
        self.valid_due = valid_due
        self.login_sessions = login_sessions
        self.avatar_link = avatar_link

    def from_web_dto(dto: dict):
        if dto.keys().__contains__("id") == True:
            if (dto.get("id") != None) or (dto.get("id") != ""):
                return UserData(dto.get("id"), dto.get("name"), dto.get("surname"), dto.get("login"), dto.get("password"),
                                dto.get("visit_frequency"),
                                datetime.datetime.strptime(dto.get("valid_due"), DATE_FORMAT),
                                dto.get("login_sessions"))

        return UserData(uuid.uuid1(), dto.get("name"), dto.get("surname"), dto.get("login"), dto.get("password"),
                                dto.get("visit_frequency"),
                                datetime.datetime.strptime(dto.get("valid_due"), DATE_FORMAT),
                                dto.get("login_sessions"))

    def get_id_str(self) -> str:
        return str(self.id)

    def to_web_dto(self) -> dict:
        return {
            "id": self.get_id_str(),
            "name": self.name,
            "surname": self.surname,
            "login": self.login,
            "password": self.password,
            "visit_frequency": self.visit_frequency,
            "valid_due": self.valid_due.strftime(DATE_FORMAT),
            "login_sessions": self.login_sessions,
            "avatar_link": self.avatar_link,
        }

    def to_db_dto(self) -> dict:
        return {
            "id": self.get_id_str(),
            "name": self.name,
            "surname": self.surname,
            "login": self.login,
            "password": self.password,
            "visit_frequency": self.visit_frequency,
            "valid_due": self.valid_due.strftime(DATE_FORMAT),
            "login_sessions": self.login_sessions,
            "avatar_link": self.avatar_link,
        }


def from_db_dto(dto: dict) -> UserData:
    return UserData(uuid.uuid1(), dto.get("name"), dto.get("surname"), dto.get("login"), dto.get("password"),
                                dto.get("visit_frequency"),
                                datetime.datetime.strptime(dto.get("valid_due"), DATE_FORMAT),
                                dto.get("login_sessions"))
