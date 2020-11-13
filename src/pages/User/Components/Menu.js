import React, {useState} from 'react'
import * as FaIcons from 'react-icons/fa';
import * as BsIcons from "react-icons/bs";
import * as BiIcons from "react-icons/bi";
import * as AiIcons from 'react-icons/ai';
import * as TiIcons from "react-icons/ti";
import * as IoIcons from "react-icons/io";
import { Link } from 'react-router-dom';
import { MenuData } from './MenuData'
import './Menu.css'
import imagenes from '../../../assets/img/imagenes';

function Menu() {
    const [sidebar, setSidebar] = useState (false); /*No mostrar barra*/

    const showSidebar = () => setSidebar (!sidebar); /*Mostrar barra*/


    return (
        <>
        <div className='navbar'>
            <Link to='#' className='menu-bars'>
            <FaIcons.FaBars onClick={showSidebar}/> {/*Icono de barras de react*/}
            </Link>

            <img className="logo" src= {imagenes.logoazul}/>

            <div className='comunidad'> Comunidad </div>

            <div className='categorias'> Categorias </div>

            {/*Busqueda */}
            <div className="barraBusqueda">
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

            <BsIcons.BsFillBellFill onClick="#" className="campana"/>
            <BiIcons.BiUserCircle onClick="#" className="icono-usuario"/>
        </div>

        <div className= 'usercont'>

            <div className='bienvenido'> 
                Bienvenido,   
            </div>

            <div className='nombre-usuario'> 
                Nombre de Usuario
            </div>

            <div className='cursos-populares'> 
                Cursos Populares  
            </div>
                    
        </div> 

        <div class="seccion-cursos">            

            <div class="cont-curso1">
                <img className="video" src= {imagenes.video}/>
                <div class="tit-estrella">Asesoria Personal</div>
                <div class= "des-estrella">Impartido por Nombre Instructor</div>
            </div>


            <div class="cont-curso2">
                <img className="video" src= {imagenes.video}/>
                <div class="tit-estrella">Fundamentos de mercadotecnia</div>
                <div class= "des-estrella">Impartido por Nombre Instructor</div>    
            </div>

            <div class="cont-curso3">
                <img className="video" src= {imagenes.video}/>
                <div class="tit-estrella">Aprende a cocinar</div>
                <div class= "des-estrella">Impartido por Nombre Instructor</div>
            </div>

            <div class="cont-curso4">
                <img className="video" src= {imagenes.video}/>
                <div class="tit-estrella">Seminario de Lenguas</div>
                <div class= "des-estrella">Impartido por Nombre Instructor</div>
            </div>

            <div class="cont-curso5">
                <img className="video" src= {imagenes.video}/>
                <div class="tit-estrella">Aprende Música</div>
                <div class= "des-estrella">Impartido por Nombre Instructor</div>
            </div>

            <div class="cont-curso6">
                <img className="video" src= {imagenes.video}/>
                <div class="tit-estrella">Total Body Yoga</div>
                <div class= "des-estrella">Impartido por Nombre Instructor</div>
            </div>
        
        </div>

        <div className='foro'> 
                Foro de discusión   
        </div>

        <div className= 'seccion-foro'>

            <div className= 'cont-foro1'>
                <TiIcons.TiMessages onClick="#" className="icono-mensajes"/>
                <div className='nombre-curso'> 
                    Nombre de Curso
                </div>

                <div className='mensaje'> 
                    Último mensaje  
                </div>

                <IoIcons.IoIosArrowDropright onClick="#" className="icono-flecha"/>
            </div>

            <div className= 'cont-foro2'>
                <TiIcons.TiMessages onClick="#" className="icono-mensajes"/>
                <div className='nombre-curso'> 
                    Nombre de Curso
                </div>

                <div className='mensaje'> 
                    Último mensaje  
                </div>

                <IoIcons.IoIosArrowDropright onClick="#" className="icono-flecha"/>
            </div>
                    
        </div> 

        <div className='profesores'> 
                Profesores Populares   
        </div>

        <div className= 'seccion-profesores'>

            <div className= 'cont-profesor1'>
                <BiIcons.BiUserCircle onClick="#" className="icono-profesor"/>
                <div className='nombre-profesor'> 
                    Nombre de Profesor
                </div>

                <div className='experto'> 
                    Experto en Finanzas  
                </div>

                <IoIcons.IoIosArrowDropright onClick="#" className="icono-flecha"/>
            </div>

            <div className= 'cont-profesor2'>
                <BiIcons.BiUserCircle onClick="#" className="icono-profesor"/>
                <div className='nombre-profesor'> 
                    Nombre de Profesor
                </div>

                <div className='experto'> 
                    Experto en Finanzas  
                </div>

                <IoIcons.IoIosArrowDropright onClick="#" className="icono-flecha"/>
            </div>

            <div className= 'cont-profesor3'>
                <BiIcons.BiUserCircle onClick="#" className="icono-profesor"/>
                <div className='nombre-profesor'> 
                    Nombre de Profesor
                </div>

                <div className='experto'> 
                    Experto en Finanzas  
                </div>

                <IoIcons.IoIosArrowDropright onClick="#" className="icono-flecha"/>
            </div>

            <div className= 'cont-profesor4'>
                <BiIcons.BiUserCircle onClick="#" className="icono-profesor"/>
                <div className='nombre-profesor'> 
                    Nombre de Profesor
                </div>

                <div className='experto'> 
                    Experto en Finanzas  
                </div>

                <IoIcons.IoIosArrowDropright onClick="#" className="icono-flecha"/>
            </div>
                    
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
                            <span>{item.title}</span> {/*Se mostrara el titulo indicado en archivo MenuData */}
                            </Link>
                        </li>
                    );
                })}
            </ul>
        </nav>
    </>
    );
}

export default Menu;
