import React, {useState} from 'react'
import * as FaIcons from 'react-icons/fa';
import * as BsIcons from "react-icons/bs";
import * as BiIcons from "react-icons/bi";
import * as AiIcons from 'react-icons/ai';
import { Link } from 'react-router-dom';
import { MenuDataTeacher } from './MenuDataTeacherC'
import './MenuTeacherC.css'
import imagenes from '../../assets/img/imagenes';



function UserTeacherCourses() {
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

        <div class="seccion-nomcurso" >          
            <div className='titulo2'> Nombre del Curso </div>
            <div className='titulo3'> Impartido por Nombre de Instructor </div><br></br>

            <div className='nCurso'> 
            <img className="video-sim" src= {imagenes.video}/>
            </div>
        </div>


       <div class="seccion-lista-curso" >
          <select  >
            <option value="boton-lista">Introducción</option>
            <option value="lime">Introducción: Bienvenida</option>
            <option value="coconut">Clase 1</option>
            <option value="mango">Clase 2</option>
          </select>
        </div>
        
        <div class="seccion-lista-curso2" >
          <select >
            <option value="boton-lista">Módulo 1:</option>
            <option value="lime">Introducción: Bienvenida</option>
            <option value="coconut">Clase 1</option>
            <option value="mango">Clase 2</option>
          </select>
        </div>

        <div class="seccion-lista-curso3" >
          <select  >
            <option value="boton-lista">Módulo 2:</option>
            <option value="lime">Introducción: Bienvenida</option>
            <option value="coconut">Clase 1</option>
            <option value="mango">Clase 2</option>
          </select>
        </div>

        <div class="seccion-lista-curso4" >
          <select  >
            <option value="boton-lista">Módulo 3:</option>
            <option value="lime">Introducción: Bienvenida</option>
            <option value="coconut">Clase 1</option>
            <option value="mango">Clase 2</option>
          </select>
        </div>
        <div class="seccion-lista-curso5" >
          <select  >
            <option value="boton-lista">Conclusión:</option>
            <option value="lime">Introducción: Salida</option>
            <option value="coconut">Clase 1</option>
            <option value="mango">Clase 2</option>
          </select>
        </div>
   
        

    
        <div className= 'seccion-sobre'>
            <div className='titulo2'> Sobre este Curso </div><br></br>
            <br></br>
            <div className='titulo3'> Nivel </div>
            <br></br><br></br><br></br>
            <div className='titulo3'> Duración </div>
            <br></br><br></br><br></br>
            <div className='titulo3'> Estudiantes </div>
            <br></br><br></br><br></br>
            <div className='titulo3'> Audio </div>
        </div> 

      

        <div className= 'seccion-acerca-prof'>
            <div className='titulo2'> Acerca del instructor </div><br></br>

            <BiIcons.BiUserCircle onClick="#" className="icono-profe2"/>

            <div className='nProfe'> 
                Nombre del Profesor   
            </div><br></br>

            <div className='des-profe-cursos'> Hola soy experto en Marketing
            Digital y creador de productos digitales me enecanta todo lo que tiene que ver
            con el avance de la tecnologia y como a traves de ella se mejora la calidad de vida </div>
                    
        </div> 
 

        <div className="seccion-valor">
            <div className="titulo2"> Valoración </div><br></br>

            <AiIcons.AiOutlineStar onClick="#" className="icono-sta"/>
            <AiIcons.AiOutlineStar onClick="#" className="icono-sta"/>
            <AiIcons.AiOutlineStar onClick="#" className="icono-sta"/>
            <AiIcons.AiOutlineStar onClick="#" className="icono-sta"/>
            <AiIcons.AiOutlineStar onClick="#" className="icono-sta"/><br></br>
            
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

export default UserTeacherCourses;
