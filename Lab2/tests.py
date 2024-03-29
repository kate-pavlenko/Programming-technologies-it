import unittest
from app import main, home_work


class TestClass(unittest.TestCase):
    def setUp(self):
        # Дана функція налаштовує початкові агрументи визначені лише для класу
        self.date_url = 'http://date.jsontest.com/'
        self.ip_url = 'http://ip.jsontest.com/'
        self.ip_url = 'http://ip.jsontest.com/'
        self.AM = 'FdgrjhskehksdhrkAMhjugre'
        self.PM = 'Banana milana PM finana'
        self.Err = 'Time error'

    def test_date_work_successfully(self):
        # Перевіряєм чи функція відправювала до кінця і повернулі True
        self.assertTrue(main(self.date_url))

    def test_empty_url(self):
        # Перевіряєм чи у функцію не було передано жодної URL
        self.assertFalse(main())

    def test_no_date_in_response(self):
        # Перевіряємо що у відповіді відсутнє поле дата (тобто передана направильна URL)
        with self.assertRaises(Exception):
            main(self.ip_url)


        # Ваш захист
    def test_home_work_AM(self):
        self.assertTrue(home_work(self.AM) == 0)

    def test_home_work_PM(self):
        self.assertTrue(home_work(self.PM) == 0)

    def test_home_work_Err(self):
        self.assertTrue(home_work(self.Err) == 1)