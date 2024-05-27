from src.config_settings import read_config
from src.api_hh import ApiHH
from src.DBManager import DatabaseManager


def main():

    job_api_response = ApiHH()

    employers_data = job_api_response.get_employers()

    jobs_data = job_api_response.get_jobs()

    db_manager = DatabaseManager(read_config(), 'CompanyJobs')

    db_manager.create_database()

    db_manager.create_db_tables()

    db_manager.save_data_to_db(employers_data, jobs_data)

    all_employers_jobs = db_manager.get_employers_and_jobs_count()

    print("Getting a list of all employers and the number of jobs at each company: ")
    for value in all_employers_jobs:
        print(f"{value}")

    all_jobs = db_manager.get_all_jobs()

    print("\nGetting a list of all jobs: ")
    for value in all_jobs:
        print(f"{value}\n")

    avg_salary = db_manager.get_avg_salary()

    print("\nGetting the average salary for jobs: ")
    for value in avg_salary:
        print(f"{value}\n")

    higher_salary_jobs = db_manager.get_jobs_with_higher_salary()

    print("\nGetting a list of all jobs with a salary higher than the average salary: ")
    for value in higher_salary_jobs:
        print(f"{value}")

    keyword_jobs = db_manager.get_jobs_with_keyword('driver')
    print("\nGetting a list of all jobs by keyword: ")
    for value in keyword_jobs:
        print(f"{value}")
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
