from abc import ABC, abstractmethod
from typing import Any


class Parrot(ABC):
    """
    Абстрактный класс, описывающий попугая.
    """

    def __init__(self, species: str, age: int):
        if age < 0:
            raise ValueError("Возраст не может быть отрицательным.")
        self.species = species
        self.age = age

    def talk(self, phrase: str) -> None:
        """
        Попугай произносит переданную фразу.

        :param phrase: Фраза, которую должен произнести попугай.
        :type phrase: str
        :return: None

        Пример использования:
        >>> parrot.talk("Привет!")
        """
        ...

    def fly(self, distance: float) -> float:
        """
        Попугай летит на указанное расстояние.

        :param distance: Расстояние, которое должен преодолеть попугай (в км).
        :type distance: float
        :return: Длина пути, пройденного попугаем.

        Пример использования:
        >>> parrot.fly(10)
        10.0
        """
        ...


class Snow(ABC):
    """
    Абстрактный класс, описывающий снег.
    """

    def __init__(self, temperature: float, purity: float):
        if purity < 0 or purity > 100:
            raise ValueError("Чистота должна быть в пределах от 0 до 100.")
        self.temperature = temperature
        self.purity = purity

    def melt(self) -> bool:
        """
        Определяет, растает ли снег при текущей температуре.

        :return: True, если снег тает, иначе False.

        Пример использования:
        >>> snow.melt()
        True
        """
        ...

    def compact(self) -> None:
        """
        Уплотняет снег.

        :return: None

        Пример использования:
        >>> snow.compact()
        """
        ...


class Twitter(ABC):
    """
    Абстрактный класс, описывающий Twitter-аккаунт.
    """

    def __init__(self, username: str, followers_count: int):
        if followers_count < 0:
            raise ValueError("Количество подписчиков не может быть отрицательным.")
        self.username = username
        self.followers_count = followers_count

    def tweet(self, message: str) -> None:
        """
        Публикует твит с указанным сообщением.

        :param message: Текст сообщения.
        :type message: str
        :return: None

        Пример использования:
        >>> twitter.tweet("Доброе утро!")
        """
        ...


    def follow(self, username: str) -> None:
        """
        Подписывается на указанный аккаунт.

        :param username: Имя пользователя, на которого нужно подписаться.
        :type username: str
        :return: None

        Пример использования:
        >>> twitter.follow("openai")
        """
        ...


if __name__ == "__main__":
    import doctest

    doctest.testmod()
