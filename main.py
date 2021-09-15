# --*-- coding: utf-8 --*--
"""Задание №3 вопросы со Stackoverflow"""
from datetime import date, timedelta

import requests


def get_stackoverflow_questions_count(period: int, tag: str) -> int:
    """Получение количества вопросов

    Args:
        period(int): Период запроса в днях
        tag(str): Тег вопроса

    Returns:
        questions_count(int): Количество вопросов
    """
    url = "https://api.stackexchange.com/2.3/questions"
    params = {
        "fromdate": date.today() - timedelta(days=period),
        "tagged": tag,
        "site": "stackoverflow",
        "filter": "total",
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    questions_count = int(response.json()["total"])
    return questions_count


def get_stackoverflow_questions(
    period: int, tag: str, pagesize: int, page: int
) -> list:
    """Получение информации о вопросах

    Args:
        period(int): Период запроса в днях
        tag(str): Тег вопроса
        pagesize(int): Размер страницы с результатами
        page(int): Номер страницы

    Returns:
        questions_list(list): Список вопросов
    """
    url = "https://api.stackexchange.com/2.3/questions"
    params = {
        "fromdate": date.today() - timedelta(days=period),
        "tagged": tag,
        "site": "stackoverflow",
        "pagesize": pagesize,
        "page": page,
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    questions_list = response.json()["items"]
    return questions_list


if __name__ == "__main__":
    period = 2
    tag = "Python"
    questions_count = get_stackoverflow_questions_count(period, tag)
    print(
        f"Over the past {period} days, {questions_count} "
        f"questions have been posted on Stackoverflow with the '{tag}' tag!"
    )
    pagesize = 30
    page = 0

    while page <= (questions_count // pagesize):
        choice = input(f"---\nPrint titles of {pagesize} questions? ")
        if choice.lower() == "y":
            page += 1
            for question in get_stackoverflow_questions(period, tag, pagesize, page):
                print(question["title"])
            print(f"---\nPage {page} from {questions_count // pagesize}")
        else:
            print("---\nExecution completed")
            break
