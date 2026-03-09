# ComfyUI Thumbnail Cycle Generator

A custom node for ComfyUI that triggers [WinThumbsPreloader](https://github.com/Moguri/WinThumbsPreloader) every X cycles to ensure Windows thumbnails are generated for your output folders.

## Features
- **Persistent Counter**: Starts at 0 and increments every time the workflow runs.
- **Cycle Control**: Configurable number of runs before triggering the command.
- **Windows Integration**: Specifically designed to run `WinThumbsPreloader.exe` in silent mode.
- **Path Resolution**: Automatically uses the ComfyUI output directory and allows for a folder suffix.

## Requirements
- **Windows OS**
- **WinThumbsPreloader**: Must be installed and available in your system's `PATH`. If it's not in your PATH, you may need to update the node code with the full absolute path to the executable.

## Installation
1. Clone or download this repository into your `ComfyUI/custom_nodes/` directory:
   ```bash
   cd ComfyUI/custom_nodes/
   git clone https://github.com/your-username/comfyui-thumb-generator
   ```
2. Restart ComfyUI.

## Parameters
- **cycle_time**: (INT) How many times the node should run before triggering the command.
- **folder_suffix**: (STRING) Appended to the default ComfyUI output path (e.g., if you output to a specific subfolder).

## Output
- **current_count**: (INT) Returns the current count (starting from 0).

## How it works
Every time ComfyUI executes the workflow:
1. The internal counter increments.
2. If the counter matches `cycle_time`:
   - It calculates the full path: `{ComfyUI_Output_Dir}/{folder_suffix}`.
   - It runs: `WinThumbsPreloader.exe -s {path}`.
   - The counter resets to 0.
3. The node always reports it has "changed" to ensure it executes on every queue run.
