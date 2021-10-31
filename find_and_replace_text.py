from mwrogue.esports_client import EsportsClient
from mwrogue.auth_credentials import AuthCredentials
from mwcleric.page_modifier import PageModifierBase

credentials = AuthCredentials(user_file="me")
site = EsportsClient('cod-esports', credentials=credentials)
summary = 'Fixing tournament display for player media'


class PageModifier(PageModifierBase):
    def update_plaintext(self, text):
        text = text.replace('MLG World Finals 2015', '2016 CWL NA Stage 1 Regular Season')
        return text


PageModifier(site, page_list=site.pages_using('PlayerImageMetadata'), summary=summary).run()
