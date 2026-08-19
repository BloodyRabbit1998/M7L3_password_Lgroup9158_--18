import string
from password.new_password import generate_password

def test_password_characters():
    """Тест, что при генерации используются только допустимые символы"""
    valid_characters = string.ascii_letters + string.digits + string.punctuation
    password = generate_password(100)  # Генерируем длинный пароль для более надежной проверки
    for char in password:
        assert char in valid_characters


###Допиши еще тесты из предложенных.
def test_lenght_generate_password():
    ###Тест, что длина пароля соответствует заданной
    password = generate_password(101)
    count_for_password = 0
    for char in password:
        count_for_password += 1
    assert count_for_password == 101

def test_same_generate_password():
    ###Тест, что два сгенерированных подряд пароля различаются
    password = generate_password(777)
    password7 = generate_password(777)
    if password != password7:
        stroki = 'raznie'
    else:
        stroki = 'odinakovie'
    assert stroki == 'raznie'

