const jwt = require('jsonwebtoken');
const jwtPassword = 'secret';

function signJwt(username, password) {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    const passwordLengthRequirement = 6;

    if (!emailRegex.test(username) || password.length < passwordLengthRequirement) {
        return null;
    }

    const payload = { username, password };
    return jwt.sign(payload, jwtPassword);
}

function verifyJwt(token) {
    try {
        jwt.verify(token, jwtPassword);
        return true;
    } catch (e) {
        return false;
    }
}

function decodeJwt(token) {
    try {
        const decoded = jwt.decode(token);
        return !!decoded; // Return true if decoded successfully, false otherwise
    } catch (e) {
        return false;
    }
}

module.exports = {
  signJwt,
  verifyJwt,
  decodeJwt,
  jwtPassword,
};
