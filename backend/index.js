const Express = require('./modules/express');
const express = Express.init();
express.listen(80, () => console.log('Express running on port 80'));
