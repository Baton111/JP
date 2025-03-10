import requests
import json


def get_salary(skills, page):
    url = "https://api.hh.ru/vacancies"
    params = {
        "text": skills,
        "per_page": 100,
        "page": page
    }
    response=requests.get(url,params=params).json()
    salary_list = []
    count_vacancies = len(response['items'])
    for vacancy in response['items']:
        if vacancy['salary'] and vacancy['salary']["from"] and vacancy['salary']['to'] and vacancy['salary']["currency"]=='RUR':
            mid_salary=(vacancy['salary']['from'] + vacancy['salary']['to'] ) /2
            salary_list.append(mid_salary)
    return count_vacancies, salary_list

def get_statistic():
    all_salary = []
    count = 0
    skills = input("write which job are you finding")
    for page in range(10):
        count_vacancies, salary_list = get_salary(skills, page)
        count += count_vacancies
        all_salary.extend(salary_list)
    statistic = [count, len(all_salary),int(min(all_salary)), int(max(all_salary)), int(sum(all_salary)/len(all_salary))]
    return statistic

print(get_statistic())
