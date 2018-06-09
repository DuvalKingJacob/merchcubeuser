"""Creates the bucket user and policies"""
from troposphere.iam import User

merch_cube_user = User(
    "merchcubeuser"
)
