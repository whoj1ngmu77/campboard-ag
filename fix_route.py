content = open('index.js').read()
content = content.replace(
    "console.log('dataEntries:', JSON.stringify(dataEntries, null, 2)); res.render('extension', {\n      user: req.session.user,\n      dataEntries,\n      error: null\n    });",
    "res.render('extension', {\n      user: req.session.user,\n      dataEntriesJSON: JSON.stringify(dataEntries),\n      error: null\n    });"
)
open('index.js', 'w').write(content)
print('Done')
