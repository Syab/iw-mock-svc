const cors = require('cors');
const express = require('express');
const bodyParser = require('body-parser');
const{PORT} = require('./services/config');
// const task = require('./tasks');

const app = express();

app.use(cors());
app.use((req, res, next) => {
    res.header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS, PUT, PATCH, DELETE' );
    res.header('Access-Control-Allow-Origin', '*');
    res.header('AAccess-Control-Allow-Headers', 'Origin, X-Requested-With, Content-Type, Accept, filename');
    next()
    ;});

app.use(bodyParser.text());
app.use(bodyParser.json());
app.use(express.static('.'))
app.use(bodyParser.urlencoded({extended: true,}));

app.get('/', (req, res) => {
    res.json('Root OK!');
});

app.get('/health', (req, res) => {
    res.json({
        "msg": "Health Ok!",
        "environmentvars": process.env.HEALTH
    });
});