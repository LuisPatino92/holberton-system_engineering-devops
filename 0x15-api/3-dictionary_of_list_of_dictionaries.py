#!/usr/bin/python3
""" This module makes a request for a Fake API """

import json
import requests


def get_info(url):
    """ This function makes the request and returns the json """
    return json.loads(requests.get(url).text)


def make_user_dict():
    """ This function returns the dictionary with the relevant information """
    user_dict = {}
    base_url = 'https://jsonplaceholder.typicode.com/'
    user_info = get_info("{}users/{}".format(base_url, sys.argv[1]))
    user_dict['name'] = user_info['name']
    raw_json = get_info('{}todos'.format(base_url))
    done_tasks = 0
    total_tasks = 0
    tasks = []
    for element in raw_json:
        if element['userId'] == int(sys.argv[1]):
            total_tasks += 1
            if element['completed'] is True:
                done_tasks += 1
                tasks += [element['title']]
    user_dict['done_tasks'] = done_tasks
    user_dict['total_tasks'] = total_tasks
    user_dict['tasks'] = tasks
    return user_dict


def get_list(user):
    """ Teturn a list with each line to write to .csv """
    base_url = 'https://jsonplaceholder.typicode.com/'
    user_info = get_info("{}users/{}".format(base_url, user))
    raw_json = get_info('{}todos'.format(base_url))

    tmp_list = []
    for element in raw_json:
        tmp_dict = {}
        if element['userId'] == int(user):
            tmp_dict['task'] = element['title']
            tmp_dict['completed'] = element['completed']
            tmp_dict['username'] = user_info['username']

            tmp_list += [tmp_dict]
    return tmp_list


def get_users():
    """ Returns a list of all users in the API """

    raw_users = get_info('https://jsonplaceholder.typicode.com/users')
    list_users = []
    for element in raw_users:
        list_users += [element['id']]

    return list_users


if __name__ == '__main__':
    users_id = get_users()
    my_dict = {}
    for element in users_id:
        my_dict[element] = get_list(element)
    file_name = '{}.json'.format('todo_all_employees')
    with open(file_name, 'w') as json_file:
        json.dump(my_dict, json_file)
