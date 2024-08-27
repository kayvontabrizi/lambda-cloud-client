# coding: utf-8

"""
    Lambda Cloud API

    API for interacting with the Lambda GPU Cloud

    The version of the OpenAPI document: 1.5.3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from lambda_cloud_client.models.region import Region


class TestRegion(unittest.TestCase):
    """Region unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Region:
        """Test Region
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `Region`
        """
        model = Region()
        if include_optional:
            return Region(
                name = 'us-tx-1',
                description = 'Austin, Texas'
            )
        else:
            return Region(
                name = 'us-tx-1',
                description = 'Austin, Texas',
        )
        """

    def testRegion(self):
        """Test Region"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
