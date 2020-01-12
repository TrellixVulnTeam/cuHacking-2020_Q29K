const express = require('express');
const cors = require('cors');
const fs = require('fs');
const bodyParser = require('body-parser');

const twitter = require('./twitter-api');

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

    router.get('/api/get-tweets/:account-:maxId', async function(req, res) {
        const tweets = await twitter.getTweets(req.params.account, req.params.maxId);
        console.log(tweets);
        res.send(tweets);
    });

    router.get('*', function(req, res) { res.sendFile(config.frontendDistHtml) });
    backend.use(router);

    return backend;
}