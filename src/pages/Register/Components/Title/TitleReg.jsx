import React from 'react';
//import Title from './components/Title/Tile.jsx';
import './TitleReg.css';

const TitleReg = ({text}) => { /*Esperamos un texto*/
    return (
        <div className= 'titlecont'>
            <label className= 'titlelabel'> {text} </label>
        </div> 
    )
};

export default TitleReg;