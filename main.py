#!/usr/bin/env python3
"""
Base Guild Python Tool
A utility tool with multiple features.
"""

import sys
from config import print_config, get_config
from utils import format_timestamp, validate_json
import argparse

def process_file(file_path):
    """Process a file and display information."""
    print(f"📁 Processing file: {file_path}")
    # In a real app, this would do actual file processing
    print(f"Timestamp: {format_timestamp()}")
    return True

def show_help():
    """Display help information."""
    config = get_config()
    print(f"\n{config['app_name']} v{config['version']}")
    print("=" * 40)
    print("Available commands:")
    print("  --help, -h     Show this help message")
    print("  --config, -c   Show configuration")
    print("  --process FILE Process a file")
    print("  --test         Run tests")
    print("\nExample: python main.py --config")

def main():
    """Main entry point with argument parsing."""
    parser = argparse.ArgumentParser(description="Base Guild Python Tool")
    parser.add_argument('-c', '--config', action='store_true', help='Show configuration')
    parser.add_argument('-p', '--process', type=str, help='Process a file')
    parser.add_argument('-t', '--test', action='store_true', help='Run tests')
    
    if len(sys.argv) == 1:
        show_help()
        return
    
    args = parser.parse_args()
    
    if args.config:
        print_config()
    elif args.process:
        process_file(args.process)
    elif args.test:
        print("Running tests...")
        # In a real app: os.system("pytest test_utils.py")
        print("Tests would run here (pytest framework)")
    else:
        show_help()

if __name__ == "__main__":
    main()
