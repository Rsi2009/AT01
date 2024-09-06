import pytest
from unittest.mock import patch
from main3 import get_random_cat_image

@patch('requests.get')
def test_successful_request(mock_get):
    # Мокаем успешный запрос
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = [{"url": "https://example.com/cat.jpg"}]

    # Вызываем функцию
    result = get_random_cat_image()

    # Проверяем, что URL верный
    assert result == "https://example.com/cat.jpg"

    @patch('requests.get')
    def test_unsuccessful_request(mock_get):
        # Мокаем неуспешный запрос с кодом 404
        mock_get.return_value.status_code = 404

        # Вызываем функцию
        result = get_random_cat_image()

        # Проверяем, что результат None
        assert result is None