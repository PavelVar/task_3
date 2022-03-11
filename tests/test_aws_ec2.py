"""Module contains tests of EC instance, EC2 Security Group and EC2 Network Interface charachteristics"""
import pytest

import asserts.aws_ec2_asserts
from .models.aws_ec2_instance import AWSInstance


def test_ec2_image_id(ec2_instance_actual_attributes, expected_data_for_ec2: dict, ec2_instance: AWSInstance):
    asserts.check_instance_image(ec2_instance_actual_attributes, expected_data_for_ec2)

def test_ec2_instance_state(ec2_instance_actual_attributes):
    asserts.check_instance_state(ec2_instance_actual_attributes)

def test_ec2_instance_public_ip(ec2_instance_actual_attributes, expected_data_for_ec2: dict):
    asserts.check_instance_public_ip(ec2_instance_actual_attributes, expected_data_for_ec2)

def test_ec2_security_rules_for_ports(security_group_actual_ports, expected_data_for_ec2: dict):
    asserts.check_security_rules_for_ports(security_group_actual_ports, expected_data_for_ec2)

def test_ec2_instance_tags(ec2_instance_actual_attributes, expected_data_for_ec2: dict):
    asserts.check_instance_tags(ec2_instance_actual_attributes, expected_data_for_ec2)

def test_ec2_network_interface_ip(network_actual_attributes, expected_data_for_ec2: dict):
    check_network_interface_ip(network_actual_attributes, expected_data_for_ec2)

def test_ec2_network_interface_tags(network_actual_attributes, expected_data_for_ec2: dict):
    asserts.check_network_interface_tags(network_actual_attributes, expected_data_for_ec2)
