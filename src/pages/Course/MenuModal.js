import React, { Component } from "react";
import { Link } from 'react-router-dom';
import ReactDOM from "react-dom";
import './Course.css';
import imagenes from '../../assets/img/imagenes';
import Modal from './Modal';
import Prueba from './Prueba';


import {FontAwesomeIcon} from '@fortawesome/react-fontawesome';
import {faFile, faArrowAltCircleDown, faFileAlt, faPaste, faArrowAltCircleUp} from '@fortawesome/free-solid-svg-icons';




/*----------------------------MODAL----------------------------*/


/*----------------------------------------------------------*/










class MenuModal extends Component {
  constructor() {
    super();
    this.state = { checked: false };
    this.handleChange = this.handleChange.bind(this);

   /* const [show, setShow] = useState(false);
    const closeModalHandler = () => setShow(false);
    */
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
              onClick={() => this.handleChange(false)}
            >
              Todos mis cursos
            </button>

            {/* Este es el boton 2 */}
            <button
              type="button"
              id="btn-flex"
              className="button2"
              onClick={() => this.handleChange(true)}
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

            {/* Este es el boton 4 */}
            <button
              type="button"
              id="btn-flex"
              className="button4"
              onClick={() => this.handleChange('btn4')}
            >
             Calendario
            </button>
          </div>
        </div>
        <span>
          {this.state.checked === false && (
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
           {this.state.checked ===true &&
           (
            <div /* Este es el div 2 */ className="red2" >
              
              <h4 className="title2">2 Descargas Nuevas</h4>
              <hr></hr>
                <div className="tarea1">
                <FontAwesomeIcon icon={faFile} onClick="#" className="icon-document"></FontAwesomeIcon>

              <div className="textdocument">
              Modulo 1 Audio
              </div>
                <h5 className="description">Loremp  ipsun Loremp ipsun</h5>
                <FontAwesomeIcon icon={faArrowAltCircleDown} onClick="#" className="icon-download"></FontAwesomeIcon>
            </div>
              <br></br>
            <hr></hr>
        
            <div className="tarea2">
              <FontAwesomeIcon icon={faFile} onClick="#" className="icon-document2"></FontAwesomeIcon>
                <div className="textdocument">
               Modulo 2 Audio
               </div>
               <h5 className="description">Loremp  ipsun Loremp ipsun</h5>
               <FontAwesomeIcon icon={faArrowAltCircleDown} onClick="#" className="icon-download"></FontAwesomeIcon>
        </div>    
                </div>
          )}

          {this.state.checked ==='btn3' &&
          (
            <div /* Este es el div 3 */ className="red2">
                
              
              <h4 className="title3">2 Tareas Nuevas</h4>
              <hr></hr>
                <div className="tarea1">
                <FontAwesomeIcon icon={faFileAlt} onClick="#" className="icon-task"></FontAwesomeIcon>

              <div className="textdocument">
              Modulo 1 Audio
              </div>
                <h5 className="description">Loremp  ipsun Loremp ipsun</h5>
                <FontAwesomeIcon icon={faArrowAltCircleUp} onClick="#" className="icon-upload"></FontAwesomeIcon>
            </div>
              <br></br>
            <hr></hr>
        
            <div className="tarea2">
              <FontAwesomeIcon icon={faPaste} onClick="#" className="icon-task2"></FontAwesomeIcon>
                <div className="textdocument">
               Modulo 2 Audio
               </div>
               <h5 className="description">Loremp  ipsun Loremp ipsun</h5>
               <FontAwesomeIcon icon={faArrowAltCircleUp} onClick="#" className="icon-upload"></FontAwesomeIcon>
        </div>    
                </div>
          
          )}

          {this.state.checked ==='btn4' &&
          (
            <div /* Este es el div 4 */ className="red2">
             <div>
               <hr className="barra"></hr>
             </div>

              <div className="container-calendar">
                <br></br>

                <li>
                  <a href="" className="button-horario">
                    Agregar horario
                 </a>
               </li>

              <Prueba/>
              </div>
              

              
            </div>
          )}
        </span>
        
            <div className="modalContainer">
            {/*   <h1>Este es un modal</h1> */}
                <div>
          {/*      <button onClick={() => setShow(true)} className="btn-openModal">Open Modal</button>  */}
             {/*      <Modal show={show} closeModalHandler={closeModalHandler}/> */}
                </div>
            </div>

      </div>

     
    );
  }
}

export default MenuModal;