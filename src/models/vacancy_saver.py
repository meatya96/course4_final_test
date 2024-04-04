from abc import ABC, abstractmethod
import json


class VacancySaver(ABC):
    """
    Абстрактный класс для сохранения вакансий. Определяет основные методы для работы с вакансиями.
    """

    @abstractmethod
    def add_vacancy(self, vacancy):
        """
        Добавляет вакансию.

        Args:
            vacancy: Объект вакансии для добавления.
        """
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy):
        """
        Удаляет вакансию.

        Args:
            vacancy: Объект вакансии для удаления.
        """
        pass

    @abstractmethod
    def get_vacancies_by_criteria(self, criteria):
        """
        Возвращает вакансии, соответствующие заданным критериям.

        Args:
            criteria: Критерии для поиска вакансий.

        Returns:
            Список вакансий, соответствующих критериям.
        """
        pass


class JSONSaver(VacancySaver):
    """
    Класс для сохранения вакансий в формате JSON. Реализует интерфейс VacancySaver.
    """

    def __init__(self, file_path="vacancies.json"):
        """
        Инициализирует новый экземпляр класса JSONSaver.

        Args:
            file_path (str): Путь к файлу, в который будут сохраняться вакансии. По умолчанию 'vacancies.json'.
        """
        self.file_path = file_path

    def add_vacancy(self, vacancies):
        """
        Добавляет вакансию в файл JSON.

        Args:
            vacancy: Объект вакансии для добавления.
        """
        with open(self.file_path, 'a') as file:
            for vacancy in vacancies:
                json.dump(vacancy.to_json(), file)
                file.write('\n')

    def delete_vacancy(self, vacancy):
        pass

    def get_vacancies_by_criteria(self, criteria):
        pass