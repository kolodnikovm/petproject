from .apps import *
from .auth import *
from .base import *
from .middlewares import *
from .statics import *
from .templates import *

try:
    from .local import *
except ImportError:
    print('No local settings found')
