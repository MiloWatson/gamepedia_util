from log_into_wiki import *

site = login('me', 'rollerchampions-esports')  # Set wiki

limit = -1
lmt = 0

pages = site.pages['Category:Pages with script errors'].embeddedin()

for page in pages:
    if lmt == limit:
        break
    lmt += 1
    print('beginning page %s' % page.name)
    text = page.text()
    print('Saving page %s...' % page.name)
    page.save(text)