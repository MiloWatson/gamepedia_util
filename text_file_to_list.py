unformatted = open('sync_list.txt', 'r')
lines = unformatted.readlines()
output = []
for i in lines:
    output.append(i.strip())
formatted = open('sync_list_formatted.txt', 'w')
formatted.write(str(output))
formatted.close()
