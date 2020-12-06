import React, { useState } from "react";

import imagenes from "../../assets/img/imagenes";

import "./Category.css";

function handleSummit() {}

const Categorias = () => {
  return (
    <div className="catcont">
      <img className="fondo" src={imagenes["logoazul2"]} />

      <div className="title">
        <h5 className="titlewhite">Selecciona</h5>
        <h5 className="titleblue">3 Categorias</h5>
      </div>

      <div className="contenedor">
        <div className="item">
          <a href="#Example">
            <img className="icon" src={imagenes["imgpersonal"]} />
          </a>
        </div>

        <div className="item">
          <a href="">
            <img className="icon" src={imagenes["imgpersonal"]} />
          </a>
        </div>

        <div className="item">
          <img
            onClick={handleSummit}
            className="icon"
            src={imagenes["imgpersonal"]}
          />
        </div>

        <div className="item">
          <img className="icon" src={imagenes["imgpersonal"]} />
        </div>

        <div className="item">
          <img className="icon" src={imagenes["imgpersonal"]} />
        </div>

        <div className="item">
          <img className="icon" src={imagenes["imgpersonal"]} />
        </div>

        <div className="item">
          <img className="icon" src={imagenes["imgpersonal"]} />
        </div>

        <div className="item">
          <img className="icon" src={imagenes["imgpersonal"]} />
        </div>

        <div className="item">
          <img className="icon" src={imagenes["imgpersonal"]} />
        </div>

        <div className="item">
          <img className="icon" src={imagenes["imgpersonal"]} />
        </div>

        <div className="item">
          <img className="icon" src={imagenes["imgpersonal"]} />
        </div>

        <div className="item">
          <img className="icon" src={imagenes["imgpersonal"]} />
        </div>
      </div>

      <li>
        <a href="" className="button-saltar">
          Saltar
        </a>
      </li>

      <li>
        <a href="" className="button-comenzar">
          ¡Comencemos!
        </a>
      </li>
    </div>
  );
};

export default Categorias;
