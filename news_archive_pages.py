from mwrogue.esports_client import EsportsClient
from mwrogue.auth_credentials import AuthCredentials
from mwcleric.page_modifier import PageModifierBase

credentials = AuthCredentials(user_file="me")
site = EsportsClient('halo-esports', credentials=credentials)
summary = 'Creating news archive pages'

years = ['2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015',
         '2016', '2017', '2018']
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
          'November', 'December']

pattern = 'Halo Esports Wiki:News/'
text = '{{News Navbox}}\n{{ArchiveNews}}'

limit = -1
lmt = 0

for year in years:
    for month in months:
        if lmt == limit:
            break
        lmt += 1
        subpage = year + '/' + month
        news_page = pattern + subpage
        page = site.client.pages[news_page]
        site.save(page, text, summary=summary)
        print('Saving page %s...' % page.name)


