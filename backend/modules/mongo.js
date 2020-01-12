const mongoose = require('mongoose');
const fs = require('fs');

const config = JSON.parse(fs.readFileSync('./config/config.json'));

mongoose.connect(config.mongoUri, {useNewUrlParser: true, useUnifiedTopology: true}, err => handleError(err));
user = mongoose.model('user', new mongoose.Schema({email: String, handles: Array}, {versionKey: false}));

function handleError(err) {
    if (err) console.log(err);
}

module.exports.addUser = function addUser(email) {
    user.find({email}).countDocuments(function(err, data) {
        handleError(err);
        if (data == 0) {
            new user({email}).save(err => handleError(err));
        }
    });
}

module.exports.getUser = async function getUser(email) {
    return user.find({email}, function(err, data) {
        handleError(err);
        if (data[0]) {
            return data[0];
        }
    });
}

module.exports.addHandle = function addHandle(email, handle) {
    user.updateOne({email}, {$push: {handles: handle}}, function(err, data) { 
        handleError(err);
    });
}

module.exports.removeHandle = function removeHandle(email, handle) {
    user.updateOne({email}, {$pull: {handles: handle}}, function(err, data) { 
        handleError(err);
    });
}

