

# Automated DuckDuckGo Search and Screenshot Archiver

## Description

This Python script automates the process of searching for a list of names on DuckDuckGo using Selenium with Microsoft Edge. It captures full-page screenshots of the search results, extracts the visible text, and saves both outputs with timestamps for documentation or compliance purposes.

## Features

- Automated DuckDuckGo search for multiple names
- Full-page scrolling and screenshot capture
- Image stitching to create a single long screenshot
- Text extraction and saving of search results
- Timestamped output for traceability
- Cleanup of intermediate screenshot files

## Requirements

- Python 3.7+
- Microsoft Edge browser
- Microsoft Edge WebDriver (matching your browser version)

### Python Packages

Install required packages using pip:

```bash
pip install selenium pillow
```

## Setup

1. Update the working directory path:

```python
os.chdir(r"working directory")  # Replace with your desired output folder
```

2. Update the Edge WebDriver path:

```python
edgedriver_path = r"C:\Program Files (x86)\Microsoft\msedgedriver.exe"  # Update if needed
```

3. Modify the list of names as needed:

```python
names = """Name1
Name2
..."""
names = names.split('\n')
names = names[:2]  # Adjust the slice to control how many names are processed
```

## How It Works

For each name in the list:

1. Launches Edge browser and navigates to DuckDuckGo
2. Performs a search and waits for results to load
3. Extracts visible text and saves it to a timestamped `.txt` file
4. Scrolls through the page and captures screenshots
5. Stitches screenshots into one full-page `.png` image
6. Deletes temporary screenshots after stitching

## Output

- `search_text_<name>_<timestamp>.txt`: Contains raw search result text
- `fullpage_stitched <name>.png`: Stitched full-page screenshot

Optional (commented out in the script):

- PDF conversion of the stitched image
