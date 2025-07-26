#!/usr/bin/env python3
"""
Hugo Cards Updater

This script automatically updates card sections in _index.md files
based on the directory structure and available tools.

Usage: python update_cards.py [root_directory]
"""

import os
import re
import sys
from pathlib import Path


def load_icons(icons_file_path):
    """
    Load icons from the icons.yaml file.
    
    Args:
        icons_file_path (str): Path to the icons.yaml file
        
    Returns:
        dict: Dictionary of icon names and their SVG content
    """
    icons = {}
    try:
        with open(icons_file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Simple parsing of YAML-like structure for icons
        lines = content.split('\n')
        for line in lines:
            if ':' in line and not line.strip().startswith('#'):
                parts = line.split(':', 1)
                if len(parts) == 2:
                    key = parts[0].strip()
                    value = parts[1].strip()
                    if key and value:
                        icons[key] = value
                        
    except FileNotFoundError:
        print(f"Warning: Icons file not found at {icons_file_path}")
    except Exception as e:
        print(f"Error parsing icons file: {e}")
        
    return icons


def determine_icon_and_tag(path, icons):
    """
    Determine the appropriate icon and tag based on folder structure.
    Rules applied in order:
    a. if folder contains "powershell" use powershell icon
    b. if folder contains "pipeline" use rocket icon  
    c. if folder contains "calendar" use calendar icon
    d. if folder contains "email" use email-at icon
    e. if folder contains "automate" use powerautomate icon
    
    Args:
        path (str): The path to analyze
        icons (dict): Available icons
        
    Returns:
        tuple: (icon_name, tag_name, tag_color)
    """
    path_lower = path.lower()
    
    # Apply rules in the specified order
    if 'powershell' in path_lower or 'dataverse-4-teams' in path_lower:
        return 'powershell', 'Powershell', 'green'
    elif 'pipeline' in path_lower:
        return 'rocket', 'Pipeline', 'green'
    elif 'calendar' in path_lower or 'working-day' in path_lower:
        return 'calendar', 'Calendar', 'blue'
    elif 'email' in path_lower:
        return 'email-at', 'Email', 'blue'
    elif 'automate' in path_lower:
        return 'powerautomate', 'Flow', 'blue'
    else:
        # Additional defaults based on common patterns
        if 'power-automate' in path_lower or 'flow' in path_lower:
            return 'powerautomate', 'Flow', 'blue'
        elif 'devops' in path_lower or 'cicd' in path_lower or 'playwright' in path_lower:
            return 'rocket', 'CICD', 'green'
        else:
            return 'rocket', 'Tool', 'gray'


def extract_title_from_frontmatter(file_path):
    """
    Extract the title from a markdown file's frontmatter.
    
    Args:
        file_path (str): Path to the markdown file
        
    Returns:
        str: The title from frontmatter, or filename if not found
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Check if file starts with frontmatter
        if content.startswith('---'):
            # Find the end of frontmatter
            end_match = re.search(r'\n---\n', content)
            if end_match:
                frontmatter = content[:end_match.start()]
                # Extract title
                title_match = re.search(r'^title:\s*(.+)$', frontmatter, re.MULTILINE)
                if title_match:
                    return title_match.group(1).strip().strip('"\'')
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
    
    # Fallback to filename
    return Path(file_path).parent.name.replace('-', ' ').title()


def find_tools_in_directory(content_dir, target_dir):
    """
    Find all tools (directories with _index.md) within a target directory.
    
    Args:
        content_dir (str): Root content directory
        target_dir (str): Target directory to search within
        
    Returns:
        list: List of tool info dictionaries
    """
    tools = []
    seen_titles = set()  # To avoid duplicates
    target_path = Path(content_dir) / target_dir if target_dir else Path(content_dir)
    
    if not target_path.exists():
        return tools
    
    # Walk through all subdirectories
    for root, dirs, files in os.walk(target_path):
        if '_index.md' in files:
            # Skip the root directory itself if it's the target
            if root == str(target_path):
                continue
                
            index_file = os.path.join(root, '_index.md')
            
            # Get relative path from content directory
            rel_path = os.path.relpath(root, content_dir)
            rel_path = rel_path.replace('\\', '/')  # Ensure forward slashes
            
            # Skip duplicated paths under /tools/ if we already have the main version
            if '/tools/' in rel_path:
                main_path = rel_path.replace('/tools/', '/')
                if any(tool['path'] == main_path for tool in tools):
                    continue
            
            # Extract title
            title = extract_title_from_frontmatter(index_file)
            
            # Skip if we already have this title (avoid duplicates)
            if title in seen_titles:
                continue
            seen_titles.add(title)
            
            # Determine icon and tag
            icon, tag, tag_color = determine_icon_and_tag(rel_path, {})
            
            tools.append({
                'link': f'/{rel_path}/',
                'title': title,
                'icon': icon,
                'tag': tag,
                'tag_color': tag_color,
                'path': rel_path
            })
    
    return sorted(tools, key=lambda x: x['title'])


def generate_cards_section(tools):
    """
    Generate the cards section content.
    
    Args:
        tools (list): List of tool dictionaries
        
    Returns:
        str: Generated cards section
    """
    if not tools:
        return "{{< cards >}}\n{{< /cards >}}"
    
    cards_content = "{{< cards >}}\n"
    for tool in tools:
        cards_content += f'  {{{{< card link="{tool["link"]}" title="{tool["title"]}" icon="{tool["icon"]}" tag="{tool["tag"]}" tagColor="{tool["tag_color"]}">}}}}\n'
    cards_content += "{{< /cards >}}"
    
    return cards_content


def update_index_file(file_path, content_dir):
    """
    Update a single _index.md file with the appropriate cards.
    
    Args:
        file_path (str): Path to the _index.md file
        content_dir (str): Root content directory
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Determine the directory this index file is in
        index_dir = os.path.dirname(file_path)
        rel_dir = os.path.relpath(index_dir, content_dir)
        
        # If we're at the root, search everything; otherwise search within the subdirectory
        search_dir = '' if rel_dir == '.' else rel_dir
        
        # Find tools in this directory and subdirectories
        tools = find_tools_in_directory(content_dir, search_dir)
        
        # Generate new cards section
        new_cards = generate_cards_section(tools)
        
        # Find and replace existing cards section
        cards_pattern = r'{{<\s*cards\s*>}}.*?{{<\s*/cards\s*>}}'
        cards_matches = list(re.finditer(cards_pattern, content, re.DOTALL | re.IGNORECASE))
        
        if cards_matches:
            # Replace all cards sections (there might be multiple)
            offset = 0
            for match in cards_matches:
                start = match.start() + offset
                end = match.end() + offset
                
                # Replace this cards section
                new_content = content[:start] + new_cards + content[end:]
                offset += len(new_cards) - (end - start)
                content = new_content
            
            # Write back to file
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print(f"Updated {file_path} with {len(tools)} tools")
        else:
            print(f"No cards section found in {file_path}")
            
    except Exception as e:
        print(f"Error updating {file_path}: {e}")


def process_all_index_files(root_dir):
    """
    Process all _index.md files in the content directory.
    
    Args:
        root_dir (str): Root directory of the Hugo site
    """
    content_dir = os.path.join(root_dir, 'content')
    
    if not os.path.exists(content_dir):
        print(f"Content directory not found: {content_dir}")
        return
    
    # Find all _index.md files
    index_files = []
    for root, dirs, files in os.walk(content_dir):
        if '_index.md' in files:
            index_files.append(os.path.join(root, '_index.md'))
    
    print(f"Found {len(index_files)} _index.md files")
    
    # Update each index file
    for index_file in index_files:
        update_index_file(index_file, content_dir)


def main():
    """Main function."""
    # Get root directory from command line argument or use current directory
    root_dir = sys.argv[1] if len(sys.argv) > 1 else '.'
    root_dir = os.path.abspath(root_dir)
    
    print(f"Processing Hugo site at: {root_dir}")
    
    # Load icons (optional, for validation)
    icons_file = os.path.join(root_dir, 'data', 'icons.yaml')
    icons = load_icons(icons_file)
    print(f"Loaded {len(icons)} icons")
    
    # Process all index files
    process_all_index_files(root_dir)
    
    print("Cards update complete!")


if __name__ == '__main__':
    main()
