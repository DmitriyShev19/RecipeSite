import re
from flask import flash
from app import ALLOWED_EXTENSIONS
from models import Users


def check_new_user(login: str, email: str, password: str) -> bool:
    """
        Проверяет данные нового пользователя перед регистрацией.

        :param login: логин пользователя
        :type login: str
        :param email: электронная почта пользователя
        :type email: str
        :param password: пароль пользователя
        :type password: str
        :return: результат проверки
        :rtype: bool
    """
    pattern_login = r'^[a-zA-Z!?\d]{5,25}$'
    pattern_email = r'^[-\w\.]+@([-\w]+\.)+[-\w]{2,4}$'
    pattern_password = r'^[a-zA-Z!?\d]{5,36}$'
    if Users.query.filter_by(login=login).first():
        flash({"title": "Ошибка!", "message": "Такой пользователь уже существует"}, category="error")
        return False
    elif Users.query.filter_by(email=email).first():
        flash({"title": "Ошибка!",
               "message": "Пользователь с таким E-mail уже есть"},
              category="error")
        return False
    elif re.match(pattern_login, login) is None:
        flash({"title": "Ошибка!",
               "message": "Логин должен состоять из 5-25 латинских букв, цифр и символов!"},
              category="error")
        return False
    elif re.match(pattern_email, email) is None:
        flash({"title": "Ошибка!",
               "message": "Вы ввели неверный формат почты!"},
              category="error")
        return False
    elif re.match(pattern_password, password) is None:
        flash({"title": "Ошибка!",
               "message": "Пароль должен состоять из 5-36 латинских букв, цифр и символов"},
              category="error")
        return False
    else:
        flash({'title': 'Успешно!',
               'message': 'Вы успешно зарегистрированы, зайдите в кабинет'},
              category='success')
        return True


def allowed_file(filename: str) -> bool:
    """
        Проверяет расширение загружаемого файла и сравнивает его со списком допустимых
        расширений, которые хранятся в константе ALLOWED_EXTENSIONS.

        :param filename: имя файла
        :type filename: str
        :return: результат проверки
        :rtype: bool
    """
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
