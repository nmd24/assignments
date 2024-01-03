const express = require('express');
const bodyParser = require('body-parser');
const mongoose = require('mongoose');

const app = express();

// Connect to MongoDB
mongoose.connect('mongodb+srv://nmd:ycMjDNoRxR4UNfCz@atlascluster.o5duqvq.mongodb.net/course_selling_app', { useNewUrlParser: true, useUnifiedTopology: true });

// Define schemas
const AdminSchema = new mongoose.Schema({
    username: String,
    password: String
});

const UserSchema = new mongoose.Schema({
    username: String,
    password: String
});

const CourseSchema = new mongoose.Schema({
    title: String,
    description: String,
    price: Number,
    image: String,
});

const Admin = mongoose.model('Admin', AdminSchema);
const User = mongoose.model('User', UserSchema);
const Course = mongoose.model('Course', CourseSchema);

// Middleware for parsing request bodies
app.use(bodyParser.json());

// Admin Routes
app.post('/admin/signup', (req, res) => {
    Admin.create({
        username: req.body.username,
        password: req.body.password
    });
    res.json({
        message: 'Admin created successfully'
    });
});

app.post('/admin/courses', (req, res) => {
    Course
    .create({
        title: req.body.title,
        description: req.body.description,
        price: req.body.price,
        image: req.body.image
    })
    .then(() => res.json({ message: 'Course created successfully' }))
    .catch(err => res.status(500).json({ error: err.message }));
});

app.get('/admin/courses', (req, res) => {
    Course
        .find()
        .then(courses => {
            res.json(courses);
        })
        .catch(err => res.status(500).json({ error: err.message }));
});

// User Routes
app.post('/users/signup', (req, res) => {
    User.create({
        username: req.body.username,
        password: req.body.password
    });
    res.json({
        message: 'User created successfully'
    });
});

app.get('/users/courses', (req, res) => {
    Course
        .find()
        .then(courses => {
            res.json(courses);
        })
        .catch(err => res.status(500).json({ error: err.message }));
});

app.post('/users/courses/:courseId', (req, res) => {
    // Implement logic for users to sign up for courses
});

app.get('/users/purchasedCourses', (req, res) => {
    // Implement fetching purchased courses logic
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
