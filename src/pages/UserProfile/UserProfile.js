import React, {useState} from 'react'
import * as FaIcons from 'react-icons/fa';
import * as BsIcons from "react-icons/bs";
import * as BiIcons from "react-icons/bi";
import * as AiIcons from 'react-icons/ai';
import * as TiIcons from "react-icons/ti";
import * as IoIcons from "react-icons/io";
import { Link } from 'react-router-dom';
import { MenuData } from './MenuData'
import './UserProfile.css'
import imagenes from '../../assets/img/imagenes';

function UserProfile() {
    const [sidebar, setSidebar] = useState (false); /*No mostrar barra*/

    const showSidebar = () => setSidebar (!sidebar); /*Mostrar barra*/

    return (
        <>
        <div className='navbar'>
            <Link to='#' className='menu-bars'>
            <FaIcons.FaBars onClick={showSidebar}/> {/*Icono de barras de react*/}
            </Link>

            <img className="logo" src= {imagenes.logoazul}/>

            <div className='com'> Comunidad </div>

            <div className='categorias'> Categorias </div>

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

    <div className= 'seccion-pagina'>

        <div className= 'seccion-perfil'>
            <BiIcons.BiUserCircle onClick="#" className="icon-usuario"/>

            <div className='nombre-us'> 
                Nombre de Usuario   
            </div>

            <div className='nivel-us'> 
                Nivel de Usuario <br></br>
            </div>

            <div className='desc-us'> 
            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.   
            </div>

            <div className='editar'> 
                Editar 
            </div>
            <BsIcons.BsFillGearFill onClick="#" className="icono-engrane"/>
                    
        </div> 


        <div class="seccion-insignias">   

          <div className='insignias'> 
            Insignias 
          </div> <br></br>      

            <div class="insignia1">
                <BiIcons.BiBadge onClick="#" className="icono-insignia"/>
                <div class="logro">Nombre del logro</div>
            </div>

            <div class="insignia2">
                <BiIcons.BiBadge onClick="#" className="icono-insignia2"/>
                <div class="logro">Nombre del logro</div>
            </div>

            <div class="insignia3">
                <BiIcons.BiBadge onClick="#" className="icono-insignia2"/>
                <div class="logro">Nombre del logro</div>
            </div>

            <div class="insignia4">
                <BiIcons.BiBadge onClick="#" className="icono-insignia2"/>
                <div class="logro">Nombre del logro</div>
            </div>

            <div class="insignia5">
                <BiIcons.BiBadge onClick="#" className="icono-insignia"/>
                <div class="logro">Nombre del logro</div>
            </div>

            <div class="insignia6">
                <BiIcons.BiBadge onClick="#" className="icono-insignia3"/>
                <div class="logro">Nombre del logro</div>
            </div>

          
        </div>

        <div className= 'seccion-misprofesores'>

          <div className='mis-profesores'> 
                  Mis Profesores   
          </div>

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

        <div className= 'seccion-detalles'>

            <div className='detalles-cuenta'> 
                Detalles de la cuenta   
            </div><br></br>

            <div className='nombre'><strong>Nombre:</strong> Usuario</div>
            <div className='fecha'><strong>Fecha de Nacimiento:</strong> 01/enero/2000</div>
            <div className='correo-elec'><strong>Correo Electrónico:</strong> usuario@gmail.com</div>
            <div className='tel'><strong>Teléfono:</strong> 222 222 222 </div>

            <div className='editar2'> 
                Editar 
            </div>
            <BsIcons.BsFillGearFill onClick="#" className="icono-engrane2"/>
                    
        </div>  

        <div className= 'seccion-informacion'>

            <div className='info-pago'> 
                Información de Pago   
            </div><br></br>

            <div className='membresia'><strong>Membresia:</strong> Activa</div>
            <div className='suscripcion'><strong>Suscripción:</strong> Anual</div>
            <div className='metodo'><strong>Método:</strong> PayPal </div>

            <div className='editar2'> 
                Editar 
            </div>
            <BsIcons.BsFillGearFill onClick="#" className="icono-engrane2"/>
                    
        </div>


        <div className= 'seccion-actividad'>

            <div className='actividad'> 
                Actividad   
            </div><br></br>

            <div className= 'cont-act1'>
              <BiIcons.BiCircle onClick="#" className="icono-circulo1"/>

                <div className='nombre-act'> Curso Marketing Digital </div>

                <div className='status1'> Tarea Entregada </div>
            </div><br></br>

            <div className= 'cont-act2'>
              <BiIcons.BiCircle onClick="#" className="icono-circulo2"/>

                <div className='nombre-act'> Lección 01: Cocina 101 </div>

                <div className='status2'> Continuar viendo </div>
            </div><br></br>

            <div className= 'cont-act3'>
              <BiIcons.BiCircle onClick="#" className="icono-circulo3"/>

                <div className='nombre-act'> ¡Logro Desbloqueado! </div>

                <div className='status3'> Ver insignia </div>
            </div><br></br>

            <div className= 'cont-act4'>
              <BiIcons.BiCircle onClick="#" className="icono-circulo1"/>

                <div className='nombre-act'> Curso Marketing Digital </div>

                <div className='status1'> Tarea Entregada </div>
            </div><br></br>

            <div className= 'cont-act5'>
              <BiIcons.BiCircle onClick="#" className="icono-circulo1"/>

                <div className='nombre-act'> Curso Cocina </div>

                <div className='status1'> Tarea Entregada </div>
            </div>
      
        </div> 
    </div> 

    <div class="section-footer">
        <img className="logo-footer" src={imagenes.logoazul} />
        {/*<hr class="hline2"></hr>*/}

        <div class="inc">Knowtured, Inc. 2020</div>
        <a className="ayuda" href="#">
          {" "}
          Ayuda{" "}
        </a>
        <a className="privacidad" href="#">
          {" "}
          Privacidad{" "}
        </a>
        <a className="terminos" href="#">
          {" "}
          Términos y Condiciones
        </a>

        <div className="links-1">
          <a className="sobre" href="#">
            {" "}
            Sobre nosotros{" "}
          </a>
          <a className="contacto" href="#">
            {" "}
            Contáctanos{" "}
          </a>
          <a className="asociaciones" href="#">
            {" "}
            Asociaciones{" "}
          </a>
        </div>

        <div className="links-2">
          <a className="premium" href="#">
            {" "}
            Conviértete en Premium{" "}
          </a>
          <a className="planes" href="#">
            {" "}
            Planes de pago{" "}
          </a>
          <a className="becas" href="#">
            {" "}
            Becas escolares{" "}
          </a>
        </div>

        <div className="links-3">
          <a className="enseña" href="#">
            {" "}
            Enseña en Knowtured{" "}
          </a>
          <a className="cursos" href="#">
            {" "}
            Cursos Knowtured{" "}
          </a>
          <a className="comunidad" href="#">
            {" "}
            Comunidad{" "}
          </a>
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

export default UserProfile;

