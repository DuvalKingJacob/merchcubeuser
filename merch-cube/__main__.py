"""Main Module."""
from .template import create_cft

if __name__ == "__main__":
    print(create_cft().to_json())
