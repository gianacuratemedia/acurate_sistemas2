import React, { useState } from "react";

import "./Login.css";

import Title from "./Components/Title/TitleLog";
import Label from "./Components/Label/LabelLog";
import Input from "./Components/Input/InputLog";
import { Link } from "react-router-dom";

import API from "../../services/api";
import Swal from "sweetalert2";

const Login = () => {
  //Estados
  const [user, setUser] = useState("");
  const [password, setPassword] = useState("");
  const [passwordError, setPasswordError] = useState(false);

  function handleChange(name, value) {
    //Si es el ingreso (en text box) de usuario tomar info, si es el de contraseña no
    if (name === "usuario") {
      setUser(value);
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
    let account = { user, password }; //Armar una variable llamada account que estara compuesto por user y password
    if (account) {
      //Aqui en base de datos
      const response = API.post(`users/login/`, {
        email: user,
        password: password,
      })
        .then(function (response) {
          console.log(response);
          Swal.fire({
            title: "Login Success!",
            text: "Welcome!",
            icon: "success",
            timer: 1200,
            showCancelButton: false,
            showConfirmButton: false,
          }).then(function () {
            localStorage.setItem("token", response.data.tokens.access);
            localStorage.setItem("username", response.data.username);
            localStorage.setItem("email", response.data.email);
            window.location = "/User";
          });
        })
        .catch(function (error) {
          console.log(error);
          Swal.fire({
            title: "Error!",
            text: "Reintenta por favor",
            icon: "error",
            confirmButtonText: "Reintentar",
          });
        });
      console.log("account:", account);
    }
  }

  return (
    <div className="">
      <div className="row ">
        <div className="col s12 l4"></div>
        <div className="col s12 l4">
          <div className="logincont">
            <div className="titulo">
              <Title text="Knowture"> </Title>
            </div>

            <div className="labelCorreo">
              <Label text="Correo Electrónico"> </Label>
            </div>
            <div className="inputCorreo">
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

            <div className="labelContraseña">
              <Label text="Contraseña"> </Label>
            </div>
            <div className="inputContraseña">
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

            <div className="boton-iniciaSesion-container">
              <button onClick={handleSubmit} className="boton-inicia-sesion">
                {/*<link to={"/register"}> Enlace a pagina*/}
                Inicia Sesión
                {/*</link>*/}
              </button>
            </div>
            <Link to={"/RecuperarPassword"} className="olvide">
              ¿Olvidaste tu Contraseña?
            </Link>

            <div className="cuentaLog">¿No tienes una cuenta?</div>
            <Link to={"/register"} className="registrate">
              Regístrate
            </Link>
          </div>
        </div>
        <div className="col s12 l4"></div>
      </div>
    </div>
  );
};

export default Login;
