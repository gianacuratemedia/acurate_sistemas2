import React from "react";
import { Link } from "react-router-dom";
import "../../assets/css/indexLayout.css";
import "../../assets/css/stylesprofesores.css";

import imagenes from "../../assets/img/imagenes";
import "materialize-css/dist/css/materialize.min.css";
import M from "materialize-css";

// import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
// import { faSearch } from "@fortawesome/free-solid-svg-icons";

function App() {
  document.addEventListener("DOMContentLoaded", function () {
    var elems = document.querySelectorAll(".parallax");
    var instances = M.Parallax.init(elems);
  });
  return (
    <div>
      <div class="parallax-container">
        <div class="parallax">
          <img src={imagenes.img4} />
        </div>
        <nav className="transparent z-depth-0">
          <div class="nav-wrapper">
            <a href="#" class="brand-logo">
              <img className="azul responsive-img" src={imagenes.logoazul} />
            </a>
            <ul id="nav-mobile" class="right hide-on-med-and-down">
              <li>
                <Link to="/login">
                  <a class="boton-iniciar">Iniciar Sesión</a>
                </Link>
              </li>
              <li>
                <Link to="/register">
                  <a className="boton-unete">¡Unete a nosotros!</a>
                </Link>
              </li>
            </ul>
          </div>
        </nav>

        <form>
          <div className="barraBusqueda">
            <label class="label-icon" for="search">
              <i class="material-icons">search</i>
            </label>
            <input
              id="search"
              type="search"
              placeholder="Encuentra cursos, certificaciones y profesores.."
              required
            />
          </div>
        </form>
      </div>

      <div class="section-white1">
        <div class="row container">
          <div className="col s12 center">
            <div className="texto">
              Aprende de manera eficiente,<br></br>
              con los mejores profesores.
            </div>
            <p className="parrafoPrincipal">
              Somos una plataforma de contenido en
              streaming. Nuestros programas permiten<br></br> terminar
              cursos enteros en 15 minutos en el formato que
              prefieran con mas de 600<br></br> contenidos en áreas
            </p>
          </div>
          <div class="container-avanza center col s12 l4">
            <img className="estrella" src={imagenes.estrellas} />
            <div class="titulo-estrella">+600 cursos en linea</div>
            <div class="desc-estrella">
              Encuentra tu curso ideal y aprende habilidades nuevas en menos de
              2 horas
            </div>
          </div>

          <div class="container-instruccion center s12 col l4">
            <img className="estrella" src={imagenes.estrellas} />
            <div class="titulo-estrella">Avanza a tu propio ritmo</div>
            <div class="desc-estrella">
              Disfruta de acceso exclusivo a cursos en línea a tu propio horario
              y ritmo
            </div>
          </div>

          <div class="container-mas center col s12 l4">
            <img className="estrella" src={imagenes.estrellas} />
            <div class="titulo-estrella">Instrucción Experta</div>
            <div class="desc-estrella">
              Encuentra el instructor adecuado y aprende de los expertos de la
              industria
            </div>
          </div>
        </div>
      </div>

      <div class="section white2">
        <div class="row container">
          <div class="header-center col s12 center">
            Conoce a tus profesores
          </div>

          <div className="col s4">
            <div className=" center">
              <img className="profe1" src={imagenes.img5} />
              <div className="item-text">
                <h3>
                  <a href="#">Nombre de Instructor</a>
                </h3>
                <div className="sub-text">
                  <h5>Loremp ipsun</h5>
                </div>
              </div>
            </div>
          </div>

          <div className="col s4">
            <div className=" center">
              <img className="profe1" src={imagenes.img5} />
              <div className="item-text">
                <h3>
                  <a href="#">Nombre de Instructor</a>
                </h3>
                <div className="sub-text">
                  <h5>Loremp ipsun</h5>
                </div>
              </div>
            </div>
          </div>

          <div className="col s4">
            <div className=" center">
              <img className="profe1" src={imagenes.img5} />
              <div className="item-text">
                <h3>
                  <a href="#">Nombre de Instructor</a>
                </h3>
                <div className="sub-text">
                  <h5>Loremp ipsun</h5>
                </div>
              </div>
            </div>
          </div>
       
        </div>
      </div>

      <div class="section-white3">
        <div class="row container">
          <div className="col s6">
            <div class="container-comparte center">
              <div class="comparte">
                Comparte tu conocimiento<br></br>y crea tu propio curso<br></br>
              </div>
              <div class="desc-comparte">
                Sácale el maximo provecho a tu pasión. Crea un<br></br>
                curso para miles de personas de todo el mundo<br></br>y genera
                mas ingresos por tus conocimientos<br></br>
              </div>
            </div>
          </div>

          <div className="col s6">
            <img
              className="imagen-comparte responsive-img"
              src={imagenes.comparte}
            />
          </div>
        </div>
      </div>

      <div class="section-white4">
        <div class="row container">
          <div class="planes-pago col s12 center">
            Planes de pago
            <div class="divider   "></div>
          </div>
          <div className="col l4 center">
            <div class="container-gratis">
              <div class="titulo-plan">Prueba gratis</div>
              <div class="desc-plan">
                <strong>$0.00</strong> / al mes
              </div>

              <a className="boton-conviertete" href="#">
                ¡Conviértete en Premium!
              </a>
            </div>
          </div>

          <div className="col l4 center">
            <div class="container-mensual">
              <div class="titulo-plan">Prueba mensual</div>
              <div class="desc-plan">
                <strong>$9.00</strong> / al mes
              </div>

              <a className="boton-conviertete" href="#">
                ¡Conviértete en Premium!
              </a>
            </div>
          </div>

          <div className="col l4 center">
            <div class="container-anual">
              <div class="titulo-plan">Prueba anual</div>
              <div class="desc-plan">
                <strong>$79.00</strong> / al mes
              </div>

              <a className="boton-conviertete" href="#">
                ¡Conviértete en Premium!
              </a>
            </div>
          </div>
        </div>
      </div>

      <div class="section-footer">
        <img className="logo-footer" src={imagenes.logoazul} />
        {/*<hr class="hline2"></hr>*/}

        <div class="inc">Knowtured, Inc. 2020</div>
        <a className="ayuda" href="#">
          {" "}
          Ayuda{" "}
        </a>
        <a className="privacidad" href="#">
          {" "}
          Privacidad{" "}
        </a>
        <a className="terminos" href="#">
          {" "}
          Términos y Condiciones
        </a>

        <div className="links-1">
          <a className="sobre" href="#">
            {" "}
            Sobre nosotros{" "}
          </a>
          <a className="contacto" href="#">
            {" "}
            Contáctanos{" "}
          </a>
          <a className="asociaciones" href="#">
            {" "}
            Asociaciones{" "}
          </a>
        </div>

        <div className="links-2">
          <a className="premium" href="#">
            {" "}
            Conviértete en Premium{" "}
          </a>
          <a className="planes" href="#">
            {" "}
            Planes de pago{" "}
          </a>
          <a className="becas" href="#">
            {" "}
            Becas escolares{" "}
          </a>
        </div>

        <div className="links-3">
          <a className="enseña" href="#">
            {" "}
            Enseña en Knowtured{" "}
          </a>
          <a className="cursos" href="#">
            {" "}
            Cursos Knowtured{" "}
          </a>
          <a className="comunidad" href="#">
            {" "}
            Comunidad{" "}
          </a>
        </div>
      </div>
    </div>
  );
}

export default App;
