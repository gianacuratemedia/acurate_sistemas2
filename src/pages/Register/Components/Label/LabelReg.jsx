import React from 'react';

import './LabelReg.css';

const LabelReg = ({text}) =>{
    return(
        <div>
            <label className='label'>{text}</label>

        </div>
    )
};

export default LabelReg;

//Vamos a estar pasando texto y sea dinamico no se quede solo con soy un label
//{text}