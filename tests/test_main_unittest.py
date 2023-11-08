from unittest import TestCase
from function import APIYandex



class TestAPIYandex(TestCase):
    def setUp(self):
        self.token = ''  # нужно указать токен от полигона
        self.folder = '' # указать папку для создания, поиска, удаления

    def test_1status_code(self):
        expected = 200
        result = APIYandex(self.token).result()
        self.assertEqual(expected, result)

    def test_2create_folder(self):
        expected = 201
        result = APIYandex(self.token).create_folder(self.folder)
        self.assertEqual(expected, result)

    def test_3folder(self):
        expected = self.folder
        result = APIYandex(self.token).find_info()
        self.assertIn(expected, result)

    def test_4delete_folder(self):
        expected = 202
        result = APIYandex(self.token).delete_folder(self.folder)
        self.assertEqual(expected, result)
