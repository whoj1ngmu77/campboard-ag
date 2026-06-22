require('dotenv').config();
const express = require('express');
const { engine } = require('express-handlebars');
const session = require('express-session');
const path = require('path');
const connectDB = require('./db');
const routes = require('./index');

const app = express();

connectDB();

app.engine('hbs', engine({
  extname: '.hbs',
  defaultLayout: false,
  runtimeOptions: {
    allowProtoPropertiesByDefault: true,
    allowProtoMethodsByDefault: true
  }
}));

app.set('view engine', 'hbs');
app.set('views', path.join(__dirname, '../frontend'));
app.use(express.urlencoded({ extended: true }));
app.use(express.json());
app.use(express.static(path.join(__dirname, '../frontend/public')));
app.use(session({
  secret: process.env.SECRET_KEY || 'campboard_secret',
  resave: false,
  saveUninitialized: false,
  cookie: { maxAge: 1000 * 60 * 60 * 24 }
}));
app.use('/', routes);
const PORT = process.env.PORT || 3001;
app.listen(PORT, () => {
  console.log(`CAMPUShelp running on http://localhost:${PORT}`);
});
