const request = require('supertest');
const assert = require('assert');
const express = require('express');

const app = express();
let errorCount = 0;

app.get('/user', function(req, res, next) {
    // Simulated error
    throw new Error("User not found");
});

app.post('/user', function(req, res) {
    res.status(200).json({ msg: 'created dummy user' });
});

app.get('/errorCount', function(req, res) {
    res.status(200).json({ errorCount });
});

// Error handling middleware
app.use((err, req, res, next) => {
    errorCount++; // Increment error count
    res.status(404).json({ error: 'Not Found' });
});

module.exports = app;
