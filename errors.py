"""
Этот модуль содержит функции-обработчики ошибок, которые используются в
приложении для перенаправления пользователя на страницу с соответствующей
ошибкой.
"""

from flask import redirect, render_template, flash, url_for, Response

from app import app


@app.errorhandler(401)
def error401(status) -> Response:
    """
    Функция обрабатывает ошибку HTTP 401, перенаправляя пользователя на
    страницу авторизации.
    :param status: Int(Код ошибки)
    :return: None
    """
    flash(
        {'title': 'Внимание!', 'message': 'Необходимо авторизоваться.'},
        category='info',
    )
    return redirect(url_for('input_user')), 301


@app.errorhandler(404)
def error404(status) -> str:
    """
    Функция обрабатывает ошибку HTTP 404.
    :param status: int(Код ошибки)
    :return: error404.html (Шаблон страницы ошибки)
    """
    return render_template('errors/error404.html')


@app.errorhandler(429)
def error429(status) -> str:
    """
    Функция отрабатывает ошибку HTTP 429.
    :param status: int(Код ошибки)
    :return: error429.html (Шаблон страницы ошибки)
    """
    return render_template('errors/error429.html')
