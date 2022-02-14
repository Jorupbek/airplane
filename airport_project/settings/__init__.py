import os
import json

CONFIG_FILE = '/etc/config.json'

try:
    from .docker import *

except KeyError:
    from .local import *

