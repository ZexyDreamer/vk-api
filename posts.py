import requests
import csv

token = '80b98a3e80b98a3e80b98a3e7180cbf101880b980b98a3ede65550f3daad0b099317ff1'
version = 5.107
user_id = int(input('Enter user id: '))


def get_posts(u_id):
    response = requests.get('https://api.vk.com/method/wall.get',
                            params={'access_token': token,
                                    'v': version,
                                    'owner_id': u_id,
                                    'count': 10,
                                    'filter': 'owner'})
    data = response.json()
    return data


def write_posts(data):
    posts_list = [f"{post['likes']['count']} {post['reposts']['count']} " \
                  f"{post['views']['count']}" for
                  post in
                  data['response']['items']]
    with open(f'posts_of_{user_id}.csv', 'w') as file:
        a_pen = csv.writer(file)
        a_pen.writerow(('Likes', 'Reposts', 'Views'))
        for post in posts_list:
            p = post.split()
            a_pen.writerow((p[0], p[1], p[2]))


data = get_posts(user_id)
write_posts(data)
