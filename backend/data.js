const mongoose = require('mongoose');

const dataSchema = new mongoose.Schema({
  name: {
    type: String,
    required: true,
    trim: true
  },
  age: {
    type: Number,
    required: true
  },
  mobileNumber: {
    type: String,
    required: true,
    trim: true
  },
  emailId: {
    type: String,
    required: true,
    trim: true
  },
  adharNumber: {
    type: String,
    required: true,
    trim: true
  },
  address: {
    type: String,
    required: true,
    trim: true
  },
  fathersName: {
    type: String,
    required: true,
    trim: true
  },
  mothersName: {
    type: String,
    required: true,
    trim: true
  },
  fatherMobileNumber: {
    type: String,
    required: true,
    trim: true
  },
  fatherEmail: {
    type: String,
    required: true,
    trim: true
  },
  motherMobileNumber: {
    type: String,
    required: true,
    trim: true
  },
  motherEmail: {
    type: String,
    required: true,
    trim: true
  },
  boardOfEducation: {
    type: String,
    required: true,
    trim: true
  },
  seniorSecondaryPercentage: {
    type: Number,
    required: true
  },
  secondaryPercentage: {
    type: Number,
    required: true
  },
  subjects: {
    type: [String],
    required: true
  },
  user: {
    type: mongoose.Schema.Types.ObjectId,
    ref: 'User',
    required: true
  },
  createdAt: {
    type: Date,
    default: Date.now
  }
});

module.exports = mongoose.model('Data', dataSchema);
