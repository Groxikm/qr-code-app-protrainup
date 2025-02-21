from abc import abstractmethod, ABC
import db_methods_posts_service.post as post
from abstractions.data_access import repository


class PostsService:
    def __init__(self, repo: repository.Repository) -> None:
        self._repo = repo

    def add_new(self, post_dto: dict) -> post.Post:
        return post.from_db_dto(self._repo.create(post.Post.from_web_dto(post_dto)))

    def update(self, post_dto: dict) -> post.Post:
        self._repo.update(post.Post.from_web_dto(post_dto))
        post_obj = post.from_db_dto(self._repo.find_by_id(post_dto.get("id")))
        return post_obj

    def delete(self, id: str) -> None:
        self._repo.delete_by_id(id)

    def find_by_id(self, id: str) -> post.Post:
        return post.from_db_dto(self._repo.find_by_id(id))

    def find_all_by_page(self, start_from: str, page_size: int) -> list[post.Post]:
        db_dtos = self._repo.find_all_by_page(start_from, page_size)
        post_dtos = list()
        for dto in db_dtos:
            post_dtos.append(post.from_db_dto(dto))
        return post_dtos
