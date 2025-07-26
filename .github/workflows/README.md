# Markdown Include Processor (`include_md.py`)

This script scans all markdown (`.md`) files in your repository and processes custom include directives to fetch and embed remote markdown content. It is designed to be run automatically in your CI pipeline before building your Hugo site, but can also be run manually.

## How It Works

- The script looks for lines in markdown files that match this pattern:
  ```
  <--include-md https://raw.githubusercontent.com/user/repo/branch/path/to/file.md skip=2 -->
  ```
  - The `skip=N` parameter is optional. If present, the script will skip the first N lines of the included file.
- For each directive found, the script fetches the remote markdown file, skips the specified number of lines, and replaces the directive with the fetched content.
- All `.md` files in the repository (recursively) are processed.

## Usage

You can run the script manually:

```sh
python3 include_md.py [root_directory]
```
- If `root_directory` is not specified, the current directory is used.

In the GitHub Actions pipeline, the script is run automatically before the Hugo build step.

## Example

If your markdown file contains:

```
<--include-md https://raw.githubusercontent.com/example/repo/main/README.md skip=2 -->
```

The script will fetch the remote file, skip the first 2 lines, and insert the rest of the content in place of the directive.

## Error Handling
- If the remote file cannot be fetched, an HTML comment with the error is inserted in place of the directive.

## Requirements
- Python 3.x
- Internet access (for fetching remote files)

## Typical Workflow Integration
- Place this script in your `.github/workflows/` folder.
- Add a step in your CI pipeline to run the script before building your site.

---

For questions or improvements, please open an issue or pull request in this repository.
