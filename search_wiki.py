from mwrogue.esports_client import EsportsClient
from mwrogue.auth_credentials import AuthCredentials

credentials = AuthCredentials(user_file="me")
site = EsportsClient('cod-esports', credentials=credentials)

site.search_namespace('H3LL', 10006)

# -- Namespace codes --
# https://cod-esports.fandom.com/wiki/Special:AllPages?from=&to=&namespace=0 (to find number)
# Module: 828
# MediaWiki: 8
# Main: 0
# Special: -1
# Media: -2
# File: 6
# Template: 10
# Help: 12
# Category: 14
# Predictions: 10010
# Data: 10006



