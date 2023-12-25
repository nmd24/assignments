const request = require('supertest');
const assert = require('assert');
const express = require('express');
const app = express();

let numberOfRequestsForUser = {};
let errorCount = 0;

setInterval(() => {
    numberOfRequestsForUser = {};
}, 1000);

// Rate limiting middleware
app.use((req, res, next) => {
    const userId = req.header('user-id');

    if (!userId) {
        return res.status(400).send('User ID is required');
    }

    if (!numberOfRequestsForUser[userId]) {
        numberOfRequestsForUser[userId] = 0;
    }

    numberOfRequestsForUser[userId]++;

    if (numberOfRequestsForUser[userId] > 5) {
        return res.status(404).send('Rate limit exceeded');
    }

    next();
});

// Error handling middleware
app.use((err, req, res, next) => {
    errorCount++;
    res.status(500).json({ error: 'Internal Server Error' });
});

app.get('/user', function(req, res) {
    // Simulate an error for testing
    if (req.query.triggerError) {
        throw new Error('Test Error');
    }
    res.status(200).json({ name: 'john' });
});

app.post('/user', function(req, res) {
    res.status(200).json({ msg: 'created dummy user' });
});

app.get('/errorCount', function(req, res) {
    res.status(200).json({ errorCount });
});

module.exports = app;
