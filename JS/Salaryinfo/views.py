from django.shortcuts import render
from .forms import PostForm
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

def get_statistic(skills):
    all_salary = []
    count = 0
    for page in range(10):
        count_vacancies, salary_list = get_salary(skills, page)
        count += count_vacancies
        all_salary.extend(salary_list)
    statistic = [count, len(all_salary),int(min(all_salary)), int(max(all_salary)), int(sum(all_salary)/len(all_salary))]
    return statistic

def submitted_form(request):
    if request.method == "POST":
        form=PostForm(request.POST)
        form_get=PostForm()
        if form.is_valid():
            skills=form.cleaned_data['skills']
            statistic=get_statistic(skills)
            context={
                'count':statistic[0],
                'proceeded':statistic[1],P
                'min':statistic[2],
                'max':statistic[3],
                'mid':statistic[4],
                "form":form_get

            }
            return render(request, 'result.html', context)
def index (request):
    form=PostForm()
    return render(request, 'home.html', {'form':form})

# Create your views here.
