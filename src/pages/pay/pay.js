import React from 'react';
import imagenes from "../../assets/img/imagenes";
import "materialize-css/dist/css/materialize.min.css";
import M from "materialize-css";
import Title from '../Login/Components/Title/Title';

function pay() {
    document.addEventListener("DOMContentLoaded", function () {
        // var elems = document.querySelectorAll(".parallax");
        // var instances = M.Parallax.init(elems);
      });

      return(
        <div>
            <div class="row">
                <Title text= 'Knowture'></Title>
                <div className="col s12 l1"></div>
                <div className="col s12 l7 ">
                    <div className="col l12 center-align">
                        <h2>Comienza 15 días gratis</h2>
                        <span>Sin compromiso. Cancela cuando quieras</span>
                    </div>
                    <div className="col l4">
                        
                    </div>

                    <div className="col l4">
                        
                    </div>

                    <div className="col l4">

                    </div>

                    <div className="col l12">
                        <h6>Paga con Paypal</h6>
                        
                    </div>
                </div>
                <div className="col s12 l4">
                <h3>Beneficios premium</h3>
                    <div className="col l1">

                    </div>
                    <div className="col l10">
                    <div className="col s12">
                    <div class="card blue-grey darken-1">
                         <div class="card-image center">
                             <i class="material-icons large">star_rate</i>
                        </div>
                            <div class="card-content white-text center-align">
                            <span class="card-title">+600 cursos en línea</span>
                                <p>Encuentra tu curso ideal y aprende habilidades nuevas en menos de 2 horas.</p>
                            </div>
                        </div>
                    </div>

                    <div className="col s12">
                    <div class="card blue-grey darken-1">
                    <div class="card-image center">
                             <i class="material-icons large">video_library</i>
                        </div>
                            <div class="card-content white-text center-align">
                            <span class="card-title">Avanza a tu propio ritmo</span>
                                <p>Disfruta de acceso exlusico a cursos en línea en tu propio horario y a tu ritmo.</p>
                            </div>
                        </div>
                    </div>

                    <div className="col s12">
                   
                        <div class="card blue-grey darken-1 ">
                        <div class="card-image center">
                             <i class="material-icons large">av_timer</i>
                        </div>
                            <div class="card-content white-text center-align">
                            <span class="card-title">Instrucción experta</span>
                                <p>Encuentra el instructor adecuado y aprende de los expertos de la industria</p>
                            </div>
                        </div>
                    </div>



                    </div>

                    <div className="col l1">

                    </div>
                </div>    
            </div>
        </div>
      );
    
}

export default pay;
