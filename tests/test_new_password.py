import string
from password.new_password import generate_password
def test_password_characters():
    """Тест, что при генерации используются только допустимые символы"""
    valid_characters = string.ascii_letters + string.digits + string.punctuation
    password = generate_password(100)  # Генерируем длинный пароль для более надежной проверки
    for char in password:
        assert char in valid_characters


def test_possword_lenght():
    """Тест длины"""
    test_lengths = [8, 12, 16, 20, 32, 50]
    for length in test_lengths:
        password = generate_password(length)
        assert len(password) == length

def test_passwords_different():
    """Тест, что два сгенерированных подряд пароля различаются"""
    p1 = generate_password(10)
    p2 = generate_password(10)
    assert p1 != p2