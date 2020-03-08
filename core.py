import requests
from collections import defaultdict
from geopy.distance import geodesic


def get_response_from_url_in_json(url):
    return requests.get(url).json()


def find_all_posts_created_by_user(posts):
    all_posts_of_user = defaultdict(list)
    for post in posts:
        all_posts_of_user[post["userId"]] += [
            {"post_id": post["id"], "title": post["title"], "body": post["body"]}
        ]
    return all_posts_of_user


def return_number_of_posts_by_username(users, users_posts):
    list_of_str = []
    for user in users:
        if user["id"] in users_posts:
            list_of_str += [
                str(user["username"]) + " count " + str(len(users_posts[user["id"]]))
            ]

    return list_of_str


def find_not_unique_titles(posts):
    seen = set()
    not_unique = []
    for post in posts:
        post_title = post["title"].lower()
        if post_title not in seen:
            seen.add(post_title)
        else:
            not_unique.append(post_title)
    return not_unique


def calculate_distance_between_two_gps_points_in_meters(first_loc, second_loc):
    """
    first_loc/second_loc must be sequence of two numbers where
    1st one is Latitude 2nd Longtitude
    """
    return geodesic(first_loc, second_loc).meters


def find_nearest_living_user(users):
    calc_dist = calculate_distance_between_two_gps_points_in_meters
    user_location_list = []
    neighbours_list = []

    # This loop is redundant but kept for readability.
    for user in users:
        user_location_list.append(
            (user["id"], user["address"]["geo"]["lat"], user["address"]["geo"]["lng"])
        )

    for index, user in enumerate(user_location_list):
        min_distance_between_users = float("inf")
        first_loc = user[1], user[2]
        first_id = user[0]
        for user2 in user_location_list[index + 1 :]:
            second_loc = user2[1], user2[2]
            second_id = user2[0]
            curr_dist_between_users = calc_dist(first_loc, second_loc)
            if curr_dist_between_users < min_distance_between_users:
                min_distance_between_users = curr_dist_between_users
                close_living_users = first_id, second_id
        neighbours_list += [close_living_users]
    return neighbours_list


def main():
    users = get_response_from_url_in_json("https://jsonplaceholder.typicode.com/users")
    posts = get_response_from_url_in_json("https://jsonplaceholder.typicode.com/posts")
    user_posts = find_all_posts_created_by_user(posts)
    print(return_number_of_posts_by_username(users, user_posts))
    print("not unique posts: ", find_not_unique_titles(posts))
    print("closest neighbours id pairs: ", find_nearest_living_user(users))


if __name__ == "__main__":
    main()
