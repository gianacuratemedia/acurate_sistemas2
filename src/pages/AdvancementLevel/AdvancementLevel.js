import imagenes from '../../assets/img/imagenes';
import React, {useState} from 'react'
import { Link } from 'react-router-dom';
import * as FaIcons from 'react-icons/fa';
import * as BsIcons from "react-icons/bs";
import * as BiIcons from "react-icons/bi";
import * as AiIcons from 'react-icons/ai';
import './AdvancementLevel.css';
import { MenuData } from './MenuData';
//import '../Chat/node_modules/bootstrap/dist/css/bootstrap.min.css';



const AdvancementLevel = (props) => {

    const [sidebar, setSidebar] = useState (false); /*No mostrar barra*/

    const showSidebar = () => setSidebar (!sidebar); /*Mostrar barra*/



    return (
        <>
        <div className='navbar'>
            <Link to='#' className='menu-bars'>
            <FaIcons.FaBars onClick={showSidebar}/> {/*Icono de barras de react*/}
            </Link>

            <img className="logo1" src= {imagenes.logoazul}/>

            <div className='com1'> Comunidad </div>

            <div className='categorias21'> Categorias </div>

            {/*Busqueda */}
            <div className="barrabusqueda1">
                <label class="label-icon" for="search">
                    <i class="material-icons">search</i>
                </label>
                    <input
                    id="search"
                    type="search"
                    placeholder="Encuentra cursos, certificaciones y profesores.."
                    required
                    />
            </div>

            <BsIcons.BsFillCameraVideoFill onClick="#" className="icono-video1"/>
            <BsIcons.BsFillBellFill onClick="#" className="campana1"/>
            <BiIcons.BiUserCircle onClick="#" className="icono-usuario1"/>
        </div>


      <div className="avance-cursos">
        
        <div className="avanceC"> Avance de Cursos </div><br></br><br></br>

        <div className="nom-cursos">Nombre de Curso </div><br></br>
        
        
        <div className="contenedorProgressBar">
            <div className="progress">
                <div className="progress-bar progress-bar-striped bg-danger progress-bar-animated"
                role="progressbar"
                style={{width: props.porcentaje ? props.porcentaje +"%": "80%"}}>
                </div>
            </div>
            
        </div>


        <div className="de">Avance 32/40 estudiantes</div><br></br><br></br>

        <div className="nom-cursos">Nombre de Curso </div><br></br>
        <div className="progress">
                <div className="progress-bar progress-bar-striped bg-danger progress-bar-animated"
                role="progressbar"
                style={{color: "yellow", width: props.porcentaje ? props.porcentaje +"%": "60%"}}>
                </div>
            </div>
        <div className="de">Avance 24/40 estudiantes</div><br></br><br></br>

        <div className="nom-cursos">Nombre de Curso </div><br></br>
        <div className="progress">
                <div className="progress-bar progress-bar-striped bg-danger progress-bar-animated"
                role="progressbar"
                style={{width: props.porcentaje ? props.porcentaje +"%": "40%"}}>
                </div>
            </div>
        <div className="de">Avance 16/40 estudiantes</div><br></br><br></br>
      </div>


      <nav className={sidebar ? 'nav-menu active' : 'nav-menu'}> {/*Si presiono icono de menu se ctiva */}
            <ul className='nav-menu-items' onClick={showSidebar}>
                <li className='navbar-toggle'>
                <Link to='#' className='menu-bars'>
                    <AiIcons.AiOutlineClose/>
                </Link>
                </li>
                {MenuData.map((item, index) => {
                    return(
                        <li key= {index} className={item.cName}> {/*Cuando se seleccione delarchivo menu data se pasara a la direccion que se tiene en path */}
                            <Link to={item.path}>
                            <span>{item.title}</span> {/*Se mostrara el titulo indicado en archivo MenuDataTeacher */}
                            </Link>
                        </li>
                    );
                })}
            </ul>
        </nav>

      </>
    );
};

export default AdvancementLevel;
