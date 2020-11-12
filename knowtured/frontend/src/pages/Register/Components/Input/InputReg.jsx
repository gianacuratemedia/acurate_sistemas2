import React from 'react';

import './InputReg.css';

//Handle change manejador de eventos
const InputReg = ({attribute, handleChange, param}) => {
    return(
        <div className='input-container'>
            <input  //Para tener dos campos donde se definan de diferente manera usuario y contraseña deifinidos en Login
                id= {attribute.id}
                name= {attribute.name}   
                placeholder= {attribute.placeholder}  
                type= {attribute.type}      
                onChange= {(e) => handleChange(e.target.name, e.target.value )} 
                className={ param ? 'input-error' : 'input-style' }
                //Si el parametro es verdadero (si hay error en password) se pone el estilo de error si no el estilo regular 
                >
            </input>
        </div>
    )
};

export default InputReg;