import React from 'react';

import './Label.css';

const Label = ({text}) =>{
    return(
        <div>
            <label className='label'>{text}</label>

        </div>
    )
};

export default Label;

//Vamos a estar pasando texto y sea dinamico no se quede solo con soy un label
//{text}