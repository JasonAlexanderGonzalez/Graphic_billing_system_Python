const express = require('express');
const app = express();
const cors = require('cors');
const db = require('./database'); // Importa la configuración de la base de datos

app.use(cors());
app.use(express.json());



// Conexión a la base de datos
db.connect((err) => {
  if (err) {
    console.error('Error al conectar a la base de datos:', err);
  } else {
    console.log('Conexión a la base de datos MySQL exitosa');
  }
});



/*
app.delete("/delete/:id",(req,res) =>{
  const id = req.params.id;
  db.query('DELETE FROM empleados WHERE id = ?',id,
  (err,result) => {
    if(err){
      console.log(err);
    }else{
      res.send("Empleado eliminado con exito");
    }
  });
});
*/

// Ruta para buscar un registro por número de cuenta
app.get('/buscarCuenta/:numeroCuenta', (req, res) => {
  const numeroCuenta = req.params.numeroCuenta; // Obtener el número de cuenta de la solicitud

  // Consulta SQL para buscar el nombre de la cuenta por número de cuenta
  const sql = 'SELECT nombreCuenta FROM catalogo WHERE numeroCuenta = ?';

  // Ejecutar la consulta con el número de cuenta proporcionado
  db.query(sql, [numeroCuenta], (err, result) => {
    if (err) {
      console.error('Error al buscar la cuenta:', err);
      res.status(500).json({ error: 'Error interno del servidor' });
    } else if (result.length === 0) {
      // No se encontró ninguna cuenta con el número proporcionado
      res.status(404).json({ mensaje: 'Cuenta no encontrada' });
    } else {
      // Se encontró la cuenta, enviar el nombre de la cuenta como respuesta
      res.status(200).json({ nombreCuenta: result[0].nombreCuenta });
    }
  });
});


app.get('/obtenerCuenta/:numeroCuenta', (req, res) => {
  const numeroCuenta = req.params.numeroCuenta;
  // Aquí, realiza una consulta a tu base de datos para obtener la fila completa
  // correspondiente al número de cuenta y envía los datos como respuesta
  // Puedes utilizar una consulta SQL para obtener los datos de la tabla 'catalogo'
  // relacionados con el número de cuenta proporcionado.
  // Luego, envía los datos como un objeto JSON en la respuesta.
  // Por ejemplo:
  const query = "SELECT * FROM catalogo WHERE numeroCuenta = ?";
  db.query(query, [numeroCuenta], (err, result) => {
    if (err) {
      console.error('Error al obtener la cuenta:', err);
      res.status(500).json({ error: 'Error al obtener la cuenta' });
    } else {
      if (result.length === 0) {
        res.status(404).json({ error: 'Cuenta no encontrada' });
      } else {
        // Envía la fila de la cuenta como respuesta
        res.status(200).json(result[0]);
      }
    }
  });
});


app.post('/agregarCuenta', (req, res) => {
  const nuevaCuenta = req.body; // Obtener los datos enviados desde el componente React

  // Consulta SQL para insertar una nueva cuenta en la tabla 'asientos'
  const sql = 'INSERT INTO asientos (numeroCuenta, monto, tipoMovimiento, fechaMovimiento) VALUES (?, ?, ?, ?)';

  // Ejecutar la consulta SQL con los valores de la cuenta
  db.query(
    sql,
    [nuevaCuenta.numeroCuenta, nuevaCuenta.saldoNormal, nuevaCuenta.saldo, nuevaCuenta.fechaMovimiento],
    (err, result) => {
      if (err) {
        console.error('Error al agregar la cuenta:', err);
        res.status(500).json({ error: 'Error interno del servidor' });
      } else {
        // La cuenta se agregó con éxito, enviar una respuesta exitosa
        res.status(200).json({ mensaje: 'Cuenta agregada con éxito' });
      }
    }
  );
});


app.get('/consultarDatos', (req, res) => {
  
  // ... El resto de tu código de consulta de datos
  // Aquí realiza una consulta a tu base de datos para obtener los datos que deseas consultar
  // Puedes utilizar una consulta SQL para obtener los datos necesarios
  const query = "SELECT * FROM asientos"; // Cambia 'tuTabla' por el nombre de tu tabla
  
  db.query(query, (err, result) => {
    if (err) {
      console.error('Error al consultar datos:', err);
      res.status(500).json({ error: 'Error al consultar datos' });
    } else {
      // Envía los datos consultados como respuesta
      res.status(200).json(result);
    }
  });
});


/*
app.get("/empleados",(req,res) =>{
  db.query('SELECT * FROM empleados',
  (err,result) => {
    if(err){
      console.log(err);
    }else{
      res.send(result);
    }
  });
});
*/

app.listen(3001,()=>{
  console.log("Corriendo en el puerto 3001");
});