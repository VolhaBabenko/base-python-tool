"""
Configuration settings for the Base Guild tool.
"""

CONFIG = {
    "app_name": "Base Guild Tool",
    "version": "1.0.0",
    "author": "Base Guild Member",
    "repository": "https://github.com/user/base-python-tool",
    "features": [
        "file operations",
        "data processing",
        "API integration"
    ]
}

def get_config():
    """Return the application configuration."""
    return CONFIG.copy()

def print_config():
    """Print the current configuration."""
    print("=== Application Configuration ===")
    for key, value in CONFIG.items():
        print(f"{key}: {value}")
