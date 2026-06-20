content = open('extension.hbs').read()
content = content.replace(
    'var entries = {{{dataEntriesJSON}}};',
    'var entries = JSON.parse(document.getElementById("data-store").textContent);'
)
# Add data store div before the script
content = content.replace(
    '<script>',
    '<script id="data-store" type="application/json">{{{dataEntriesJSON}}}</script>\n  <script>',
    1
)
open('extension.hbs', 'w').write(content)
print('Done')
