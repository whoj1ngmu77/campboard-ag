const express = require('express');
const router = express.Router();
const authController = require('./authController');
const Data = require('./data');
const User = require('./user');

// Middleware to check if user is logged in
const isAuthenticated = (req, res, next) => {
  if (req.session.user) {
    return next();
  }
  res.redirect('/login');
};

// Public routes
router.get('/', (req, res) => {
  res.redirect('/login');
});

router.get('/signup', (req, res) => {
  res.render('signup', { message: null });
});

router.post('/signup', authController.signup);

router.get('/login', (req, res) => {
  res.render('login', { message: null });
});

router.post('/login', authController.login);

router.get('/logout', authController.logout);

// Protected routes

// Data entry form (after signup or via "Add New Entry")
router.get('/data', isAuthenticated, (req, res) => {
  res.render('data', { user: req.session.user, error: null });
});

// Handle data form submission
router.post('/data', isAuthenticated, async (req, res) => {
  try {
    // Collect all fields from req.body (adjust as per your form)
    const {
      name,
      age,
      mobileNumber,
      emailId,
      adharNumber,
      address,
      fathersName,
      mothersName,
      fatherMobileNumber,
      fatherEmail,
      motherMobileNumber,
      motherEmail,
      boardOfEducation,
      seniorSecondaryPercentage,
      secondaryPercentage,
      subjects // should be an array or comma-separated string
    } = req.body;
    // Validate required fields
    await Data.create({
      name,
      age,
      mobileNumber,
      emailId,
      adharNumber,
      address,
      fathersName,
      mothersName,
      fatherMobileNumber,
      fatherEmail,
      motherMobileNumber,
      motherEmail,
      boardOfEducation,
      seniorSecondaryPercentage,
      secondaryPercentage,
      subjects: typeof subjects === 'string' ? subjects.split(',').map(s => s.trim()) : (Array.isArray(subjects) ? subjects : []),
      user: req.session.user.id
    });

    res.redirect('/extension');
  } catch (error) {
    // Reload the data form with error message
    res.render('data', {
      error: 'Failed to save data',
      user: req.session.user
    });
  }
});

// Show all data entries for the user (after login)
router.get('/extension', isAuthenticated, async (req, res) => {
  try {
    const mongoose = require('mongoose');
    const dataEntries = await Data.find({ user: new mongoose.Types.ObjectId(req.session.user.id) }).lean();
    res.render('extension', {
      user: req.session.user,
      dataEntriesJSON: JSON.stringify(dataEntries),
      error: null
    });
  } catch (error) {
    console.error('Extension error:', error);
    res.render('extension', {
      user: req.session.user,
      dataEntriesJSON: '[]',
      error: 'Failed to load data'
    });
  }
});

module.exports = router;
router.get('/debug-users', async (req, res) => {
  const users = await require('./user').find({});
  res.json(users);
});
