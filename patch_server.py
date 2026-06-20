content = open('server.js').read()
old = "const { engine } = require('express-handlebars');"
new = "const { engine, ExpressHandlebars } = require('express-handlebars');\nconst Handlebars = require('handlebars');"
content = content.replace(old, new)

content = content.replace(
    "helpers: { json: function(context) { var hbs = require('express-handlebars'); return JSON.stringify(context); } }",
    "helpers: { json: function(context) { return new Handlebars.SafeString(JSON.stringify(context)); } }"
)
open('server.js', 'w').write(content)
print('Done')
