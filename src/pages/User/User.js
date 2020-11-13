import React from 'react';
import imagenes from '../../assets/img/imagenes';

import './User.css';

const User = () => {

    
    return (
    <div className= 'usercont'>

      <div className='bienvenido'> 
          Bienvenido,   
      </div>

      <div className='nombre-usuario'> 
          Nombre de Usuario
      </div>

      <div className='cursos-populares'> 
          Cursos Populares  
      </div>
            

    </div> 
    )
};

export default User;
