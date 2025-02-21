from abc import abstractmethod, ABC
import db_methods_user_data_service.user_data as userData
from abstractions.data_access import repository


class UserDataService:
    def __init__(self, repo: repository.Repository) -> None:
        self._repo = repo

    def add_new(self, userData_dto: dict) -> userData.UserData:
        return userData.from_db_dto(self._repo.create(userData.UserData.from_web_dto(userData_dto)))

    def update(self, userData_dto: dict) -> userData.UserData:
        self._repo.update(userData.UserData.from_web_dto(userData_dto))
        userData_obj = userData.from_db_dto(self._repo.find_by_id(userData_dto.get("id")))
        return userData_obj

    def delete(self, id: str) -> None:
        self._repo.delete_by_id(id)

    def find_by_id(self, id: str) -> userData.UserData:
        return userData.from_db_dto(self._repo.find_by_id(id))

    def find_all_by_page(self, start_from: str, page_size: int) -> list[userData.UserData]:
        db_dtos = self._repo.find_all_by_page(start_from, page_size)
        userData_dtos = list()
        for dto in db_dtos:
            userData_dtos.append(userData.from_db_dto(dto))
        return userData_dtos
