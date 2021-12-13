from mwrogue.esports_client import EsportsClient
from mwrogue.auth_credentials import AuthCredentials
from mwcleric.template_modifier import TemplateModifierBase
from string import ascii_uppercase

credentials = AuthCredentials(user_file="bot")
site = EsportsClient('cod-esports', credentials=credentials)
summary = 'DAL -> DALE prep for name change'

# set current input used for team that needs to be changed (must be uppercase)
old = 'DAL'
old_long = 'DALLAS'
# don't touch old_inputs
old_inputs = {old, old_long}
# set new input to be used for team
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
        if template.name.matches('RCPlayer'):
            if template.has('loaned_to'):
                if template.get('loaned_to').value.strip().upper() in old_inputs:
                    template.remove('loaned_to')
                    template.add('loaned_to', new)
            if template.has('loaned_from'):
                if template.get('loaned_from').value.strip().upper() in old_inputs:
                    template.remove('loaned_from')
                    template.add('loaned_from', new)
            return
        if template.has('team1') and template.has('team2'):
            if template.get('team1').value.strip().upper() in old_inputs:
                template.remove('team1')
                template.add('team1', new, before='team2')
            if template.get('team2').value.strip().upper() in old_inputs:
                template.remove('team2')
                template.add('team2', new, before='team1score')
            return
        if template.name.matches('Infobox Tournament'):
            if template.has('host'):
                if template.get('host').value.strip().upper() in old_inputs:
                    template.remove('host')
                    template.add('host', new, before='sponsor')
            if template.has('first'):
                if template.get('first').value.strip().upper() in old_inputs:
                    template.remove('first')
                    template.add('first', new, before='second')
                elif template.get('second').value.strip().upper() in old_inputs:
                    template.remove('second')
                    template.add('second', new, before='third')
                elif template.get('third').value.strip().upper() in old_inputs:
                    template.remove('third')
                    template.add('third', new, before='fourth')
                elif template.get('fourth').value.strip().upper() in old_inputs:
                    template.remove('fourth')
                    template.add('fourth', new)
            return
        if template.name.matches('ExternalContent/Line'):
            if template.has('teams'):
                teams = template.get('teams').value.strip().upper()
                team_list = teams.split(',')
                if old in team_list or old_long in team_list:
                    modified_list = [new if team in old_inputs else team for team in team_list]
                    teams_string = ','.join(modified_list)
                    template.remove('teams')
                    template.add('teams', teams_string, before='publication')
            return
        if template.name.matches('AutoStandings'):
            if template.has('teamlist'):
                teams = template.get('teamlist').value.strip().upper()
                team_list = teams.split(',')
                if old in team_list or old_long in team_list:
                    modified_list = [new if team in old_inputs else team for team in team_list]
                    teams_string = ','.join(modified_list)
                    template.remove('teamlist')
                    template.add('teamlist', teams_string, before='places')
            if template.has('finalorder'):
                teams = template.get('finalorder').value.strip().upper()
                team_list = teams.split(',')
                if old in team_list or old_long in team_list:
                    modified_list = [new if team in old_inputs else team for team in team_list]
                    teams_string = ','.join(modified_list)
                    template.remove('finalorder')
                    template.add('finalorder', teams_string, before='places')
            return
        if template.name.matches('TournamentGroups'):
            for char in ascii_uppercase:
                group = 'Group ' + char
                if template.has(group):
                    teams = template.get(group).value.strip().upper()
                    team_list = teams.split(',')
                    if old in team_list or old_long in team_list:
                        modified_list = [new if team in old_inputs else team for team in team_list]
                        teams_string = ','.join(modified_list)
                        template.remove(group)
                        template.add(group, teams_string)
            return
        if template.name.matches('Team') or template.name.matches('team') or template.name.matches('StandingsLine'):
            if template.get(1).value.strip().upper() in old_inputs:
                template.remove(1)
                template.add(1, new)
            return


# TemplateModifier(site, 'RosterChangeData/Line', summary=summary).run()
# TemplateModifier(site, 'RCPlayer', summary=summary).run()
# TemplateModifier(site, 'TournamentResults/Line', summary=summary).run()
# TemplateModifier(site, 'PlayerImageMetadata', summary=summary).run()
# TemplateModifier(site, 'PlayerStickers', summary=summary).run()
# TemplateModifier(site, 'TeamRosterPhotoMetadata', summary=summary).run()
# TemplateModifier(site, 'MatchSchedule', summary=summary).run()
# TemplateModifier(site, 'Infobox Tournament', summary=summary).run()
# TemplateModifier(site, 'CircuitPointsLine', summary=summary).run()
# TemplateModifier(site, 'TeamRoster', summary=summary).run()
# TemplateModifier(site, 'ExternalContent/Line', summary=summary).run()
# TemplateModifier(site, 'AutoStandings', summary=summary).run()
# TemplateModifier(site, 'Team', summary=summary).run()
# TemplateModifier(site, 'StandingsLine', summary=summary).run()
TemplateModifier(site, 'TournamentGroups', summary=summary).run()

