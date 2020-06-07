import requests
import csv


token = '80b98a3e80b98a3e80b98a3e7180cbf101880b980b98a3ede65550f3daad0b099317ff1'
version = 5.107
user_id = int(input('Enter user id: '))


def get_friends(u_id):
    response = requests.get('https://api.vk.com/method/friends.get',
                            params={'access_token': token,
                                    'v': version,
                                    'user_id': u_id,
                                    'fields': 'domain'})
    data = response.json()
    return data


def write_friends(data):
    friend_list = [f"{friend['first_name']} {friend['last_name']}" for friend in data['response']['items']]
    with open(f'friends_of_{user_id}.csv', 'w') as file:
        a_pen = csv.writer(file)
        a_pen.writerow(('First name', 'Last name'))
        for friend in friend_list:
            fr = friend.split()
            if fr[0] != 'DELETED':
                a_pen.writerow((fr[0], fr[1]))


data = get_friends(user_id)
write_friends(data)
