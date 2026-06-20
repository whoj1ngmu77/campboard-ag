content = open('server.js').read()
content = content.replace("const Handlebars = require('handlebars');\n", "")
content = content.replace(
    """  helpers: {
    json: function(context) {
      return new Handlebars.SafeString(JSON.stringify(context));
    }
  }""",
    ""
)
open('server.js', 'w').write(content)
print('Done')
