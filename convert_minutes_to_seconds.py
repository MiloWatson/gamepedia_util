from mwrogue.esports_client import EsportsClient
from mwrogue.auth_credentials import AuthCredentials
from mwcleric.template_modifier import TemplateModifierBase
import re

credentials = AuthCredentials(user_file="me")
site = EsportsClient('cod-esports', credentials=credentials)
summary = 'Changing M:SS time to seconds'
start_at = 'CWL/2018 Season/Pro League/Stage 1/Scoreboards/Week 1'

regex = r"[0-5]?\d:[0-5]\d"


def get_sec(time_str):
    m, s = time_str.split(':')
    return int(m) * 60 + int(s)


class TemplateModifier(TemplateModifierBase):
    def update_template(self, template):
        if template.has('time'):
            time = template.get('time').value.strip()
            match = re.match(regex, time)
            if match:
                output = get_sec(time)
                template.remove('time')
                template.add('time', output)


TemplateModifier(site, 'Scoreboard/Player', summary=summary).run()
