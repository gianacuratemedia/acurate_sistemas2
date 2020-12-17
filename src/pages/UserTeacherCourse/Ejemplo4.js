import React, { Component } from "react";
import './Course3.css';
import { Link } from "react-router-dom";
import * as BiIcons from "react-icons/bi";
import * as AiIcons from "react-icons/ai";
import imagenes from '../../assets/img/imagenes';

import {FontAwesomeIcon} from '@fortawesome/react-fontawesome';
import {faFile, faArrowAltCircleDown, faFileAlt, faPaste, faArrowAltCircleUp} from '@fortawesome/free-solid-svg-icons';


class Ejemplo4 extends Component {
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
              Sobre el curso
            </button>

            {/* Este es el boton 2 */}
            <button
              type="button"
              id="btn-flex"
              className="button2"
              onClick={() => this.handleChange('btn2')}
            >
              Comentarios
            </button>

             {/* Este es el boton 3 */}
             <button
              type="button"
              id="btn-flex"
              className="button3"
              onClick={() => this.handleChange('btn3')}
            >
             Recursos
            </button>

            {/* Este es el boton 4*/}
            <button
              type="button"
              id="btn-flex"
              className="button3"
              onClick={() => this.handleChange('btn4')}
            >
             Notas
            </button>

          </div>
        </div>
        <span>
          {this.state.checked === 'btn1' && (
        <div /* Este es el div 1 */ className="button1" >

          <div className= 'seccion-sobre'>
            <div className='titulo2'> Sobre este Curso </div>
            <br></br><br></br>
            <div className='titulo3'> Nivel </div>
            <br></br><br></br>
            <div className='titulo3'> Duración </div>
            <br></br><br></br>
            <div className='titulo3'> Estudiantes </div>
            <br></br><br></br>
            <div className='titulo3'> Audio </div>
        </div> 

        <div className= 'seccion-acerca-prof'>
            <div className='titulo2'> Acerca del instructor </div><br></br>

            <BiIcons.BiUserCircle onClick="#" className="icono-profe2"/>

            <div className='nProfe'> 
                Nombre del Profesor   
            </div><br></br>

            <div className='des-profe-cursos'> Hola soy experto en Marketing
            Digital y creador de productos digitales me enecanta todo lo que tiene que ver
            con el avance de la tecnologia y como a traves de ella se mejora la calidad de vida </div>
                    
        </div> 
 

        <div className="seccion-valor">
            <div className="titulo2"> Valoración </div><br></br>

            <AiIcons.AiOutlineStar onClick="#" className="icono-sta"/>
            <AiIcons.AiOutlineStar onClick="#" className="icono-sta"/>
            <AiIcons.AiOutlineStar onClick="#" className="icono-sta"/>
            <AiIcons.AiOutlineStar onClick="#" className="icono-sta"/>
            <AiIcons.AiOutlineStar onClick="#" className="icono-sta"/><br></br>
            
        </div>

     
      </div>
          ) }
           {this.state.checked ==='btn2' &&
           (
            <div /* Este es el div 2 */ className="red2" >

              <div className='comentarios'> 
                Comentarios  
              </div>

           
            </div>
          )}

          {this.state.checked ==='btn3' &&
          (
            <div /* Este es el div 3 */ className="red2">
                
                <div className='Recursos'> 
                Recursos  
                </div>

            </div>
          
          )}

          {this.state.checked ==='btn4' &&
          (
            <div /* Este es el div 3 */ className="red2">
                
                <div className='Comentarios'> 
                Comentarios  
                </div>

            </div>
          
          )}



          
        </span>


      </div>
    );
  }
}

export default Ejemplo4;