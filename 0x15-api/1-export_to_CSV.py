#!/usr/bin/python3
""" This module makes a request for a Fake API """

import json
import requests
import sys


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


def get_csv():
    """ Teturn a list with each line to write to .csv """
    base_url = 'https://jsonplaceholder.typicode.com/'
    user_info = get_info("{}users/{}".format(base_url, sys.argv[1]))
    raw_json = get_info('{}todos'.format(base_url))

    csv_list = []
    for element in raw_json:
        if element['userId'] == int(sys.argv[1]):
            csv_list += ['"{}","{}","{}","{}"\n'.format(str(sys.argv[1]),
                                                        user_info['username'],
                                                        element['completed'],
                                                        element['title'])]
    return csv_list


if __name__ == '__main__':
    user_state = get_csv()
    file_name = '{}.csv'.format(sys.argv[1])
    with open(file_name, 'w') as csv_file:
        for element in user_state:
            csv_file.writelines(element)
