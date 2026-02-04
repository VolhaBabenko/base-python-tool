"""
Tests for utility functions.
"""

import pytest
from utils import format_timestamp, validate_json

def test_format_timestamp():
    """Test timestamp formatting."""
    result = format_timestamp(1672531200)  # 2023-01-01 00:00:00
    assert "2023-01-01" in result
    
def test_format_current_timestamp():
    """Test formatting current timestamp."""
    result = format_timestamp()
    assert len(result) == 19  # YYYY-MM-DD HH:MM:SS
    
def test_validate_json():
    """Test JSON validation."""
    assert validate_json('{"key": "value"}') == True
    assert validate_json('invalid json') == False
    assert validate_json('') == False
    
def test_validate_json_complex():
    """Test complex JSON validation."""
    complex_json = '''
    {
        "name": "Base Guild",
        "commits": 15,
        "files": ["main.py", "utils.py", "config.py"]
    }
    '''
    assert validate_json(complex_json) == True

if __name__ == "__main__":
    pytest.main([__file__])
