from mwrogue.esports_client import EsportsClient
from mwparserfromhell.nodes import Template
from mwrogue.auth_credentials import AuthCredentials
from mwcleric.template_modifier import TemplateModifierBase

credentials = AuthCredentials(user_file="me")
site = EsportsClient('cod-esports', credentials=credentials)
summary = 'TeePee -> TeeP from MW season onwards'


class TemplateModifier(TemplateModifierBase):
    def update_template(self, template: Template):
        if template.has('player'):
            if template.get('player').value.strip() == 'TeePee':
                template.remove('player')
                template.add('player', 'TeeP', before='role')


TemplateModifier(site, 'RCPlayer', summary=summary).run()
