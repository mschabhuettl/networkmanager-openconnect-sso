# Example: Importing main modules to make them publicly available
from .main import main_function
from .networkmanager import client
from .ui import main_window

# __all__ defines what modules are available when using "from [package] import *"
__all__ = ["main_function", "client", "main_window"]
