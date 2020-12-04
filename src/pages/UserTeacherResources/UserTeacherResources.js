import React, {useState} from 'react'
import * as FaIcons from 'react-icons/fa';
import * as BsIcons from "react-icons/bs";
import * as BiIcons from "react-icons/bi";
import * as AiIcons from 'react-icons/ai';
import * as TiIcons from "react-icons/ti";
import * as IoIcons from "react-icons/io";
import {Bar} from 'react-chartjs-2';
import { Link } from 'react-router-dom';
import { MenuDataTeacher } from './MenuDataTeacher'
import './MenuTeacher.css'
import imagenes from '../../assets/img/imagenes';

function UserTeacherResources() {
    const [sidebar, setSidebar] = useState (false); /*No mostrar barra*/

    const showSidebar = () => setSidebar (!sidebar); /*Mostrar barra*/

    return (
        <>
        <div className='navbar'>
            <Link to='#' className='menu-bars'>
            <FaIcons.FaBars onClick={showSidebar}/> {/*Icono de barras de react*/}
            </Link>

            <img className="logo" src= {imagenes.logoazul}/>

            <div className='com2'> Comunidad </div>

            <div className='categorias2'> Categorias </div>

            {/*Busqueda */}
            <div className="barrabusqueda">
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

            <BsIcons.BsFillCameraVideoFill onClick="#" className="icono-video"/>
            <BsIcons.BsFillBellFill onClick="#" className="campana"/>
            <BiIcons.BiUserCircle onClick="#" className="icono-usuario"/>
        </div>

    <div className= 'mis-cursos'>

            <div className='Titulo'> 
                Mis cursos,   
            </div>

            <div className='Titulo2'> 
                Todos mis cursos   
            </div>            

            <div class="cont-curso11">
                <img className="video" src= {imagenes.video}/>
                <div class="tit-estrella">Asesoria Personal</div>
                <div class= "des-estrella">Impartido por Nombre Instructor</div>
            </div>


            <div class="cont-curso21">
                <img className="video" src= {imagenes.video}/>
                <div class="tit-estrella">Fundamentos de mercadotecnia</div>
                <div class= "des-estrella">Impartido por Nombre Instructor</div>    
            </div>

            <div class="cont-curso31">
                <img className="video" src= {imagenes.video}/>
                <div class="tit-estrella">Aprende a cocinar</div>
                <div class= "des-estrella">Impartido por Nombre Instructor</div>
            </div>
                    
    </div> 


        

        <nav className={sidebar ? 'nav-menu active' : 'nav-menu'}> {/*Si presiono icono de menu se ctiva */}
            <ul className='nav-menu-items' onClick={showSidebar}>
                <li className='navbar-toggle'>
                <Link to='#' className='menu-bars'>
                    <AiIcons.AiOutlineClose/>
                </Link>
                </li>
                {MenuDataTeacher.map((item, index) => {
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
}

export default UserTeacherResources;
