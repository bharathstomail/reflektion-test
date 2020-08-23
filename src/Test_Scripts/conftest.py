
from src.Library_files.common_functions import CommonClass
import pytest


def get_obj(obj=''):
    objects = dict(CommonClass=CommonClass())
    return objects[obj]


@pytest.fixture()
def setup():
    common_class = get_obj('CommonClass')
    config_data = common_class.get_config('/Test_Resources/endpoint.json')
    return common_class, config_data
