"""Parameters"""
from troposphere import Parameter

environment_group_param = Parameter(
    "EnvironmentGroup",
    Description="Environment Group [lab, anaprod]",
    Type="String",
    AllowedValues=[
        "lab",
        "anaprod"
    ],
    ConstraintDescription="must be an valid environment group" +
    "[lab, anaprod]"
)

parameters = [
    environment_group_param
]
