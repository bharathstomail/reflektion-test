
# Created on Aug 23, 2020

# @author: Bharath HS

import json
import requests
from pathlib import Path


class CommonClass:

    def __init__(self):
        self.header = {'Content-Type': 'application/json', "charset": "UTF-8"}
        self.config_dir = str(Path(__file__).parent.parent)

    def get_config(self, file_path):
        # config_dir = str(Path(__file__).parent.parent)
        path_arg = self.config_dir + file_path
        with open(path_arg) as o1:
            data_json = json.loads(o1.read())
        return data_json

    def get_attribute(self, file_path):
        # config_dir = str(Path(__file__).parent.parent)
        path_arg = self.config_dir + file_path
        with open(path_arg) as o1:
            data_json = json.loads(o1.read())
        return data_json

    def get_url(self, endpoint_object, endpoint_arg):
        return endpoint_object["base_url"]+endpoint_arg

    def get_service(self, url_arg):
        print("header details : ", self.header)
        response = requests.get(url_arg, headers=self.header, verify=False)
        return response

    def post_service(self, url_arg, file_arg):

        with open(self.config_dir + file_arg, 'rb') as o1:
            payload_1 = json.load(o1)

        response = requests.post(url_arg, json=payload_1, headers=self.header, verify=False)

        return response

    def put_service(self, url_arg, file_arg):

        with open(self.config_dir + file_arg, 'rb') as o1:
            payload = json.load(o1)

        header = {"key": "Content-Type", "value": "application/json", "charset": "UTF-8"}
        
        response = requests.put(url_arg, data=payload, headers=header, verify=False)

        return response

    def delete_service(self, url_arg):

        payload = {}

        response = requests.request("DELETE", url_arg, headers=self.header, data=payload)

        return response

    def update_config_file(self, key_arg, val_arg):
        path_arg = self.config_dir + '/Test_Resources/Config_File.json'

        with open(path_arg, 'r+') as f:
            data = json.load(f)
            data[key_arg] = val_arg
            f.seek(0)
            json.dump(data, f, indent=4)
            f.truncate()

    # To validate the user created/updated against the attribute
    def validate_put_post_service(self, response_arg, file_path, event_arg, setup):
        # Call Factory method to get the instance of the class
        self.CommonClass, self.config_data = setup

        config_dir = str(Path(__file__).parent.parent)

        with open(config_dir+file_path) as o1:
            self.body_msg_json = json.loads(o1.read())

        assert len(response_arg) == 4, "Doesn't match with the no. of Response data - " + str(
            len(response_arg))

        self.url_arg = self.CommonClass.get_url(self.config_data, self.config_data["get_all_user_endpoint"])

        # executing the method,to perform get operation
        self.get_response = self.CommonClass.get_service(self.url_arg)
        self.get_response_data = self.get_response.json()

        # validate the id value for post
        if str(event_arg).upper() == "POST":
            assert response_arg['id'] > self.get_response_data[len(self.get_response_data)-1]['id'], \
                "id created must be greater than existing value"

        # validating the parameter values with body message posted
        for data in response_arg.keys():
            if not str(event_arg).upper() == "POST":
                assert str(response_arg[data]) == str(self.body_msg_json[data]), \
                    "Doesn't match with the Parameter value - " + str(self.body_msg_json[data])

    # To validate the user created/updated against the end point "https://jsonplaceholder.typicode.com/posts"
    def validate_record_created(self, url_arg):

        # executing the method,to perform get operation
        self.response = self.get_service(url_arg)

        assert self.response.status_code == 200, "Failed to retrieve the user information, Status code is - " + str(
            self.response.status_code) + ", 200 is expected"

        return self.response
