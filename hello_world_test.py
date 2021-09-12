from river_mwclient.esports_client import EsportsClient
from river_mwclient.auth_credentials import AuthCredentials
import mwparserfromhell

credentials = AuthCredentials(user_file="testbot")
site = EsportsClient('halo-esports', credentials=credentials)  # Set wiki
summary = 'hello world test'  # Set summary

pages = site.client.pages["User:Ispoonz"]

text = pages.text()
print(text)

pages.save('hello world', summary=summary)