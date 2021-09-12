from mwrogue.esports_client import EsportsClient
from mwrogue.auth_credentials import AuthCredentials

credentials = AuthCredentials(user_file="me")
site = EsportsClient('halo-esports', credentials=credentials)

site.search_namespace('Module:Class', 828)
