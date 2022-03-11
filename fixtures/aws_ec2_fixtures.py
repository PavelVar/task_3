"""Module contains fixtures preparing data sets for tests of AWS EC2 instances, security group and network interfaces"""
import yaml
import pytest

from aws_ec2_fixtures_test_data import get_test_data
from .models.aws_ec2_instance import AWSInstance, AWSSecurityCroup, AWSNetworkInterface


@pytest.fixture
def ec2_instance_id(get_test_data: dict) -> str:
    """Returns ec2_instance_id from data extracted from .yaml file."""
    return get_test_data['instance_id']


@pytest.fixture
def network_id(get_test_data: dict) -> str:
    """Returns network interface id from data extracted from .yaml file."""
    return get_test_data['network_id']


@pytest.fixture
def ec2_instance(ec2_instance_id: str) -> AWSInstance:
    """Creates AWSInstance and returns it to use in other fixtures for call AWSHelper methods."""
    return AWSInstance(ec2_instance_id)

@pytest.fixture
def ec2_instance_actual_attributes(ec2_instance: AWSInstance) -> dict:
    """Using AWSInstance gets it attributes and return them as a dict: image id, state status, public ip number, tags
    and security group id"""
    return {'image_id': ec2_instance.image_id, 'state': ec2_instance.state['Name'], 'tags': ec2_instance.tag[0],
            'public_ip': ec2_instance.public_ip_address, 'security_groupg_id': ec2_instance.security_groups[0]['GroupId']}


@pytest.fixture
def security_group_instance(ec2_instance_actual_attributes) -> AWSSecurityCroup:
    """Gets AWS Security Group instance and returns it for further use."""
    return AWSSecurityCroup(ec2_instance_actual_attributes['security_groupg_id'])


@pytest.fixture
def security_group_actual_ports(security_group_instance: AWSSecurityCroup) -> dict:
    """Gets security group ports and returns them. Returns dict with security group ports numbers: FromPorts and ToPorts."""
    return security_group_instance.allowed_ports


@pytest.fixture
def network_interface(network_id: str) -> AWSNetworkInterface:
    """Gets AWS Network Interface instance and returns it for further use."""
    return AWSNetworkInterface(network_id)


@pytest.fixture
def network_actual_attributes(network_interface: AWSNetworkInterface) -> dict:
    """Using AWSNetworkInterface gets it attributes and return them as a dict: public ip and tags."""
    return {'network_ip': network_interface.private_ip_address, 'tags': network_interface.tag_set[0]}


@pytest.fixture
def expected_data_for_ec2(get_test_data: dict) -> dict:
    """Gets from .yaml data file and returns expected data about EC2 AWS instances: image id, allowed ports, tags,
    public ip, network interface ip"""
    expected_ec2_test_data = {key: get_test_data[key] for key in get_test_data if 'expected' in key}
    return expected_ec2_test_data
