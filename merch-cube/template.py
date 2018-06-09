"""Main File to generate CFT"""
from troposphere import Template
from .params import parameters
from .maps import env_group_to_env
from .managed_policies import managed_policy
from .user import merch_cube_user


def create_cft():
    """"Creates the CFT"""
    template = Template()
    template.add_version("2010-09-09")
    template.add_description(
        "CFT to create merch cube user"
    )

    # Add Parameters
    for param in parameters:
        template.add_parameter(param)

    # Add Maps
    template.add_mapping("EnvGroupToEnv", env_group_to_env)

    # Add Resources
    template.add_resource(managed_policy)

    template.add_resource(merch_cube_user)

    return template

if __name__ == "__main__":
    print(create_cft().to_json())
