// import mariadb
let mariadb = require('mariadb');

// create a new connection pool
const pool = mariadb.createPool({
    host: "localhost",
    port: 3306,
    user: "root",
    password: "root123",
    database: "datas"
});

// expose the ability to create new connections
module.exports={
    getConnection: function(){
        return new Promise(function(resolve,reject){
            pool.getConnection().then(function(connection){
                resolve(connection);
            }).catch(function(error){
                reject(error);
            });
        });
    }
}