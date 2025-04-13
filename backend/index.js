//このプロジェクトはAlbertoによってさくせいされました

const express = require("express");
const app = express();
const port = 4000;
const mysql = require("mysql");
const cors = require("cors");

app.use(cors());
app.use(express.json());

const pool = mysql.createPool({
    connectionLimit: 20,
    host: "localhost",
    user: "root",
    password: "",
    database: "zoologic"
});

// Ruta para insertar un registro
app.post("/createRegister", (req, res)=> {

    const { fecha, hora } = req.body;
    const query = "INSERT INTO trabajohecho (fecha, hora) VALUES (?, ?)";
    pool.query(query, [fecha, hora], (err, result) => {
        if (err) {
            console.error("Error al insertar el registro:", err);
            return res.status(500).json({ error: "Error al insertar el registro" });
        }

        res.status(201).json({ message: "Registro insertado correctamente", id: result.insertId });
    });

})


//Ruta para obtener todos los regitros
app.get("/getRegisters", (req, res) => {
    const query = "SELECT * FROM trabajohecho";

    pool.query(query, (err, results) => {
        if (err) {
            console.error("Error al obtener los registros:", err.message);
            return res.status(500).json({ error: "Error al obtener los registros" });
        }
        res.status(200).json(results);
    });
});


// Iniciar el servidor
app.listen(port, (err) => {
    if (!err) {
        console.log(`El servidor está corriendo en http://localhost:${port}`);
    } else {
        console.error("Error al iniciar el servidor:", err);
        throw err;
    }
});