content = open('index.js').read()
content = content.replace(
    'const dataEntries = await Data.find({ user: req.session.user.id }).lean();',
    'const mongoose = require(\'mongoose\');\n    const dataEntries = await Data.find({ user: new mongoose.Types.ObjectId(req.session.user.id) }).lean();'
)
open('index.js', 'w').write(content)
print('Done')
