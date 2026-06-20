content = open('server.js').read()
content = content.replace(
    "helpers: { json: function(context) { return JSON.stringify(context); } }",
    "helpers: { json: function(context) { var hbs = require('express-handlebars'); return JSON.stringify(context); } }"
)
# Actually just rewrite the engine line properly
import re
content = re.sub(
    r"app\.engine\('hbs'.*?\}\)\);",
    """app.engine('hbs', engine({
  extname: '.hbs',
  defaultLayout: false,
  helpers: {
    json: function(context) {
      return JSON.stringify(context);
    }
  },
  runtimeOptions: {
    allowProtoPropertiesByDefault: true,
    allowProtoMethodsByDefault: true
  }
}));""",
    content,
    flags=re.DOTALL
)
open('server.js', 'w').write(content)
print('Done')
