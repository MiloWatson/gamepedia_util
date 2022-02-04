from log_into_wiki import *

site = login('bot', 'cod-esports')  # Set wiki

limit = -1
lmt = 0
startat_page = 'Predictions:Call of Duty League/2020 Season/Launch Weekend/User/AaronJ76'
passed_startat = False if startat_page else True

pages = site.pages['Template:UserPredictions'].embeddedin()

for page in pages:
    if lmt == limit:
        break
    if startat_page and page.name == startat_page:
        passed_startat = True
    if not passed_startat:
        print("Skipping page %s" % page.name)
        continue
    lmt += 1
    print('beginning page %s' % page.name)
    text = page.text()
    print('Saving page %s...' % page.name)
    page.save(text)
