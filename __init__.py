from .thumb_generator import ThumbGeneratorNode

NODE_CLASS_MAPPINGS = {
    "ThumbGeneratorNode": ThumbGeneratorNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ThumbGeneratorNode": "Thumbnail Cycle Generator"
}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']
