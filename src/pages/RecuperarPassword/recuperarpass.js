import React, { useState } from "react";
import imagenes from "../../assets/img/imagenes";
import "materialize-css/dist/css/materialize.min.css";
import M from "materialize-css";
import API from "../../services/api";
import Swal from "sweetalert2";

const PasswordRcueperar = () => {
  const [user, setUser] = useState("");
  document.addEventListener("DOMContentLoaded", function () {
    // var elems = document.querySelectorAll(".parallax");
    // var instances = M.Parallax.init(elems);


  });

  function submit() {
    console.log(user);
  }

  function handleSubmit() {
    if (user) {
      //Aqui en base de datos
      const response = API.post(`users/request-reset-email/`, {
        email: user,
      })
        .then(function (response) {
          console.log(response);
          Swal.fire({
            title: "Cambio de contraseña!",
            text: response.data.success,
            icon: "success",
            showConfirmButton: true,
          }).then(function () {
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
    }
  }

  return (
    <div>
      <div class="row card-panel">
        <h4 class="card-title">Actividad 1</h4>
        <h6 class="card-title">
          <b>Recuperar Contraseña</b> <br></br> Insertar email
        </h6>
        <div class="input-field col s12">
          <div class="card-panel">
            <div class="input-field col s6">
              <input placeholder="Placeholder" id="first_name" type="email" class="validate" 
              onChange={(e) => {
              setUser(e.target.value);
            }}/>
              <label for="first_name">Email</label>
            </div>
          </div>
        </div>

        <button class="btn" type="submit" onClick={handleSubmit}>
          Enviar
        </button>
      </div>
    </div>
  );
}

export default PasswordRcueperar;
