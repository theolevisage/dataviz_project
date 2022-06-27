const express = require('express')
const pool = require('./db')
const app = express()
const port = 8080
const cors = require('cors')

app.use(cors())

app.get('/automats', async (req, res) => {
    let conn;
    try {
        // establish a connection to MariaDB
        conn = await pool.getConnection();

        // create a new query
        let query = "select tank_temp from automat LIMIT 12";

        // execute the query and set the result to a new variable
        let rows = await conn.query(query);

        delete rows['meta']
        formatted_data = []
        rows.forEach(el => {
            formatted_data.push(el.tank_temp)
        });
        console.log(formatted_data)

        // return the results
        res.send(formatted_data);
    } catch (err) {
        throw err;
    } finally {
        if (conn) return conn.release();
    }
});

app.get('/automats2', async (req, res) => {
    let conn;
    try {
        // establish a connection to MariaDB
        conn = await pool.getConnection();

        // create a new query
        let query = "select milk_weight from automat LIMIT 12";

        // execute the query and set the result to a new variable
        let rows = await conn.query(query);

        delete rows['meta']
        formatted_data = []
        rows.forEach(el => {
            formatted_data.push(el.milk_weight)
        });
        console.log(formatted_data)

        // return the results
        res.send(formatted_data);
    } catch (err) {
        throw err;
    } finally {
        if (conn) return conn.release();
    }
});

app.get('/automats3', async (req, res) => {
    let conn;
    try {
        // establish a connection to MariaDB
        conn = await pool.getConnection();

        // create a new query
        let query = "select salmonella from automat LIMIT 12";

        // execute the query and set the result to a new variable
        let rows = await conn.query(query);

        delete rows['meta']
        formatted_data = []
        rows.forEach(el => {
            formatted_data.push(el.salmonella)
        });
        console.log(formatted_data)

        // return the results
        res.send(formatted_data);
    } catch (err) {
        throw err;
    } finally {
        if (conn) return conn.release();
    }
});

app.get('/automats4', async (req, res) => {
    let conn;
    try {
        // establish a connection to MariaDB
        conn = await pool.getConnection();

        // create a new query
        let query = "select ph from automat LIMIT 12";

        // execute the query and set the result to a new variable
        let rows = await conn.query(query);

        delete rows['meta']
        formatted_data = []
        rows.forEach(el => {
            formatted_data.push(el.ph)
        });
        console.log(formatted_data)

        // return the results
        res.send(formatted_data);
    } catch (err) {
        throw err;
    } finally {
        if (conn) return conn.release();
    }
});

app.get('/automats5', async (req, res) => {
    let conn;
    try {
        // establish a connection to MariaDB
        conn = await pool.getConnection();

        // create a new query
        let query = "select kplus from automat LIMIT 12";

        // execute the query and set the result to a new variable
        let rows = await conn.query(query);

        delete rows['meta']
        formatted_data = []
        rows.forEach(el => {
            formatted_data.push(el.kplus)
        });
        console.log(formatted_data)

        // return the results
        res.send(formatted_data);
    } catch (err) {
        throw err;
    } finally {
        if (conn) return conn.release();
    }
});

app.listen(port, () => console.log(`Listening on port ${port}`));