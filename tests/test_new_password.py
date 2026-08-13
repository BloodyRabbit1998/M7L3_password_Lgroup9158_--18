import string
from password.new_password import generate_password

def test_password_characters():
    """Тест, что при генерации используются только допустимые символы"""
    valid_characters = string.ascii_letters + string.digits + string.punctuation
    password = generate_password(100)  # Генерируем длинный пароль для более надежной проверки
    for char in password:
        assert char in valid_characters

def test_password_length():
    password = generate_password(100)
    assert len(password) == 100

def test_passwords_are_different():
    password1 = generate_password(100)
    password2 = generate_password(100)
    assert password1 != password2

def test_short_password():
    password = generate_password(10)
    assert len(password) == 10

def test_one_character_password():
    password = generate_password(1)
    assert len(password) == 1