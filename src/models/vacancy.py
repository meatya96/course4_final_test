import json


class Vacancy:
    """
    Класс Vacancy представляет собой модель данных вакансии.

    Attributes:
        title (str): Название вакансии.
        link (str): Ссылка на вакансию.
        salary (str, int, float): Зарплата по вакансии.
        description (str): Описание вакансии.
    """

    def __init__(self, title, link, salary, description):
        """
        Инициализирует новый экземпляр класса Vacancy с заданными атрибутами.

        Args:
            title (str): Название вакансии.
            link (str): Ссылка на вакансию.
            salary (str, int, float): Зарплата по вакансии.
            description (str): Описание вакансии.
        """
        self.title = title
        self.link = link
        self.salary = salary
        self.description = description

        # Валидация значения зарплаты
        if not isinstance(self.salary, (str, int, float)):
            self.salary = 'Не указана'

    def __str__(self):
        """
        Возвращает строковое представление объекта Vacancy.

        Returns:
            str: Строковое представление вакансии.
        """
        return f"{self.title}\nЗарплата: {self.salary}\nСсылка: {self.link}\nОписание: {self.description}\n"

    def __lt__(self, other):
        """
        Определяет поведение оператора < (меньше) для сравнения двух объектов Vacancy по зарплате.

        Args:
            other (Vacancy): Другой объект Vacancy для сравнения.

        Returns:
            bool: True, если зарплата текущего объекта меньше, чем у сравниваемого. Иначе False.
        """
        return self.salary < other.salary

    def to_json(self):
        """
        Конвертирует объект Vacancy в строку формата JSON.

        Returns:
            str: Строка в формате JSON, представляющая объект Vacancy.
        """
        return json.dumps(self.__dict__)

    @staticmethod
    def from_json(json_str):
        """
        Создает объект Vacancy из строки в формате JSON.

        Args:
            json_str (str): Строка в формате JSON, из которой необходимо создать объект Vacancy.

        Returns:
            Vacancy: Объект Vacancy, созданный из строки JSON.
        """
        data = json.loads(json_str)
        return Vacancy(data['title'], data['link'], data['salary'], data['description'])
