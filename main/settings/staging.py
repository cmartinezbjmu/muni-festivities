"""
Contains settings for only staging environment.
Note: DEBUG is already set to True in base config.
"""

from .base import *

INTERNAL_IPS = ["127.0.0.1"]

###### ADD INSTALLED APPS ######
THIRD_APPS = [
    'debug_toolbar',
]

LOCAL_APPS = [
    
]

INSTALLED_APPS = INSTALLED_APPS + THIRD_APPS + LOCAL_APPS