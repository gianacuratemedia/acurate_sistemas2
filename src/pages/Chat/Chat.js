import imagenes from '../../assets/img/imagenes';
import React, {useState} from 'react'
import { Link } from 'react-router-dom';
import * as FaIcons from 'react-icons/fa';
import * as BsIcons from "react-icons/bs";
import * as BiIcons from "react-icons/bi";
import * as AiIcons from 'react-icons/ai';
import * as HiIcons from 'react-icons/hi';
import * as RiIcons from 'react-icons/ri';
import './Chat.css';
import { MenuDataChat } from './MenuDataChat';
// import 'bootstrap/dist/css/bootstrap.min.css';



const Chat = () => {

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



        <div className="seccion-chatsgrupos">

            <div className="grupos"> 

                <HiIcons.HiOutlineUserGroup onClick="#" className="icono-grupo"/>
                <div className="grupostitulo">Grupos </div>
            </div>

            <div className="grupos1"> 

                <RiIcons.RiGroup2Line onClick="#" className="icono-grupo"/>
                <div className="grupostitulo1">Nombre de curso </div>
                <div className="grupos_desc">Ultimo mensaje </div>
            </div>
            <div className="grupos2"> 

                <RiIcons.RiGroup2Line onClick="#" className="icono-grupo"/>
                <div className="grupostitulo1">Nombre de curso </div>
                <div className="grupos_desc">Ultimo mensaje </div>
            </div>
            <div className="grupos3"> 

                <RiIcons.RiGroup2Line onClick="#" className="icono-grupo"/>
                <div className="grupostitulo1">Nombre de curso </div>
                <div className="grupos_desc">Ultimo mensaje </div>
            </div>
            <div className="grupos4"> 

                <RiIcons.RiGroup2Line onClick="#" className="icono-grupo"/>
                <div className="grupostitulo1">Nombre de curso </div>
                <div className="grupos_desc">Ultimo mensaje </div>
            </div>
            <div className="grupos5"> 

                <RiIcons.RiGroup2Line onClick="#" className="icono-grupo"/>
                <div className="grupostitulo1">Nombre de curso </div>
                <div className="grupos_desc">Ultimo mensaje </div>
            </div>


        </div>

        <div className="seccion-chat">
        
            <div className="avanceC"> Nombre de Cursos </div><br></br><br></br>
        
        
        </div>


      <nav className={sidebar ? 'nav-menu active' : 'nav-menu'}> {/*Si presiono icono de menu se ctiva */}
            <ul className='nav-menu-items' onClick={showSidebar}>
                <li className='navbar-toggle'>
                <Link to='#' className='menu-bars'>
                    <AiIcons.AiOutlineClose/>
                </Link>
                </li>
                {MenuDataChat.map((item, index) => {
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

export default Chat;
