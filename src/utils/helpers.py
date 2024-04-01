def filter_vacancies(vacancies, ключевые_слова):
    """
    Фильтрует список вакансий по ключевым словам в описании.

    Args:
        vacancies (list): Список словарей вакансий.
        ключевые_слова (list): Список ключевых слов для фильтрации.

    Returns:
        list: Список вакансий, содержащих хотя бы одно из ключевых слов в описании.
    """
    return [вакансия for вакансия in vacancies if
            any(ключ.lower() in вакансия['description'].lower() for ключ in ключевые_слова)]


def sort_vacancies(vacancies):
    """
    Сортирует список вакансий по убыванию зарплаты.

    Args:
        vacancies (list): Список словарей вакансий.

    Returns:
        list: Отсортированный список вакансий по убыванию зарплаты.
    """
    return sorted(vacancies, key=lambda вакансия: вакансия.get('salary_from', 0), reverse=True)


def get_top_vacancies(vacancies, верхняя_граница):
    """
    Возвращает верхнюю часть списка вакансий в соответствии с указанным лимитом.

    Args:
        vacancies (list): Список словарей вакансий.
        верхняя_граница (int): Количество вакансий для возврата.

    Returns:
        list: Список верхних вакансий до указанного лимита.
    """
    return vacancies[:верхняя_граница]


def print_vacancies(vacancies):
    """
    Выводит информацию о вакансиях в консоль.

    Args:
        vacancies (list): Список словарей вакансий.
    """
    if vacancies:
        for index, vacancy in enumerate(vacancies, start=1):
            print(f"Вакансия {index}:")
            print(f"Название: {vacancy.get('name', 'Не указано')}")
            print(f"Зарплата от: {vacancy.get('salary_from', 'Не указана')}")
            print(f"Описание: {vacancy.get('description', 'Отсутствует')}")
            print(f"Ссылка: {vacancy.get('alternate_url', 'Не указана')}")
            print()
    else:
        print("Нет подходящих вакансий")
