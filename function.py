import requests


def exercise_1_1(mentors):
    all_names = []
    for x in mentors:
        all_names.extend(x)
    all_names_list = []
    for names in all_names:
        name = names.split(' ')[0]
        all_names_list.append(name)
    unique_names = sorted(set(all_names_list))
    return f"Уникальные имена преподавателей: {', '.join(unique_names)}"


def exercise_1_2(courses, mentors):
    mentors_names = []
    for m in mentors:
        course_names = []
        for name in m:
            course_names.append(name.split(' ')[0])
        mentors_names.append(course_names)
    pairs = []
    for id1 in range(len(mentors_names)):
        for id2 in range(len(mentors_names)):
            if mentors_names[id1] != mentors_names[id2]:
                intersection_set = set(mentors_names[id1]) & set(mentors_names[id2])
                if len(intersection_set) > 0:
                    pair = {courses[id1], courses[id2]}
                    if pair not in pairs:
                        pairs.append(pair)
                        all_names_sorted = sorted(intersection_set)
                        return f"На курсах '{courses[id1]}' и '{courses[id2]}' преподают: {', '.join(all_names_sorted)}"


def exercise_1_3(courses, mentors, durations):
    courses_list = []
    for course, mentor, duration in zip(courses, mentors, durations):
        course_dict = {"title": course, "mentors": mentor, "duration": duration}
        courses_list.append(course_dict)
    durations_dict = {}
    for id, course in enumerate(courses_list):
        key = course['duration']
        durations_dict.setdefault(key, [])
        durations_dict[key].append(id)
    durations_dict = dict(sorted(durations_dict.items()))
    for duration, ids in durations_dict.items():
        for id in ids:
            course = courses_list[id]
            return (f'{courses_list[id]["title"]} - {duration} месяцев')


def get_token():
    return open('token.txt').read()


class APIYandex:
    def __init__(self, token):
        self.name = None
        self.token = token
        self.headers = {'Content_Type': 'application/json', "Authorization": f"OAuth {self.token}"}

    def result(self):
        response = requests.get('https://cloud-api.yandex.net/v1/disk', headers=self.headers)
        return response.status_code

    def create_folder(self, name):
        self.name = name
        response = requests.put(f'https://cloud-api.yandex.net/v1/disk/resources?path={self.name}',
                                headers=self.headers)
        return response.status_code

    def delete_folder(self, name):
        self.name = name
        response = requests.delete(f'https://cloud-api.yandex.net/v1/disk/resources?path=%2F{self.name}&force_async'
                                   f'=true', headers=self.headers)
        return response.status_code

    def find_info(self):
        response = requests.get('https://cloud-api.yandex.net/v1/disk/resources?path=%2F', headers=self.headers)
        return response.text

