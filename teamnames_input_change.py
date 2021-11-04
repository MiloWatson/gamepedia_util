from mwrogue.esports_client import EsportsClient
from mwrogue.auth_credentials import AuthCredentials
from mwcleric.template_modifier import TemplateModifierBase

credentials = AuthCredentials(user_file="bot")
site = EsportsClient('cod-esports', credentials=credentials)
summary = 'DAL -> DALE prep for name change'

# set entries to be changed here (always uppercase)
old = 'DAL'
old_long = 'DALLAS'
new = 'DALE'
new_long = 'Dallas Empire'


class TemplateModifier(TemplateModifierBase):
    def update_template(self, template):
        if template.has('team'):
            team = template.get('team').value.strip().upper()
            if team == old:
                template.remove('team')
                template.add('team', new)
            if team == old_long:
                template.remove('team')
                template.add('team', new_long)
            return
        if template.has('team1') and template.has('team2'):
            if template.get('team1').value.strip().upper() == old:
                template.remove('team1')
                template.add('team1', new, before='team2')
            if template.get('team2').value.strip().upper() == old:
                template.remove('team2')
                template.add('team2', new, before='team1score')
            return
        if template.name == 'Infobox Tournament':
            if template.has('host'):
                if template.get('host').value.strip().upper() == old:
                    template.remove('host')
                    template.add('host', new, before='sponsor')
            if template.has('first'):
                if template.get('first').value.strip().upper() == old:
                    template.remove('first')
                    template.add('first', new, before='second')
                elif template.get('second').value.strip().upper() == old:
                    template.remove('second')
                    template.add('second', new, before='third')
                elif template.get('third').value.strip().upper() == old:
                    template.remove('third')
                    template.add('third', new, before='fourth')
                elif template.get('fourth').value.strip().upper() == old:
                    template.remove('fourth')
                    template.add('fourth', new)
            return

        '''
        if template.name == 'Team' or template.name == 'team' or template.name == 'StandingsLine':
            if template.get(1).value.strip().upper() == old:
                template.remove(1)
                template.add(1, new)
        return
        '''

'''
TemplateModifier(site, 'RosterChangeData/Line', summary=summary).run()
TemplateModifier(site, 'ExternalContent/Line', summary=summary).run()
TemplateModifier(site, 'TournamentResults/Line', summary=summary).run()
TemplateModifier(site, 'PlayerImageMetadata', summary=summary).run()
TemplateModifier(site, 'PlayerStickers', summary=summary).run()
TemplateModifier(site, 'TeamRosterPhotoMetadata', summary=summary).run()
TemplateModifier(site, 'MatchSchedule', summary=summary).run()
TemplateModifier(site, 'Infobox Tournament', summary=summary).run()
TemplateModifier(site, 'CircuitPointsLine', summary=summary).run()
TemplateModifier(site, 'TeamRoster', summary=summary).run()
'''
TemplateModifier(site, 'Bracket', summary=summary, ).run()
'''
TemplateModifier(site, 'Team', summary=summary).run()
TemplateModifier(site, 'StandingsLine', summary=summary).run()
'''
