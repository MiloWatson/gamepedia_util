from mwrogue.esports_client import EsportsClient
from mwrogue.auth_credentials import AuthCredentials
from mwcleric.page_modifier import PageModifierBase

credentials = AuthCredentials(user_file="me")
site = EsportsClient('cod-esports', credentials=credentials)
summary = 'Fixing old player page end'


class PageModifier(PageModifierBase):
    def update_plaintext(self, text):
        text = text.replace('<gallery>\n</gallery>\n\n== External Links ==\n\n== Redirects ==\n{{PlayerPageRedirects}}'
                            '\n== References ==\n<references />', '{{PlayerProfileGallery}}\n{{PlayerPageEnd}}')
        return text


# PageModifier(site, page_list=site.pages_using('TournamentResults'), summary=summary).run()

# PageModifier(site, page_list=site.pages_using('RosterChangeData/Line'), summary=summary).run()

PageModifier(site, page_list=site.pages_using('PlayerPageRedirects'), summary=summary).run()
