from .config import app, db, logger

# ROUTES
from .auth import auth_routes
from .client import client_routes
from .client_user import client_user_routes
from .user import user_routes
from .firm import firm_routes
from .firm_user import firm_user_routes
from .role import role_routes
from .role_permission import role_permission_routes
from .user_role import user_role_routes
from .permission import permission_routes

from .device import device_routes
from .device_info import device_info_routes
from .device_set import device_set_routes
