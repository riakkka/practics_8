import io
import sys
from main import get_hello_message


def test_get_hello_message():
    expected_output = "Hello, World!"
    assert get_hello_message() == expected_output
    print("Тест прошёл успешно!")


test_get_hello_message()
