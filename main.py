from function import exercise_1_2, exercise_1_3, exercise_1_1, APIYandex, get_token
from data import course, duration, mentor
token = '' #укажите токен


if __name__ == '__main__':
    print(exercise_1_1(mentor))
    print(exercise_1_2(course, mentor))
    print(exercise_1_3(course, mentor, duration))
    API_test = APIYandex(token)
    name_folder = str(input("Введите название папки: "))
    print(API_test.result())
    print(API_test.create_folder(name_folder))
    print(API_test.find_info())
    print(API_test.delete_folder(name_folder))