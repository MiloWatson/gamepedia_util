from mwrogue.esports_client import EsportsClient
from mwrogue.auth_credentials import AuthCredentials
from mwcleric.page_modifier import PageModifierBase
import re

credentials = AuthCredentials(user_file="bot")
site = EsportsClient('cod-esports', credentials=credentials)
summary = 'DAL -> DALE prep for name change'

# set entries to be changed here (always uppercase)
old = 'DAL'
old_long = 'DALLAS'
new = 'DALE'

# for matching bracket inputs
regex = r"((R\d+M\d+_team_\d)=(.+?)\|)"


class PageModifier(PageModifierBase):
    def update_plaintext(self, text):
        for m in re.findall(regex, text):
            team = m[2].upper().strip()
            if team == old or team == old_long:
                text = text.replace(m[0], m[1] + '=' + new + ' |')
        return text


PageModifier(site, page_list=site.pages_using('Bracket'), summary=summary).run()
