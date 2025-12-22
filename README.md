# Folder_organizer
A configurable Python automation tool that organizes files into structured folders based on file extension, size, and modification date, with full support for dry-run mode and logging.
This project is designed to be safe, reusable, and easy to customize without touching the code.

## Features
- Organizes files by **category** (Images, Documents, Audio, Video, Archives, etc.)
- Creates **date-based folders** (`YYYY-MM`)
- Further sorts files by **size buckets** (Small / Medium / Large / Huge)
- **Dry-run mode** (preview changes without moving files)
- Detailed **logging** to a file
- Fully configurable via `config.json`

## How to run the script
Open a terminal in the project directory
Make sure you are inside the folder containing main.py.

Run "python main.py" If that doesn’t work, try: python3 main.py
# On macOS / Linux
python3 main.py
(Some systems still support python, but python3 is recommended.)

## Configuration (`config.json`)
All behavior is controlled via `config.json`.  
You **do not need to edit Python code** to change how the script works.

### Example `config.json`

```json
{
  "target_path": "C:/Users/examplepath",   //This is the folder that will be organized. Change it to any directory you want. Ex: "C:/Users/YourName/Downloads"
  "dry_run": true, //True -> No files are moved, actions are only logged (safe preview mode) | False -> Files are actually moved into organized folders
  "log_file": "organizer.log", //Name of the log file where all actions and errors are recorded, you can name this freely
  "log_level": "INFO"
} 

Check the log file
After running, open the log file defined in config.json:
log_file.log

It will contain:
what files were processed
what would be moved (dry-run)
what was actually moved
any errors encountered
 
