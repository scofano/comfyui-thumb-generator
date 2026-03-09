import os
import subprocess
import folder_paths

class ThumbGeneratorNode:
    # Use a class variable to persist state across executions
    _counter = 0

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "cycle_time": ("INT", {"default": 1, "min": 1, "max": 10000, "step": 1}),
                "folder_suffix": ("STRING", {"default": ""}),
            },
        }

    RETURN_TYPES = ("INT",)
    RETURN_NAMES = ("current_count",)
    FUNCTION = "execute"
    CATEGORY = "thumb_generator"

    def execute(self, cycle_time, folder_suffix):
        # Current value to show/return
        current_val = ThumbGeneratorNode._counter
        
        # Increment for next time
        ThumbGeneratorNode._counter += 1
        
        print(f"[ThumbGenerator] Progress: {current_val + 1}/{cycle_time}")

        if ThumbGeneratorNode._counter >= cycle_time:
            # Trigger command
            output_dir = folder_paths.get_output_directory()
            path = os.path.join(output_dir, folder_suffix)
            path = os.path.normpath(path)
            
            command = ["WinThumbsPreloader.exe", "-s", path]
            print(f"[ThumbGenerator] Cycle complete. Executing: {' '.join(command)}")
            
            try:
                # Use subprocess.Popen to avoid hanging ComfyUI
                subprocess.Popen(command, shell=True)
            except Exception as e:
                print(f"[ThumbGenerator] Execution failed: {e}")
            
            # Reset for next run
            ThumbGeneratorNode._counter = 0

        return (current_val,)

    @classmethod
    def IS_CHANGED(s, **kwargs):
        # Always return a new value to ensure the node executes every time the workflow runs
        import time
        return time.time()
