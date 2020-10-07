
import React from 'react';
import './assets/css/App.css';
import './assets/css/stylesgalery.css';
import imagenes from './assets/img/imagenes';
import{FontAwesomeIcon} from '@fortawesome/react-fontawesome';
import {faSearch}from '@fortawesome/free-solid-svg-icons';


function App(){

  return (
    
    <div className="header">
      <img className="fondo" src={imagenes.img}/>
   

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

    </div>
  );
}


export default App;
