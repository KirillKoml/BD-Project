from src.config_settings import read_config
from src.api_hh import ApiHH
from src.DBManager import DatabaseManager


def main():

    job_api_response = ApiHH()

    employers_data = job_api_response.get_employers()

    jobs_data = job_api_response.get_jobs()

    db_manager = DatabaseManager(read_config(), 'postgres')

    db_manager.create_database()

    db_manager.create_db_tables()

    db_manager.save_data_to_db(employers_data, jobs_data)

    all_employers_jobs = db_manager.get_employers_and_jobs_count()

    print("Получение списка всех работодателей и количества рабочих мест в каждой компании: ")
    for value in all_employers_jobs:
        print(f"{value}")

    all_jobs = db_manager.get_all_jobs()

    print("\nПолучение списка всех вакансий: ")
    for value in all_jobs:
        print(f"{value}\n")

    avg_salary = db_manager.get_avg_salary()

    print("\nПолучение средней зарплаты по должностям: ")
    for value in avg_salary:
        print(f"{value}\n")

    higher_salary_jobs = db_manager.get_jobs_with_higher_salary()

    print("\nПолучение списка всех вакансий с зарплатой выше средней: ")
    for value in higher_salary_jobs:
        print(f"{value}")

    keyword_jobs = db_manager.get_jobs_with_keyword('driver')
    print("\nПолучение списка всех вакансий по ключевому слову: ")
    for value in keyword_jobs:
        print(f"{value}")

if __name__ == "__main__":
    main()