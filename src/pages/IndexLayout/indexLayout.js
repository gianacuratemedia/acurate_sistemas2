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
    // <div className="header">
    //   <img className="fondo" src={imagenes.img4} />

    //   <div className="boton-unete">
    //     <a className="boton-iniciar" href="">
    //       Iniciar Sesion
    //     </a>
    //     <a className="boton-unete" href="">
    //       ¡Unete!
    //     </a>
    //   </div>

    //   <img className="azul" src={imagenes.img2} />

    //   <div className="texto">
    //     <h1>
    //       Aprende de manera eficiente,<br></br>
    //       con los mejores profesores.
    //     </h1>
    //   </div>

    //   <p className="parrafoPrincipal">
    //     Somos una plataforma de contenido en<br></br>
    //     streaming. Nuestros programas permiten terminar<br></br>
    //     cursos enteros en 15 minutos en el formato que<br></br>
    //     prefieran con mas de 600 contenidos en áreas
    //   </p>

    //   <div>
    //     <a className="boton" href="">
    //       ¡Unete a nosotros!
    //     </a>
    //   </div>

    //   <div className="barraBusqueda">
    //     <FontAwesomeIcon icon={faSearch} className="icon" />
    //     <input
    //       type="text"
    //       placeholder="Encuentra cursos, certificaciones y profesores.."
    //       className="buscador"
    //     />
    //   </div>

    //   <div className="texto2">
    //     <h1>Conoce a tus profesores</h1>
    //   </div>

    //   <div className="container">
    //     <div className="item">
    //       <img className="profe1" src={imagenes.img5} />
    //       <div className="item-text">
    //         <h3>
    //           <a href="#">Nombre de Instructor</a>
    //         </h3>
    //         <div className="sub-text">
    //           <h5>Loremp ipsun</h5>
    //         </div>
    //       </div>
    //     </div>
    //     <div className="item">
    //       <img className="profe1" src={imagenes.img5} />
    //       <div className="item-text">
    //         <h3>
    //           <a href="#d">Nombre de Instructor</a>
    //         </h3>
    //         <div className="sub-text">
    //           <h5>Loremp ipsun</h5>
    //         </div>
    //       </div>
    //     </div>
    //     <div className="item">
    //       <img className="profe1" src={imagenes.img5} />
    //       <div className="item-text">
    //         <h3>
    //           <a href="fdgdf">Nombre de Instructor</a>
    //         </h3>
    //         <div className="sub-text">
    //           <h5>Loremp ipsun</h5>
    //         </div>
    //       </div>
    //     </div>
    //   </div>
    // </div>

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

      <div class="section white">
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

      <div class="parallax-container">
        <div class="parallax">
          <img src={imagenes.img4} />
        </div>
      </div>
    </div>
  );
}

export default App;
