# Created on Aug 23, 2020

# @author: Bharath HS

import pytest


class TestServicePutJsonPlaceholder:

    @pytest.mark.parametrize('x', [(1)])
    def test_update_user(self, x, setup):

        # Call Factory method to get the instance of the class
        self.CommonClass, self.config_data = setup

        self.url_arg = self.CommonClass.get_url(self.config_data, self.config_data["update_user_details_endpoint"]
                                                + str(x))

        print("update user url :", self.url_arg)
        file_path = "/Test_Resources/update_existing_user.json"

        # executing the method,to perform put operation
        self.response = self.CommonClass.put_service(self.url_arg, file_path)

        assert self.response.status_code == 200, "Put Operation failed,Status code is - " + str(
            self.response.status_code) + ", 200 is expected"

        print("response", self.response.status_code)
        self.response_data = self.response.json()

        print("update user response_data : ", self.response_data)
        self.data_json = self.CommonClass.get_attribute('/Test_Resources/attributes.json')

        self.attributes = self.data_json["attributes"]

        for key in self.response_data:
            print(key)
            if not key in self.attributes:
                assert False, "Doesn't match Parameter / Not found - " + str(key)

        # Response object --> json template
        self.CommonClass.validate_put_post_service(self.response_data, file_path, "put", setup)
