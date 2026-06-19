// src/controllers/authController.js

const User = require('../models/user');
const bcrypt = require('bcrypt');

// SIGNUP FUNCTION
async function signup(req, res) {
  console.log(req.body); // <--- Add this
  const { name, email, password } = req.body;
  try {
    let user = await User.findOne({ email: email.trim() });
    if (user) {
      return res.render('signup', { message: 'Email already registered' });
    }
    const hashedPassword = await bcrypt.hash(password, 10);
    user = await User.create({ name, email: email.trim(), password: hashedPassword });
    console.log('User created:', user); // <--- Add this
    req.session.user = { id: user._id, email: user.email, name: user.name };
    return res.redirect('/data');
  } catch (err) {
    console.error(err);
    return res.render('signup', { message: 'Signup failed' });
  }
}

// LOGIN FUNCTION
async function login(req, res) {
  const { email, password } = req.body;
  try {
    // Find user by email
    const user = await User.findOne({ email: email.trim() });
    if (!user) {
      return res.render('login', { message: 'User not found. Please check your email or sign up.' });
    }
    // Compare password
    const isMatch = await bcrypt.compare(password, user.password);
    if (!isMatch) {
      return res.render('login', { message: 'Invalid password.' });
    }
    // Set session
    req.session.user = { id: user._id, email: user.email, name: user.name };
    // Redirect to extension page after login
    return res.redirect('/extension');
  } catch (err) {
    console.error('Login error:', err);
    return res.render('login', { message: 'Login failed.' });
  }
}

// LOGOUT FUNCTION
function logout(req, res) {
  req.session.destroy(() => {
    res.redirect('/login');
  });
}

module.exports = { signup, login, logout };
