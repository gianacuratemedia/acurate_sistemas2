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

function UserTeacher() {
    const [sidebar, setSidebar] = useState (false); /*No mostrar barra*/

    const showSidebar = () => setSidebar (!sidebar); /*Mostrar barra*/

    /*Datos de la gráfica */
    const data = {
        labels: ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'],
        datasets:[{
            label:'Rendimiento de Alumnos',
            backgroundColor: 'blue',
            hoverBackgroundColor: 'green', 
            data: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        }]
    }
    /*Configurar gráfica externamente*/
    const opciones ={
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

            <BsIcons.BsFillCameraVideoFill onClick="#" className="icono-video"/>
            <BsIcons.BsFillBellFill onClick="#" className="campana"/>
            <BiIcons.BiUserCircle onClick="#" className="icono-usuario"/>
        </div>

        <div className= 'usercont'>

            <div className='bienvenido'> 
                Bienvenido,   
            </div>

            <div className='nombre-instructor'> 
                Nombre de Instructor
            </div><br></br>
                    
        </div> 


        <div class="seccion-grafica" >          
            <div className='rendimiento'> Rendimiento de alumnos </div><br></br> 
            <div className="grafica" style= {{width: '800px', height:'550px'}}>
            <Bar data={data} options={opciones}/>
            </div>
        </div>

        <div className='foro2'> 
            Foro de discusión   
        </div>
    
        <div className= 'seccion-foro2'>
            

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
                    Último mensaje  2
                </div>

                <IoIcons.IoIosArrowDropright onClick="#" className="icono-flecha"/>
            </div>
                    
        </div> 

        

        <div className= 'seccion-estadisticas'>
            <div className='estadisticas'> 
                Estadísticas   
            </div><br></br>

            <div className='vistas'> Vistas en total  </div>
            <div className='num-vistas'> 308k  </div><br></br>

            <div className='vistas'> Curso más popular  </div>
            <div className='num-vistas2'> 20k visitas  </div>
            <div className='curso-popular'> Marketing  </div>
            
                    
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

export default UserTeacher;
