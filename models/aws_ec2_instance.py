"""Module contains 2 classes:
Class AWSInstance: awaits AWS instance id and name of the region (default - eu-central-1).
Provides 'tags', 'image_id', 'private_ip_address', 'public_ip_address', 'state and security_groups'
as attributes for the given instance.
Class AWSNetworkInterface: awaits AWS Network Interface id and name of the region (default - eu-central-1).
Provides 'tags' and 'ip_address' as attributes for the given Network Interface."""
import boto3

class AWSInstance:
    """
    Class AWSInstance: awaits AWS instance id and name of the region (default - eu-central-1a).
    Provides 'tags', 'image_id', 'private_ip_address', 'public_ip_address', 'state and security_groups'
    as attributes for the given instance.
    """
    def __init__(self, instance_id: str, region_name: str = 'eu-central-1'):
        """Init method of class AWSInstance creates EC2 AWS Instance using inputed instance id and assignes attributes
        for this instance: tags info, id of the image, private ip address, public ip address, state status and security
        groups information."""
        self._ec2 = boto3.resource('ec2', region_name, aws_access_key_id='AKIAYUV3MY7THKW7VIG5',
                             aws_secret_access_key='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')
        self_.instance = self._ec2.Instance(instance_id)

        self.tag = self._instance.tags
        self.image_id = self._instance.image_id
        self.private_ip_address = self._instance.private_ip_address
        self.public_ip_address = self._instance.public_ip_address
        self.state = self._instance.state
        self.security_groups = self._instance.security_groups


class AWSNetworkInterface:
    """
    Class AWSNetworkInterface: awaits AWS Network Interface id and name of the region (default - eu-central-1a).
    Provides 'tags' and 'ip_address' as attributes for the given Network Interface.
    """
    def __init__(self, network_interface_id: str, region_name: str = 'eu-central-1'):
        """Init method of class AWSInstance creates EC2 Network Interface Instance using inputed instance id and
        assignes attributes for this instance: tags info and private ip address."""
        self._ec2 = boto3.resource('ec2', region_name, aws_access_key_id='AKIAYUV3MY7THKW7VIG5',
                             aws_secret_access_key='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')
        self._network_interface = self._ec2.NetworkInterface(network_interface_id)

        self.tag = self._network_interface.tag_set
        self.ip_address = self._network_interface.private_ip_address

class AWSSecurityCroup:
    """
    Class AAWSSecurityCroup: awaits AWS Security Croup id.
    Provides ip permissions as attribute for the given Security Croup.
    """
    def __init__(self, security_group_id: str):
        """Init method of class AWSSecurityCroup creates EC2 AWS Security Croup Instance using inputed security group id."""
        self._ec2 = boto3.resource('ec2')
        self._security_group = self._ec2.SecurityGroup(security_group_id)

    def get_allowed_ports_numbers(self):
        """Method gets ip permissions for EC2 AWS Security Croup Instance and extracts allowed ports numbers from this
        permission info: list of port numbers for FromPorts and ToPorts"""
        sg_permissions = self._security_group.ip_permissions
        self.allowed_ports = {'FromPort': [], 'ToPort': []}
        for item in sg_permissions:
            self.allowed_ports['FromPort'].append(item['FromPort'])
            self.allowed_ports['ToPort'].append(item['ToPort'])
