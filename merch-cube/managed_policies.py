"""Managed Policy"""
from troposphere import FindInMap, Join, Ref
from troposphere.iam import ManagedPolicy
from awacs.aws import Action, Allow, Policy, Statement
from .params import environment_group_param
from .user import merch_cube_user


bucket_list = [
    "internal.confidential/fan_core_in/user_maintained",
    "internal.confidential/fan_core_in/user_maintained/byr-hierarchy",
    "internal.confidential/fan_core_in/user_maintained/byr_dcs",
    "internal.confidential/fan_core_in/user_maintained/byr_item_exclusion_list",
    "internal.confidential/fan_core_in/user_maintained/byr_league_group",
    "internal.confidential/fan_core_in/user_maintained/byr_mvp_list",
    "internal.confidential/fan_core_in/user_maintained/byr_partner_site_group",
    "internal.confidential/fan_core_in/user_maintained/byr_player_status",
    "internal.confidential/fan_core_in/user_maintained/byr_replen_list",
    "internal.confidential/fan_core_in/user_maintained/byr_user_list",
    "internal.confidential/fan_core_in/user_maintained/byr_vendor",
    "internal.confidential/fan_core_in/user_maintained/byr_plan"
]

managed_policy = ManagedPolicy(
    "MerchCubeUserPolicy",
    Description="Specific policy for the merch cube user",
    Path="/",
    PolicyDocument=Policy(
        Version="2012-10-17",
        Statement=[
            Statement(
                Effect=Allow,
                Action=[
                    Action("s3", "DeleteObject"),
                    Action("s3", "GetObject"),
                    Action("s3", "PutObject")

                ],
                Resource=[
                    Join(
                        ".",
                        [
                            "arn:aws:s3:::fanatics",
                            FindInMap(
                                "EnvGroupToEnv",
                                Ref(environment_group_param),
                                "name"
                            ),
                            "%s/*" % bucket
                        ]
                    ) for bucket in bucket_list
                ],
            ),
            Statement(
                Effect=Allow,
                Action=[
                    Action("s3", "ListBucket")

                ],
                Resource=[
                    Join(
                        ".",
                        [
                            "arn:aws:s3:::fanatics",
                            FindInMap(
                                "EnvGroupToEnv",
                                Ref(environment_group_param),
                                "name"
                            ),
                            "internal.confidential"
                        ]
                    )
                ]
            )
        ]
    ),
    Users=[
        Ref(merch_cube_user)
    ]
)
