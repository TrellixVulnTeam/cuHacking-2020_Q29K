const express = require('express');
const cors = require('cors');
const fs = require('fs');
const bodyParser = require('body-parser');

const twitter = require('./twitter-api');
const mongo = require('./mongo');

const config = JSON.parse(fs.readFileSync('./config/config.json'));

module.exports.init = function init() {
    const backend = express();

    backend.use(bodyParser.json());
    backend.use(bodyParser.urlencoded({extended: true}));

    // cors
    const corsOptions = { origin: config.frontendHost, optionsSuccessStatus: 200 }
    backend.use(cors(corsOptions));

    // router configuration
    const router = express.Router();
    router.use(express.static(config.frontendDist));

    router.post('/api/add-user', function(req, res) {
        mongo.addUser(req.body.email);
    });

    router.get('/api/get-user/:email', async function(req, res) {
        const user = await mongo.getUser(req.params.email);
        res.send(user[0]);
    });

    router.post('/api/add-handle', function(req, res) {
        mongo.addHandle(req.body.email, req.body.handle);
    });

    router.post('/api/remove-handle', function(req, res) {
        mongo.removeHandle(req.body.email, req.body.handle);
    });

    router.get('/api/get-tweets/:handle-:maxId', async function(req, res) {
        const tweets = await twitter.getTweets(req.params.handle, req.params.maxId);
        res.send(tweets);
    });

    router.get('*', function(req, res) { res.sendFile(config.frontendDistHtml) });
    backend.use(router);

    return backend;
}