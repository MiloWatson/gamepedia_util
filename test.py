from log_into_wiki import *
import mwparserfromhell as mwp

site = login('me', 'cod-esports')  # Set wiki

page = site.pages['User:Ispoonz/TemplateTester']

text = page.text()
wikitext = mwp.parse(text)
for template in wikitext.filter_templates(recursive=False):
    print(template.get('prize').value.strip().upper())
