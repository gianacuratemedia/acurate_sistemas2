
import React from 'react';
import './assets/css/App.css';
import './assets/css/stylesprofesores.css';
import imagenes from './assets/img/imagenes';
import{FontAwesomeIcon} from '@fortawesome/react-fontawesome';
import {faSearch}from '@fortawesome/free-solid-svg-icons';


function App(){

  return (
    
    <div className="header">
      <img className="fondo" src={imagenes.img4}/>
   

    <div className="boton-unete">
      <a className="boton-iniciar" href="">Iniciar Sesion</a>
       <a className="boton-unete" href="">¡Unete!</a>
      
      </div>     
      
      
     
  <img className="azul" src={imagenes.img2} />
   
    <div className="texto">
    <h1>Aprende de manera eficiente,<br></br>
    con los mejores profesores.</h1>
    </div>
    
  <p className="parrafoPrincipal">
    Somos una plataforma de contenido en<br></br>
    streaming. Nuestros programas permiten terminar<br></br>
    cursos enteros en 15 minutos en el formato que<br></br>
    prefieran con mas de 600 contenidos en áreas
  </p>

<div>
<a className="boton" href="">¡Unete a nosotros!</a>
</div>


    
  <div className="barraBusqueda">
  <FontAwesomeIcon icon={faSearch} className="icon"/>
           <input 
           type="text" 
             placeholder="Encuentra cursos, certificaciones y profesores.."
              className="buscador"/>
        
        
    </div>


<div className="texto2">
<h1>Conoce a tus profesores</h1>

</div>

    <div className="container">
  
        <div className="item">
          <img className="profe1" src={imagenes.img5}/>
            <div className="item-text">
              <h3><a href="dfgdfg">Nombre de Instructor</a></h3>
                <div className="sub-text">
                 <h5>Loremp ipsun</h5>
                </div>
            </div>
        </div>
        <div className="item">
          <img className="profe1" src={imagenes.img5}/>
            <div className="item-text">
              <h3><a href="dfgdfgd">Nombre de Instructor</a></h3>
              <div className="sub-text">
                 <h5>Loremp ipsun</h5>
                </div>
            </div>
        </div>
        <div className="item">
          <img className="profe1" src={imagenes.img5}/>
            <div className="item-text">
              <h3><a href="fdgdf">Nombre de Instructor</a></h3>
              <div className="sub-text">
                 <h5>Loremp ipsun</h5>
                </div>
            </div>
        </div>
    </div>


    </div>



  );
}


export default App;
