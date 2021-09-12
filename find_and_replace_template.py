from mwrogue.esports_client import EsportsClient
from mwrogue.auth_credentials import AuthCredentials
from mwcleric.template_modifier import TemplateModifierBase

credentials = AuthCredentials(user_file="me")
site = EsportsClient('cod-esports', credentials=credentials)
summary = 'Removing storeroster=yes at end of season'


class TemplateModifier(TemplateModifierBase):
    def update_template(self, template):
        if not template.has('storeroster'):
            return
        else:
            template.remove('storeroster')


TemplateModifier(site, 'TeamRoster', summary=summary).run()
