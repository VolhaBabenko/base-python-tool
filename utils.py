"""
Utility functions for the Base Guild tool.
"""

import hashlib
import json
from datetime import datetime

def generate_file_hash(file_path):
    """
    Generate MD5 hash for a file.
    
    Args:
        file_path (str): Path to the file
        
    Returns:
        str: MD5 hash or error message
    """
    try:
        with open(file_path, 'rb') as f:
            file_hash = hashlib.md5()
            while chunk := f.read(8192):
                file_hash.update(chunk)
        return file_hash.hexdigest()
    except Exception as e:
        return f"Error: {str(e)}"

def format_timestamp(timestamp=None):
    """
    Format timestamp for display.
    
    Args:
        timestamp (float, optional): Unix timestamp. Defaults to current time.
        
    Returns:
        str: Formatted timestamp
    """
    if timestamp is None:
        timestamp = datetime.now().timestamp()
    return datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d %H:%M:%S")

def validate_json(data):
    """
    Validate if data is valid JSON.
    
    Args:
        data (str): JSON string to validate
        
    Returns:
        bool: True if valid JSON, False otherwise
    """
    try:
        json.loads(data)
        return True
    except json.JSONDecodeError:
        return False
