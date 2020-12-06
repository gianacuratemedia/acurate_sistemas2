import React, { useState, Component } from "react";
//import {Text} from 'react-naive';
import imagenes from "../../assets/img/imagenes";
//import {link} from "react-router";

import "./Register.css";

import Title from "./Components/Title/TitleReg";
import Label from "./Components/Label/LabelReg";
import Input from "./Components/Input/InputReg";
import { Link } from "react-router-dom";
import API from "../../services/api";
import Swal from "sweetalert2";

const Register = () => {
  //Estados
  const [user, setUser] = useState(""); //Buscar
  const [nombreUsuario, setNombreUser] = useState(""); //Buscar
  const [password, setPassword] = useState(""); //Buscar
  const [passwordError, setPasswordError] = useState(false);

  function handleChange(name, value) {
    //Si es el ingreso (en text box) de usuario tomar info, si es el de contraseña no
    if (name === "usuario") {
      setUser(value);
    }
    if (name === "nombreUsuario") {
      setNombreUser(value);
    } else {
      if (value.length < 6) {
        //Solo de tamaño seran mas de 6 caracteres
        setPasswordError(true);
      } else {
        setPasswordError(false);
        setPassword(value);
      }
    }
  }

  function handleSubmit() {
    let account = { user, password, nombreUsuario }; //Armar una variable llamada account que estara compuesto por user y password
    if (account) {
      //Aqui en base de datos
      const response = API.post(`users/register/`, {
        email: user,
        username: nombreUsuario,
        password: password,
      })
        .then(function (response) {
          console.log(response);
          Swal.fire({
            title: "Registro éxitoso!",
            text: "Se le mandara un correo para validación de usuario",
            icon: "success",
            confirmButtonText: "Continuar",
          }).then(function () {
            window.location = "/login";
          });
        })
        .catch(function (error) {
          console.log(error);
          Swal.fire({
            title:"Error!",
            text: "Reintenta por favor",
            icon: "error",
            confirmButtonText: "Reintentar",
          });
        });
      console.log("account:", account);
    }
  }

  return (
    <div className="regcont">
      <Title text="Knowture"> </Title>
      <div className="aprende"> ¡Aprende donde sea! </div>
      <div className="inscribete"> Inscribete y comienza a aprender </div>
      <br></br>

      <Label text="Nombre de usuario"> </Label>
      <div className="inputNombre">
        <Input
          attribute={{
            //Apartado usuario
            id: "nombreUsuario",
            name: "nombreUsuario",
            type: "text",
            placeholder: "Nombre de Usuario",
          }}
          handleChange={handleChange}
        ></Input>
      </div>

      <Label text="Correo electrónico"> </Label>
      <div className="inputUsuario">
        <Input
          attribute={{
            //Apartado usuario
            id: "usuario",
            name: "usuario",
            type: "text",
            placeholder: "nombreusuario@hotmail.com",
          }}
          handleChange={handleChange}
        ></Input>
      </div>

      <Label text="Contraseña"> </Label>
      <div className="inputContraseñaReg">
        <Input
          attribute={{
            //Apartado contraseña
            id: "contraseña",
            name: "contraseña",
            type: "password",
            placeholder: "Ingrese su contraseña",
          }}
          handleChange={handleChange}
          param={passwordError}
        ></Input>
      </div>

      <div className="boton-inicio-container">
        <button onClick={handleSubmit} className="boton-inicio-sesion">
          {/*<link to={"/register"}> Enlace a pagina*/}
          Registrate
          {/*</link>*/}
        </button>
      </div>

      <div className="cuenta">¿Ya tienes una cuenta?</div>
      <Link to={"/login"} className="inicia">
        Inicia Sesión
      </Link>
      <img className="registro" src={imagenes.registro} />
    </div>
  );
};

export default Register;