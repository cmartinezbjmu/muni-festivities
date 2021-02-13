"""
Contains settings for only production environment.
Note: DEBUG is already set to False in base config.
"""

from .base import *
import warnings

INTERNAL_IPS = ["127.0.0.1"]

###### ADD INSTALLED APPS ######
THIRD_APPS = [

]

LOCAL_APPS = [
    
]

INSTALLED_APPS = INSTALLED_APPS + THIRD_APPS + LOCAL_APPS

warnings.warn("Do not forget to set ALLOWED_HOSTS variable in DOTENV file.", RuntimeWarning)