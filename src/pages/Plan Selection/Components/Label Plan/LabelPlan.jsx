import React from 'react';

import './LabelPlan.css';

const LabelPlan = ({text}) =>{
    return(
        <div>
            <label className='label'>{text}</label>

        </div>
    )
};

export default LabelPlan;

//Vamos a estar pasando texto y sea dinamico no se quede solo con soy un label
//{text}