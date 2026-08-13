import string
from password.new_password import generate_password

def test_password_characters():
    """Тест, что при генерации используются только допустимые символы"""
    valid_characters = string.ascii_letters + string.digits + string.punctuation
    password = generate_password(100)  # Генерируем длинный пароль для более надежной проверки
    for char in password:
        assert char in valid_characters

def test_password_length():
    """Тест, что длина пароля соответствует заданной"""
    lengths = [0, 8, 16, 32]
    for length in lengths:
        password = generate_password(length)
        assert len(password) == length

def test_password_uniqueness():
    """Тест, что два последовательно сгенерированных пароля различаются"""
    password_one = generate_password(16)
    password_two = generate_password(16)
    assert password_one != password_two

def test_password_returns_string():
    """Тест, что функция возвращает именно строковый тип данных"""
    password = generate_password(12)
    assert isinstance(password, str)
