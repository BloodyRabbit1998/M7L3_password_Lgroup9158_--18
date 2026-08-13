import string
from password.new_password import generate_password


def test_password_characters():
    """Тест, что при генерации используются только допустимые символы"""
    valid_characters = string.ascii_letters + string.digits + string.punctuation
    password = generate_password(100)  # Генерируем длинный пароль для более надежной проверки
    for char in password:
        assert char in valid_characters


def test_password_length():
    """Тест, что длина пароля соответствует заданной."""
    assert len(generate_password(20)) == 20


def test_default_password_length():
    """Тест, что длина пароля по умолчанию равна 12."""
    assert len(generate_password()) == 12


def test_zero_length_password():
    """Тест, что при нулевой длине возвращается пустая строка."""
    assert generate_password(0) == ''


"""
Допиши еще один тест из предложенных. Или придумай свой.
Если сможешь написать больше, то будет круто!

Тест, что длина пароля соответствует заданной
Тест, что два сгенерированных подряд пароля различаются
"""
