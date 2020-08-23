# Created on Aug 23, 2020

# @author: Bharath HS

import pytest


class TestServicePostJsonPlaceholder:

    def test_post_new_user(self, setup):

        # Call Factory method to get the instance of the class
        self.CommonClass, self.config_data = setup

        self.url_arg = self.CommonClass.get_url(self.config_data, self.config_data["post_new_user_endpoint"])

        file_path = "/Test_Resources/upload_new_data.json"

        # executing the method,to perform post operation
        self.response = self.CommonClass.post_service(self.url_arg, file_path)

        assert self.response.status_code == 201, "Post Operation failed,Status code is - " + str(
            self.response.status_code) + ", 201 is expected"

        print("response", self.response.status_code)
        self.response_data = self.response.json()

        print("Create new user response_data : ", self.response_data)

        self.data_json = self.CommonClass.get_attribute('/Test_Resources/attributes.json')
        self.attributes = self.data_json["attributes"]

        for key in self.response_data:
            print(key)
            if not key in self.attributes:
                assert False, "Doesn't match Parameter / Not found - " + str(key)

        # Response object --> json template
        print("response_data : ", self.response_data)

        self.CommonClass.validate_put_post_service(self.response_data, file_path, "post", setup)

    def test_user_creation_negative(self, setup):

        # Call Factory method to get the instance of the class
        self.CommonClass, self.config_data = setup

        self.url_arg = self.CommonClass.get_url(self.config_data, self.config_data["post_new_user_endpoint"])

        file_path = "/Test_Resources/upload_new_data.json"

        # executing the method,to perform post operation
        self.response = self.CommonClass.post_service(self.url_arg, file_path)

        assert self.response.status_code == 201, "Post Operation failed,Status code is - " + str(
            self.response.status_code) + ", 201 is expected"

        print("response", self.response.status_code)
        self.response_data = self.response.json()

        print("Create new user response_data : ", self.response_data)

        self.data_json = self.CommonClass.get_attribute('/Test_Resources/attributes.json')
        self.attributes = self.data_json["attributes"]

        for key in self.response_data:
            print(key)
            if not key in self.attributes:
                assert False, "Doesn't match Parameter / Not found - " + str(key)

        # Response object --> json template
        print("response_data : ", self.response_data)

        self.CommonClass.validate_put_post_service(self.response_data, file_path, "post", setup)

        validation_url = self.CommonClass.get_url(self.config_data, self.config_data["get_individual_usr_endpoint"] +
                                                  str(self.response_data['id']))

        self.CommonClass.validate_record_created(validation_url)
