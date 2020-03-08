from core import (
    get_response_from_url_in_json,
    find_all_posts_created_by_user,
    find_not_unique_titles,
    find_nearest_living_user,
    return_number_of_posts_by_username,
)
from core_tests.test_variables import *


def test_number_of_users_returned_by_find_all_posts_created_by_user():
    users_posts = find_all_posts_created_by_user(posts)
    assert 4 == len(users_posts)


def test_number_of_posts_of_user_returned_by_find_all_posts_created_by_user():
    users_posts = find_all_posts_created_by_user(posts)
    assert 2 == len(users_posts[2])


def test_find_not_unique_titles():
    not_unique = find_not_unique_titles(posts)
    assert not_unique[0] == "magnam facilis autem"


def test_find_nearest_living_user():
    closeset_neighbours = find_nearest_living_user(users)
    assert closeset_neighbours == [(12, 6), (6, 9), (6, 9)]


def test_get_response_from_url_in_json(mock_response):
    expected_result = [
        {
            "id": 1,
            "name": "Leanne Graham",
            "username": "Bret",
            "email": "Sincere@april.biz",
            "address": {
                "street": "Kulas Light",
                "suite": "Apt. 556",
                "city": "Gwenborough",
                "zipcode": "92998-3874",
                "geo": {"lat": "-37.3159", "lng": "81.1496"},
            },
            "phone": "1-770-736-8031 x56442",
            "website": "hildegard.org",
            "company": {
                "name": "Romaguera-Crona",
                "catchPhrase": "Multi-layered client-server neural-net",
                "bs": "harness real-time e-markets",
            },
        }
    ]

    result = get_response_from_url_in_json("https://jsonplaceholder.typicode.com/users")
    assert result == expected_result
