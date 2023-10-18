# Example: Importing modules from the networkmanager package
from .client import establish_connection, check_connection_status

# __all__ defines what modules are available when using "from [package] import *"
__all__ = ["establish_connection", "check_connection_status"]
