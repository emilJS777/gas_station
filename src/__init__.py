from .config import app, db, logger, socketio, mail

# ROUTES
from .Auth import auth_routes
from .Client import client_routes
from .ClientUser import client_user_routes
from .User import user_routes
from .Role import role_routes
from .RolePermission import role_permission_routes
from .UserRole import user_role_routes
from .Permission import permission_routes

from .Device import device_routes
from .DeviceInfo import device_info_routes
from .DeviceSet import device_set_routes

from .DeviceError import DeviceErrorRoutes
from .CashBox import CashBoxRoutes
from .Station import DeviceStationRoutes
from .StationData import StationDataRoutes
from .CashBoxUser import CashBoxUserRoutes
from .Expense import ExpenseRoutes
from .CashBoxData import CashBoxDataRoutes

from .UserImage import UserImageRoutes
from .ClientDevice import ClientDeviceRoutes

