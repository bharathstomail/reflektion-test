# Created on Aug 23, 2020

# @author: Bharath HS

import pytest


class TestServiceDeleteJsonPlaceholder:

    @pytest.mark.parametrize('x', [(1)])
    def test_delete_user(self, x, setup):
        # Call Factory method to get the instance of the class
        self.CommonClass, self.config_data = setup

        self.url_arg = self.CommonClass.get_url(self.config_data,
                                                self.config_data["delete_user_endpoint"] + str(x))

        print("delete user url :", self.url_arg)

        # executing the method,to perform delete operation
        self.response = self.CommonClass.delete_service(self.url_arg)

        assert self.response.status_code == 200, "Delete Operation failed,Status code is - " + str(
            self.response.status_code) + ", 200 OK is expected"

        print("response", self.response.status_code)

        assert len(self.response.json()) == 0, "Response object should be an empty dictionary type "
