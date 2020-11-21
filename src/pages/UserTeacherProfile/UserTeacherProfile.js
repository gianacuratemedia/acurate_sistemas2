import React, {useState} from 'react'
import * as FaIcons from 'react-icons/fa';
import * as BsIcons from "react-icons/bs";
import * as BiIcons from "react-icons/bi";
import * as AiIcons from 'react-icons/ai';
import * as TiIcons from "react-icons/ti";
import * as IoIcons from "react-icons/io";
import {Bar} from 'react-chartjs-2';
import { Link } from 'react-router-dom';
import { MenuDataTeacher } from './MenuDataTeacherProfile'
import './MenuTeacherProfile.css'
import imagenes from '../../assets/img/imagenes';

function UserTeacherProfile() {
    const [sidebar, setSidebar] = useState (false); /*No mostrar barra*/

    const showSidebar = () => setSidebar (!sidebar); /*Mostrar barra*/

     /*Datos de la gráfica */
     const data2 = {
        labels: ['5', '4', '3', '2', '1', '0'],
        datasets:[{
            label:'Rating',
            backgroundColor: 'blue',
            hoverBackgroundColor: 'green', 
            data: [1, 2, 3, 4, 5, 6]
        }]
    }
    /*Configurar gráfica externamente*/
    const opciones2 ={
        /*Cambiar el tamaño de gráfica*/
        mainAspectRatio: false,
        responsive: true
    }

    
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

            <BsIcons.BsFillBellFill onClick="#" className="campana"/>
            <BiIcons.BiUserCircle onClick="#" className="icono-usuario"/>
        </div>



        <div className="seccion-profesor">
            <BiIcons.BiUserCircle onClick="#" className="icono-profe"/>
            <div className="nombre-prof">Nombre del Profesor</div>
            <div className="escolaridad">Escolaridad </div>

            <li>
                <a href="" className="boton-seguir">
                    Seguir
                </a>
            </li>
        </div>

        <div className="seccion-sobremi">
            
            <div className="titulos">Sobre mi</div><br></br>
            <div className="desc-sobremi">Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum</div>
        
        </div>

        <div className="seccion-cursos">
            <div className="titulos">Cursos</div><br></br>
            
            <div className="titulo-cur">Marketing Dígital</div>

            <div class="cont-cur1">
                <img className="video2" src= {imagenes.video}/>
                <div class="des-cur">Asesoria Personal</div>
                <div class= "des-cur">Impartido por Nombre Instructor</div>
            </div>

            <div class="cont-cur2">
                <img className="video2" src= {imagenes.video}/>
                <div class="des-cur">Fundamentos de mercadotecnia</div>
                <div class= "des-cur">Impartido por Nombre Instructor</div>    
            </div>

            <div class="cont-cur3">
                <img className="video2" src= {imagenes.video}/>
                <div class="des-cur">Aprende a cocinar</div>
                <div class= "des-cur">Impartido por Nombre Instructor</div>
            </div>

            <div className="titulo-cur2">Marketing Dígital</div>

            <div class="cont-cur4">
                <img className="video2" src= {imagenes.video}/>
                <div class="des-cur">Seminario de Lenguas</div>
                <div class= "des-cur">Impartido por Nombre Instructor</div>
            </div>

            <div class="cont-cur5">
                <img className="video2" src= {imagenes.video}/>
                <div class="des-cur">Aprende Música</div>
                <div class= "des-cur">Impartido por Nombre Instructor</div>
            </div>

            <div class="cont-cur6">
                <img className="video2" src= {imagenes.video}/>
                <div class="des-cur">Total Body Yoga</div>
                <div class= "des-cur">Impartido por Nombre Instructor</div>
            </div>

            <IoIcons.IoIosArrowDropright onClick="#" className="icono-flecha2"/>
            <IoIcons.IoIosArrowDropright onClick="#" className="icono-flecha3"/>

        </div>

        <div className="seccion-experiencias">
            <div className="titulos">Experiencias</div><br></br>
            
            <div className= 'cont-exp1'>
                <BiIcons.BiCircle onClick="#" className="icono-cir"/>

                <div className='nombre-exp'> Profesor de Universidad </div>
                <div className='fecha-exp'> 2020 </div>

            </div><br></br>

            <div className= 'cont-exp2'>
              <BiIcons.BiCircle onClick="#" className="icono-cir"/>

                <div className='nombre-exp'> Fundador de Organización  </div>
                <div className='fecha-exp'> 2008 - Presente </div>

            </div><br></br>

            <div className= 'cont-exp3'>
              <BiIcons.BiCircle onClick="#" className="icono-cir"/>

                <div className='nombre-exp'> Gerente en Empresa </div>
                <div className='fecha-exp'> 2000 - 2008 </div>

            </div><br></br>

            <div className= 'cont-exp4'>
              <BiIcons.BiCircle onClick="#" className="icono-cir"/>

                <div className='nombre-exp'> Maestría en Creación de Contenido </div>
                <div className='fecha-exp'> 2000 - 2002 </div>

            </div><br></br>

            <div className= 'cont-exp5'>
              <BiIcons.BiCircle onClick="#" className="icono-cir"/>

                <div className='nombre-exp'> Licenciatura en Marketing Digital </div>
                <div className='fecha-exp'> 1995 - 2000 </div>

            </div>
            
        </div>

        <div className="seccion-rating">
            <div className="titulos">Rating</div><br></br>
            
            <div className="prom-rating">4.5</div>
            <AiIcons.AiOutlineStar onClick="#" className="icono-stary"/>
            <AiIcons.AiOutlineStar onClick="#" className="icono-stary"/>
            <AiIcons.AiOutlineStar onClick="#" className="icono-stary"/>
            <AiIcons.AiOutlineStar onClick="#" className="icono-stary"/>
            <AiIcons.AiOutlineStar onClick="#" className="icono-star"/><br></br>

            <div className='nombre-rat'> Excelente </div>
            <div className='nombre-rat'> (500) </div>
            <br></br>
            <br></br>
            <div className="grafica-rating">
            <Bar data={data2} options={opciones2}/>
            </div>
            
        </div>

        <div className= 'seccion-forodis'>
            <div className="titulos">Foro de discusión</div>

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

export default UserTeacherProfile;
