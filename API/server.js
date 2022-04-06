const express = require('express')
const pool = require('./db')
const app = express()
const port = 8080

app.get('/automats', async (req, res) => {
    let conn;
    try {
        // establish a connection to MariaDB
        conn = await pool.getConnection();

        // create a new query
        let query = "select * from automat";

        // execute the query and set the result to a new variable
        let rows = await conn.query(query);

        // return the results
        res.send(rows);
    } catch (err) {
        throw err;
    } finally {
        if (conn) return conn.release();
    }
});

app.listen(port, () => console.log(`Listening on port ${port}`));