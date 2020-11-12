import React from 'react';

import './LabelLog.css';

const LabelLog = ({text}) =>{
    return(
        <div>
            <label className='label'>{text}</label>

        </div>
    )
};

export default LabelLog;

//Vamos a estar pasando texto y sea dinamico no se quede solo con soy un label
//{text}