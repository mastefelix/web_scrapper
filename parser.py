import requests
from bs4 import BeautifulSoup
import save_to_database
import save_to_csv


def parse_webpage(url, user_agent):
    headers = {'User-Agent': user_agent}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        course_elements = soup.select('.g-mb-20 > .landing-block-node-card-title')
        describe_courses = soup.select('.g-mb-20 > .landing-block-node-card-text')
        info = dict(zip(course_elements, describe_courses))
        data_for_csv = list()
        for course_name, describe_course in info.items():
            name = course_name.text.strip()
            describe = describe_course.text.strip()
            save_to_database.save_to_database(name, describe)
            data_for_csv.append({'course_name': name, 'describe': describe})
        save_to_csv.save_to_csv(data_for_csv)
        return data_for_csv
    else:
        print(f"Ошибка: Не удалось подключиться к веб-странице. Код: {response.status_code}")


def parser():
    URL = 'https://cso.neosystems.ru/'
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    save_to_database.create_database()
    result = parse_webpage(URL, user_agent)
    return result

if __name__ == "__main__":
    print(parser())
