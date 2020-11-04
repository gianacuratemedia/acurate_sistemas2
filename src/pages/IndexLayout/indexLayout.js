import React from "react";
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
              <img className="azul responsive-img" src={imagenes.img2} />
            </a>
            <ul id="nav-mobile" class="right hide-on-med-and-down">
              <li>
                <a href="#">Iniciar Sesión</a>
              </li>
              <li>
                <a href="#" className="boton-unete">
                  ¡Unete!
                </a>
              </li>
            </ul>
          </div>
        </nav>

        <div className="texto">
          <h2>
            Aprende de manera eficiente,<br></br>
            con los mejores profesores.
          </h2>
        </div>
        <p className="parrafoPrincipal">
          Somos una plataforma de contenido en<br></br>
          streaming. Nuestros programas permiten terminar<br></br>
          cursos enteros en 15 minutos en el formato que<br></br>
          prefieran con mas de 600 contenidos en áreas
        </p>

        <div>
          <a className="boton" href="#">
            ¡Unete a nosotros!
          </a>
        </div>

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

        <div class="container-avanza">
          <img className="estrella" src= {imagenes.estrellas}/>
          <div class="titulo-estrella">+600 cursos en linea</div>
          <div class= "desc-estrella">Encuentra tu curso ideal y aprende habilidades nuevas en menos de 2 horas</div>
        </div>

        <div class="container-instruccion">
            <img className="estrella" src= {imagenes.estrellas}/>
            <div class="titulo-estrella">Avanza a tu propio ritmo</div>
            <div class= "desc-estrella">Disfruta de acceso exclusivo a cursos en línea a tu propio horario y ritmo</div>
        </div>

        <div class="container-mas">
          <img className="estrella" src= {imagenes.estrellas}/>
          <div class="titulo-estrella">Instrucción Experta</div>
          <div class= "desc-estrella">Encuentra el instructor adecuado y aprende de los expertos de la industria</div>
        </div>

        </div>
      </div>



      <div class="section white2">
        <div class="row container">
          <h2 class="header center">Conoce a tus profesores</h2>

          <div className="col s4">
            <div className="item center">
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
            <div className="item center">
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
            <div className="item center">
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

        <div class="container-comparte">
          <div class="comparte">
            Comparte tu conocimiento<br></br> 
            y crea tu propio curso<br></br>
          </div>
          <div class= "desc-comparte">
            Sácale el maximo provecho a tu pasión. Crea un<br></br>
            curso para miles de personas de todo el mundo<br></br>
            y genera mas ingresos por tus conocimientos<br></br>
          </div>
        </div>

        <img className="imagen-comparte" src= {imagenes.comparte}/>

        </div>
      </div>


      <div class="section-white4">

        <div class="planes-pago">Planes de pago</div>

        <hr class="hline"></hr>

        <div class="row container">

        <div class="container-gratis">
          <div class="titulo-plan">Prueba Gratis</div>
          <div class= "desc-plan"><strong>$0.00</strong> / al mes</div>
          
          <a className="boton-conviertete" href="#">
            ¡Conviértete en Premium!
          </a>
        </div>

        <div class="container-mensual">
          <div class="titulo-plan">Prueba mensual</div>
          <div class= "desc-plan"><strong>$9.00</strong> / al mes</div>

          <a className="boton-conviertete" href="#">
            ¡Conviértete en Premium!
          </a>
        </div>

        <div class="container-anual">
          <div class="titulo-plan">Prueba anual</div>
          <div class= "desc-plan"><strong>$79.00</strong> / al mes</div>

          <a className="boton-conviertete" href="#">
            ¡Conviértete en Premium!
          </a>
        </div>

        </div>
      </div>


    </div>
  );
}

export default App;
