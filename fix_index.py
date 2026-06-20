content = open('index.js').read()
old = """  } catch (error) {
    console.log('dataEntries:', JSON.stringify(dataEntries, null, 2)); res.render('extension', {
      user: req.session.user,
      dataEntries: [],
      error: 'Failed to load data'
    });
  }"""
new = """  } catch (error) {
    console.error('Extension error:', error);
    res.render('extension', {
      user: req.session.user,
      dataEntriesJSON: '[]',
      error: 'Failed to load data'
    });
  }"""
content = content.replace(old, new)
open('index.js', 'w').write(content)
print('Done')
