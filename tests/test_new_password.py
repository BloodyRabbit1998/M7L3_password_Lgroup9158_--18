import string
from password.new_password import generate_password

def test_password_characters():
    """Тест, что при генерации используются только допустимые символы"""
    valid_characters = string.ascii_letters + string.digits + string.punctuation
    password = generate_password(100)  # Генерируем длинный пароль для более надежной проверки
    for char in password:
        assert char in valid_characters


def test_password_length_matches_requested():
    for length in [8, 16, 32, 64, 128]:
        password = generate_password(length)
        assert len(password) == length, f"Expected length {length}, got {len(password)}"