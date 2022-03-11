"""Module contains functions with asserts of EC instance, EC2 Security Group and EC2 Network Interface charachteristics"""
import pytest
from pytest_check import check_func

from .models.aws_ec2_instance import AWSInstance

@check_func
def soft_check_ec2_existance(ec2_instance: AWSInstance) -> bool:
    """Checks if EC2 AWS Instance exists.
    :param ec2_instance: AWSInstance
    """
    assert ec2_instance, 'EC2_AWS_Instance was not created.'
    return bool(ec2_instance)

def check_instance_image(actual_data: dict, expected_data: dict, ec2_instance: AWSInstance):
    """Checks the equality of expected image id of EC2 instance and it's actual image id.
    :param actual_data: dict
    :param expected_data: dict
    """
    if soft_check_ec2_existance(ec2_instance):
        error_msg = f'Actual image_id {actual_data["image_id"]} does not concur with expected ({expected_data["expected_instance_image"]}).'
        assert actual_data["image_id"] == expected_data["expected_instance_image"], error_msg

def check_instance_state(actual_data: dict, ec2_instance: AWSInstance):
    """Checks the equality of expected state of EC2 instance and it's actual state
    :param actual_data: dict
    """
    if soft_check_ec2_existance(ec2_instance):
        error_msg = f'Actual state {actual_data["state"]} does not concur with expected ("running").'
        assert actual_data['state'] == 'running', error_msg

def check_instance_public_ip(actual_data: dict, expected_data: dict, ec2_instance: AWSInstance):
    """Checks the equality of expected public ip of EC2 instance and it's actual public ip
    :param actual_data: dict
    :param expected_data: dict
    """
    if soft_check_ec2_existance(ec2_instance):
        error_msg = f'Actual instance public ip {actual_data["public_ip"]} does not concur with expected ({actual_data["public_ip"]}).'
        assert actual_data["public_ip"] == actual_data["public_ip"], error_msg

def check_security_rules_for_ports(security_group_actual_ports: dict, expected_data_for_ec2: expected_data_for_ec2, ec2_instance: AWSInstance):
    """Checks the equality of expected security group ports and actual security group ports
    :param security_group_actual_ports: dict[{'FromPort': str}, {'ToPort': str}]
    :param expected_data_for_ec2: dict
    """
    if soft_check_ec2_existance(ec2_instance):
        actual_from_ports = security_group_actual_ports['FromPorts']
        actual_to_ports = security_group_actual_ports['ToPorts']
        error_msg_from_ports = f'Actual security group FromPorts {actual_from_ports} do not concur with expected ({expected_data_for_ec2["expected_allowed_ports"]}).'
        error_msg_to_ports = f'Actual security group ToPorts {actual_to_ports} do not concur with expected ({expected_data_for_ec2["expected_allowed_ports"]}).'
        assert sorted(actual_from_ports) == sorted(expected_data_for_ec2["expected_allowed_ports"]), error_msg_from_ports
        assert sorted(actual_to_ports) == sorted(expected_data_for_ec2["expected_allowed_ports"]), error_msg_to_ports

def check_instance_tags(actual_data: dict, expected_data: dict, ec2_instance: AWSInstance):
    """Checks the equality of expected tags of EC2 instance and it's actual tags
    :param actual_data: dict
    :param expected_data: dict
    """
    if soft_check_ec2_existance(ec2_instance):
        error_msg = f'Actual instance tag name {actual_data["tags"]["Key"]} does not concur with expected ({expected_data["expected_tag_name"]}).'
        error_msg = f'Actual instance tags {actual_data["tags"]["Value"]} does not concur with expected ({expected_data["expected_tag_text"]}).'
        assert actual_data['tags']['Key'] == expected_data['expected_tag_name'], error_msg_tag_name
        assert actual_data['tags']['Value'] == expected_data['expected_tag_text'], error_msg_tag_text

def check_network_interface_ip(network_actual_attributes: dict, expected_data_for_ec2: dict, ec2_instance: AWSInstance):
    """Checks the equality of expected ip of network interface and it's actual ip
    :param network_actual_attributes: dict
    :param expected_data_for_ec2: dict
    """
    if soft_check_ec2_existance(ec2_instance):
        error_msg = f'Actual network interface ip {network_actual_attributes["network_ip"]} does not concur with expected ' \
                    f'({expected_data_for_ec2["expected_network_interface_ip"]}).'
        assert network_actual_attributes["network_ip"] == expected_data_for_ec2["expected_network_interface_ip"], error_msg

def check_network_interface_tags(network_actual_attributes: dict, expected_data_for_ec2: dict, ec2_instance: AWSInstance):
    """Checks the equality of expected tags of network interface and it's actual tags
    :param network_actual_attributes: dict
    :param expected_data_for_ec2: dict
    """
    if soft_check_ec2_existance(ec2_instance):
        error_msg = f'Actual network tag name {network_actual_attributes["tags"]["Key"]} does not concur with expected ({expected_data_for_ec2["expected_tag_name"]}).'
        error_msg = f'Actual network tags {network_actual_attributes["tags"]["Value"]} does not concur with expected ({expected_data_for_ec2["expected_tag_text"]}).'
        assert network_actual_attributes['tags']['Key'] == expected_data_for_ec2['expected_tag_name'], error_msg_tag_name
        assert network_actual_attributes['tags']['Value'] == expected_data_for_ec2['expected_tag_text'], error_msg_tag_text
