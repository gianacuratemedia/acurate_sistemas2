import React, { Component } from "react";
import './Course2.css';
import { Link } from "react-router-dom";
import * as BiIcons from "react-icons/bi";
import * as RiIcons from "react-icons/ri";
import imagenes from '../../assets/img/imagenes';

import {FontAwesomeIcon} from '@fortawesome/react-fontawesome';
import {faFile, faArrowAltCircleDown, faFileAlt, faPaste, faArrowAltCircleUp} from '@fortawesome/free-solid-svg-icons';


class Ejemplo3 extends Component {
  constructor() {
    super();
    this.state = { checked: false };
    this.handleChange = this.handleChange.bind(this);
  }

  handleChange(checked) {
    this.setState({ checked });
  }
  render() {
    return (
      <div>
        <div className="col-md-6  mb-2">
          <div
            className="btn-group btn-group-sm"
            role="group"
            aria-label="Basic example"
          >
            {/* Este es el boton 1 */}
            <button
              type="button"
              id="btn-nquote"
              className="button1"
              onClick={() => this.handleChange('btn1')}
            >
              Todos mis cursos
            </button>

            {/* Este es el boton 2 */}
            <button
              type="button"
              id="btn-flex"
              className="button2"
              onClick={() => this.handleChange('btn2')}
            >
             Recursos
            </button>

             {/* Este es el boton 3 */}
             <button
              type="button"
              id="btn-flex"
              className="button3"
              onClick={() => this.handleChange('btn3')}
            >
             Tareas
            </button>

          </div>
        </div>
        <span>
          {this.state.checked === 'btn1' && (
        <div /* Este es el div 1 */ className="button1" >

            <div class="seccion-course">            

              <div className="curso1">
                  <img className="videos" src= {imagenes.video}/>
                  <div className="tit-estrella"><center>Asesoria Personal</center></div>
                  <div class= "des-estrella">Impartido por Nombre Instructor</div>
              </div>


              <div className="curso2">
                  <img className="videos" src= {imagenes.video}/>
                  <div className="tit-estrella">Fundamentos de mercadotecnia</div>
                  <div class= "des-estrella">Impartido por Nombre Instructor</div>    
              </div>

              <div className="curso3">
                  <img className="videos" src= {imagenes.video}/>
                  <div className="tit-estrella">Aprende a cocinar</div>
                  <div class= "des-estrella">Impartido por Nombre Instructor</div>
              </div>
                
              <div className="curso4">
                  <img className="videos" src= {imagenes.video}/>
                  <div className="tit-estrella">Aprende a cocinar</div>
                  <div class= "des-estrella">Impartido por Nombre Instructor</div>
               </div> 
           </div>
     
      </div>
          ) }
           {this.state.checked ==='btn2' &&
           (
            <div /* Este es el div 2 */ className="red2" >

                <Link to="/UploadFiles">
                <a className='agregar'> Agregar archivo  </a>
                </Link>

            <div className='modulo1'> 
                <BiIcons.BiBookAlt onClick="#" className="icono-libro"/>
                <div className='modulo1-titulo'> Módulo 1 Audio </div>
                <div className='modulo1-subt'> Descripción </div>

                <BiIcons.BiDotsHorizontalRounded onClick="#" className="icono-puntos"/>
            
            </div>   
                </div>
          )}

          {this.state.checked ==='btn3' &&
          (
            <div /* Este es el div 3 */ className="red2">
                
                <Link to="/UploadFiles">
                <a className='agregar'>  Agregar tarea  </a>
                </Link>

            <div className='modulo1'> 
                <RiIcons.RiBookletFill onClick="#" className="icono-libro2"/>
                <div className='modulo1-titulo'> Tarea Módulo 1 </div>
                <div className='modulo1-subt'> Fecha limite de entrega </div>

                <BiIcons.BiDotsHorizontalRounded onClick="#" className="icono-puntos"/>
            
            </div>   
                </div>
          
          )}

          
        </span>


      </div>
    );
  }
}

export default Ejemplo3;