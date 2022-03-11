import yaml
import pytest

yaml_file_path = 'F:\\environments\\task3\\tests'
yaml_file_name = 'aws_ec2_data.yaml'

@pytest.fixture
def get_test_data() -> dict:
    """
    Gets data dict from .yaml data file (instance id< network id and expected data) for use by otrhe fixtures and tests.
    """
    with open(f'{yaml_file_path}\\{yaml_file_name}') as data_file:
        all_yaml_data = yaml.load(data_file, Loader=yaml.FullLoader)
    return all_yaml_data