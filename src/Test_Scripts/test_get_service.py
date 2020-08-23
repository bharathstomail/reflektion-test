# Created on Aug 23, 2020

# @author: Bharath HS

import pytest
import json


class TestServiceGetJsonPlaceholder:

    def test_retrieve_all_users(self, setup):
        # Call Factory method to get the instance of the class
        self.CommonClass, self.config_data = setup

        self.url_arg = self.CommonClass.get_url(self.config_data, self.config_data["get_all_user_endpoint"])

        # executing the method,to perform get operation
        self.response = self.CommonClass.get_service(self.url_arg)

        assert self.response.status_code == 200, "Failed to retrieve users info. Status code is - " + str(
            self.response.status_code) + ", 200 is expected"

        print("response", self.response.status_code)
        self.response_data = self.response.json()

        assert len(self.response_data) == 100, "Doesn't match with the no. of Response data - " + str(
            len(self.response_data))

        print(json.dumps(self.response_data, indent=4))

        return self.response_data

    @pytest.mark.run(order=2)
    @pytest.mark.parametrize('x', [(1)])
    def test_get_user_details_by_id(self, x, setup):
        # Call Factory method to get the instance of the class
        self.CommonClass, self.config_data = setup

        self.id_arg = self.CommonClass.get_url(self.config_data, self.config_data["get_individual_usr_endpoint"] + str(x))

        # executing the method,to perform get operation
        self.response = self.CommonClass.get_service(self.id_arg)

        assert self.response.status_code == 200, "Failed to retrieve user info,Status code is - " + str(
            self.response.status_code) + ", 200 is expected"

        print("response", self.response.status_code)
        self.response_data = self.response.json()

        assert len(self.response_data) == 4, "Doesn't match with the no. of Response data - " + str(
            len(self.response_data))

        print(self.response_data)

        for key in self.response_data:
            if key == "id":
                assert str(self.response_data[key]) == str(
                    x), "Value Doesn't match the criteria id - " + str(self.response_data[key])
                break
        return self.response_data
