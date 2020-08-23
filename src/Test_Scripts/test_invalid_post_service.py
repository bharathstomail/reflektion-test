# Created on Aug 23, 2020

# @author: Bharath HS

import pytest


class TestServiceInvalidPostJsonPlaceholder:

    @pytest.mark.run(order=2)
    def test_valid_invalid_posts(self, setup):
        # Call Factory method to get the instance of the class
        self.CommonClass, self.config_data = setup

        self.url_arg = self.CommonClass.get_url(self.config_data, self.config_data["get_invalid_posts_endpoint"])
        print("URL :", self.url_arg)

        # executing the method,to perform get operation
        self.response = self.CommonClass.get_service(self.url_arg)

        print("Response_status code :", self.response.status_code)
        print("Response_content :", self.response.content)

        assert self.response.status_code == 404, "Invalid post,Status code is - " + str(self.response.status_code) \
                                                 + ", 404 is expected"
