const authController = require('../controllers/authController');

async function signup(req, res) {
  // ...handle signup logic...
  res.redirect('/data');
}

module.exports = {
  signup,
  login,
  logout
};

router.post('/signup', authController.signup);