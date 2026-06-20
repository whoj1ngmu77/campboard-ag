content = open('extension.hbs').read()
content = content.replace(
    'var entries = {{{json dataEntries}}};',
    'var entries = {{{dataEntriesJSON}}};'
)
open('extension.hbs', 'w').write(content)
print('Done')
