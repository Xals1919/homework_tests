import pytest

from function import exercise_1_1, exercise_1_2, exercise_1_3
from data import course, duration, mentor

@pytest.mark.parametrize(
    "mentors, expected",
    [
        (mentor,
         "Уникальные имена преподавателей: Адилет, Азамат, Александр, Алексей, Алена, Анатолий, Анна, Антон, Вадим, "
         "Валерий, Владимир, Денис, Дмитрий, Евгений, Елена, Иван, Илья, Кирилл, Константин, Максим, Михаил, Никита, "
         "Николай, Олег, Павел, Ринат, Роман, Сергей, Татьяна, Тимур, Филипп, Эдгар, Юрий")
    ]
)
def test_exercise_1(mentors, expected):
    result = exercise_1_1(mentors)
    assert result == expected


@pytest.mark.parametrize(
    "courses, mentors, expected",
    [
        (course, mentor,
         "На курсах 'Java-разработчик с нуля' и 'Fullstack-разработчик на Python' преподают: Денис, Евгений, Максим")
    ]
)
def test_courses_top(courses, mentors, expected):
    result = exercise_1_2(courses, mentors)
    assert result == expected


@pytest.mark.parametrize(
    "courses, mentors, durations, expected",
    [
        (course, mentor, duration,
         "Python-разработчик с нуля - 12 месяцев")
    ]
)
def test_exercise_3(courses, mentors, durations, expected):
    result = exercise_1_3(courses, mentors, durations)
    assert result == expected


