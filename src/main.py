from src.api.hh_api import HHapi
from src.models.vacancy_saver import JSONSaver
from src.utils.helpers import print_vacancies
from src.utils.helpers import filter_vacancies, sort_vacancies, get_top_vacancies

def user_interaction():
    """
    Функция интерактивного взаимодействия с пользователем для поиска, фильтрации и вывода вакансий с сайта HH.ru.

    Пользователю предлагается ввести поисковый запрос, количество вакансий для вывода и ключевые слова для фильтрации.
    На основе этих данных функция использует API HH.ru для поиска вакансий, фильтрует полученные вакансии по ключевым словам,
    сортирует их по умолчанию и выводит топ N вакансий в консоль.
    """
    # Получение входных данных от пользователя
    search_query = input("Введите поисковый запрос: ")
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()

    # Создание экземпляра API и получение вакансий по поисковому запросу
    hh_api = HHapi()
    hh_vacancies = hh_api.get_vacancies(search_query)
    saver = JSONSaver()
    saver.add_vacancy(hh_vacancies)
    print("Ответ API:", hh_vacancies)

    if hh_vacancies:
        vacancies_list = []
        '''
        for vacancy_info in hh_vacancies['items']:
            # Обработка полученной информации и формирование списка вакансий
            if isinstance(vacancy_info, dict):
                name = vacancy_info.get('name', 'Не указано')
                alternate_url = vacancy_info.get('alternate_url', 'Не указано')
                salary_info = vacancy_info.get('salary')
                salary_from = salary_info.get('from', 'Зарплата не указана') if salary_info else 'Зарплата не указана'
                description = vacancy_info.get('description', 'Описание отсутствует')
                vacancies_list.append({'name': name, 'alternate_url': alternate_url, 'salary_from': salary_from, 'description': description})
            elif isinstance(vacancy_info, Vacancy):
                # Включение в список вакансий экземпляров класса Vacancy
                vacancies_list.append(vacancy_info)
        '''
        for vac in hh_vacancies:
            print(vac.__dict__)
            vacancies_list.append(vac.__dict__)
        # Фильтрация, сортировка и выбор топ N вакансий
        print(vacancies_list)
        filtered_vacancies = filter_vacancies(vacancies_list, filter_words)
        sorted_vacancies = sort_vacancies(filtered_vacancies)
        top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
        print_vacancies(top_vacancies)
    else:
        print("Не удалось получить вакансии. Пожалуйста, проверьте запрос и попробуйте снова.")

if __name__ == "__main__":
    user_interaction()
    print("Программа завершила выполнение.")
