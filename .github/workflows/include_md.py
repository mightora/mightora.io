#!/usr/bin/env python3
"""
Markdown Include Processor

This script scans all markdown files in the repository and processes
include-md directives to fetch and embed remote markdown content.

Usage: python include_md.py [root_directory]
"""

import os
import re
import sys
import urllib.request
import urllib.error
from pathlib import Path


def fetch_remote_markdown(url):
    """
    Fetch markdown content from a remote URL.
    
    Args:
        url (str): The URL to fetch content from
        
    Returns:
        str: The content of the remote markdown file
        
    Raises:
        urllib.error.URLError: If the URL cannot be fetched
    """
    try:
        with urllib.request.urlopen(url) as response:
            return response.read().decode('utf-8')
    except urllib.error.URLError as e:
        print(f"Error fetching {url}: {e}")
        raise


def process_include_directive(match):
    """
    Process a single include-md directive.
    
    Args:
        match: Regular expression match object containing the directive
        
    Returns:
        str: The processed content to replace the directive
    """
    url = match.group(1)
    skip_lines = 0
    
    # Check if skip parameter is specified
    skip_match = re.search(r'skip=(\d+)', match.group(0))
    if skip_match:
        skip_lines = int(skip_match.group(1))
    
    try:
        print(f"Fetching content from: {url}")
        content = fetch_remote_markdown(url)
        
        if skip_lines > 0:
            lines = content.split('\n')
            if len(lines) > skip_lines:
                content = '\n'.join(lines[skip_lines:])
                print(f"Skipped {skip_lines} lines from {url}")
            else:
                print(f"Warning: Requested to skip {skip_lines} lines, but file only has {len(lines)} lines")
        
        return content
        
    except Exception as e:
        error_msg = f"<!-- Error fetching {url}: {e} -->"
        print(f"Error processing {url}: {e}")
        return error_msg


def process_markdown_file(file_path):
    """
    Process a single markdown file for include-md directives.
    
    Args:
        file_path (Path): Path to the markdown file to process
        
    Returns:
        bool: True if the file was modified, False otherwise
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return False
    
    # Pattern to match include-md directives
    # Matches: <--include-md URL [skip=N] -->
    pattern = r'<--include-md\s+([^\s]+)(?:\s+skip=(\d+))?\s*-->'
    
    # Find all include directives
    matches = list(re.finditer(pattern, content))
    
    if not matches:
        return False
    
    print(f"Processing {file_path} - found {len(matches)} include directive(s)")
    
    # Process matches in reverse order to maintain string positions
    modified_content = content
    for match in reversed(matches):
        try:
            replacement = process_include_directive(match)
            modified_content = modified_content[:match.start()] + replacement + modified_content[match.end():]
        except Exception as e:
            print(f"Error processing directive in {file_path}: {e}")
            continue
    
    # Write the modified content back to the file
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(modified_content)
        print(f"Updated {file_path}")
        return True
    except Exception as e:
        print(f"Error writing to {file_path}: {e}")
        return False


def scan_directory(root_dir):
    """
    Scan directory for markdown files and process include directives.
    
    Args:
        root_dir (Path): Root directory to scan
        
    Returns:
        tuple: (total_files_processed, total_files_modified)
    """
    markdown_files = list(root_dir.rglob('*.md'))
    
    if not markdown_files:
        print("No markdown files found.")
        return 0, 0
    
    print(f"Found {len(markdown_files)} markdown files to scan")
    
    files_processed = 0
    files_modified = 0
    
    for md_file in markdown_files:
        try:
            files_processed += 1
            if process_markdown_file(md_file):
                files_modified += 1
        except Exception as e:
            print(f"Error processing {md_file}: {e}")
    
    return files_processed, files_modified


def main():
    """Main function to run the markdown include processor."""
    # Get root directory from command line argument or use current directory
    if len(sys.argv) > 1:
        root_dir = Path(sys.argv[1])
    else:
        root_dir = Path('.')
    
    if not root_dir.exists():
        print(f"Error: Directory {root_dir} does not exist")
        sys.exit(1)
    
    if not root_dir.is_dir():
        print(f"Error: {root_dir} is not a directory")
        sys.exit(1)
    
    print(f"Scanning directory: {root_dir.absolute()}")
    
    try:
        files_processed, files_modified = scan_directory(root_dir)
        
        print(f"\nSummary:")
        print(f"Files processed: {files_processed}")
        print(f"Files modified: {files_modified}")
        
        if files_modified > 0:
            print("✅ Include processing completed successfully")
        else:
            print("ℹ️  No include directives found")
            
    except KeyboardInterrupt:
        print("\n⚠️  Process interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
