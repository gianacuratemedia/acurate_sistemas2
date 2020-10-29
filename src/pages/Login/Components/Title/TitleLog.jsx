import React from 'react';
//import Title from './components/Title/Tile.jsx';
import './TitleLog.css';

const TitleLog = ({text}) => { /*Esperamos un texto*/
    return (
        <div className= 'titlecont'>
            <label className= 'titlelabel'> {text} </label>
        </div> 
    )
};

export default TitleLog;