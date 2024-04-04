from abc import ABC, abstractmethod
from src.models.vacancy import Vacancy

import requests


class Api(ABC):
    """
    Абстрактный класс для работы с API по поиску вакансий.
    Определяет общий интерфейс для получения данных о вакансиях.
    """

    @abstractmethod
    def get_vacancies(self, search_query):
        """
        Получает данные о вакансиях на основе поискового запроса.

        Args:
            search_query (str): Поисковый запрос для получения вакансий.

        Returns:
            Данные о вакансиях в зависимости от реализации конкретного API.
        """
        pass


class HHapi(Api):
    """
    Класс для работы с API HeadHunter (HH.ru).
    Реализует интерфейс Api для получения данных о вакансиях с сайта HH.ru.
    """

    def __init__(self):
        """
        Инициализирует новый экземпляр класса HHapi с базовым URL API HH.ru.
        """
        self.base_url = "https://api.hh.ru/vacancies"

    def get_vacancies(self, search_query):
        """
        Получает данные о вакансиях с сайта HH.ru на основе поискового запроса.

        Args:
            search_query (str): Поисковый запрос для получения вакансий.

        Returns:
            dict: Ответ от API HH.ru в формате JSON с данными о вакансиях.
        """
        settings = {"text": search_query, "area": 1}  # 1 - код региона (Москва)
        response = requests.get(self.base_url, params=settings).json()['items']
        vacancy_list = []
        for vacancy_info in response:
            name = vacancy_info.get('name', 'Не указано')
            alternate_url = vacancy_info.get('alternate_url', 'Не указано')
            salary_info = vacancy_info.get('salary')
            description = vacancy_info.get('description', 'Описание отсутствует')
            vacancy_list.append(Vacancy(name, alternate_url, salary_info, description))
        return vacancy_list
