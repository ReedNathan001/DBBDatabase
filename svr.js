require('dotenv').config();
const express = require('express');
const mysql = require('mysql');
const app = express();
const cors = require('cors');
app.use(cors());
app.get('/api/legos', (req, res) => {
    const db = mysql.createConnection({
        //host: process.env.DB_HOST,
        socketPath: '/tmp/mysql.sock',
        user: process.env.DB_USER,
        password: process.env.DB_PASS,
        database: process.env.DB_NAME,
        //port: 3306
    });

    db.connect(err => {
        if (err) {
            console.error('Error connecting to MySQL:', err);
            res.status(500).send('Server error');
            return;
        }

        db.query("SELECT * FROM ??", ['lego_parts'], (err, rows) => {
            if(err) {
                console.error('Error executing query:', err);
                res.status(500).send('Server error');
                return;
            }
            res.json(rows);
        });
    });
});
app.get('/', (req, res) => {
    res.send('Hello, world!');
});


app.listen(5000, () => {
    console.log('Server is running on port 5000');
});