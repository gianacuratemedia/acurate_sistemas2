import React, {useState} from 'react';
import * as FaIcons from 'react-icons/fa';
import * as BsIcons from "react-icons/bs";
import * as BiIcons from "react-icons/bi";
import * as AiIcons from 'react-icons/ai';
import * as TiIcons from "react-icons/ti";
import * as IoIcons from "react-icons/io";
import { Link } from 'react-router-dom';
import ReactDOM from "react-dom";
import { MenuData } from './MenuData';
import './Course.css';
import imagenes from '../../assets/img/imagenes';

import {FontAwesomeIcon} from '@fortawesome/react-fontawesome';
import {faFile, faArrowAltCircleDown} from '@fortawesome/free-solid-svg-icons';
// import MenuModal from "./MenuModal";

/*--------------------------------------------------------*/




/****------------------------NUEVO COMPONENT CON HOOKS--------------- */






/* class HelloWorld extends React.Component{

  state={
    show: true
  }
  render(){
     if (this.state.show) {
        return(
           <div id="title1">
              <h3>{this.props.subtitle}</h3>
               {this.props.mytext}
               <div class="curso1">
                   <img className="video" src= {imagenes.video}/>
                   <div class="tit-estrella">Asesoria de imagen personal</div>
                   <div class= "des-estrella">Impartido por Nombre Instructor</div>
                 </div>

           </div>
       )
     } else{
       return <h1>There are not elements</h1>
     }
  }
} */



function Course() {
    const [sidebar, setSidebar] = useState (false); /*No mostrar barra*/
    const [show, setShow] = useState(true);

    
    const showSidebar = () => setSidebar (!sidebar); /*Mostrar barra*/
    const[open, setOpen] = useState(false);
   

   
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



           
    
           {/*   <button onClick={()=> this.setState({show: false})}>Mis Cursos</button>
             <button>Mis Cursos</button>
             <button>Mis Cursos</button> */}
          <div>
            
          {/* <Collapsible label="Mis cursos">
              <h1>This is the Collapsible</h1>

              <p>
                Loremp ipsum oisankjash jhasasjhk jhagjsahg jhasjhsa
                kjashgkjagh kjhashgjash kjsahbkjas jhasgjd mgjashas 
                hjasgjha jhgas sakjhkjas kjhaskjhas   kgjhg jhgjhfh
                jhgjhf jhvjhvjh hbnbvnv nbvnbv nbvnbv nbvnbvnb  nbvnbv
                kjxshkjas kjsahaksja lkejroituer kahaukuqq ewqkuwe deue
                askhakeye t,kanhkakbr kjashaskjhsjs kjashaskj kjhsahasj 
                kahsakjhweruye wekuewiuwe kuwehiwe yeewuhern jhgwe
                wqkuuhqwuyqwtra lkeh jhwegjhweg jhewgjyg jhwegjygwe while  
              </p>

              <p>
                jhsgjas jhbgsajhas jhsagjhas jhreguyer jeryuer jhreguyerk
                kerjgker kjerh jhger khier uhgieugre kjherkhre kjhireuher kjerh
                kregkje kjerhr kjerhk kjre merkjbr jjb krebkrejkjerber
                kjerhkjhrejeru jhrjre jhr rekjhbre kerjher,m kjerhm erjberkj
                kjerhkjre kje kjr kj  jgvjgjer kjhekjhrek rjjkekjre erkjhgr
              </p>
              </Collapsible>
          
          <Collapsible label="Mis Cursos">
            <li>some stuff</li>
            <li>some stuff</li>
            <li>some stuff</li>
            <li>some stuff</li>
          </Collapsible>
          
          <Collapsible label="Registros">

                <div class="curso1">
                   <img className="video" src= {imagenes.video}/>
                   <div class="tit-estrella">Asesoria de imagen personal</div>
                   <div class= "des-estrella">Impartido por Nombre Instructor</div>
                 </div>

                 <div class="curso2">
                   <img className="video" src= {imagenes.video}/>
                   <div class="tit-estrella">Asesoria de imagen personal</div>
                   <div class= "des-estrella">Impartido por Nombre Instructor</div>
                 </div>

                 <div class="curso3">
                   <img className="video" src= {imagenes.video}/>
                   <div class="tit-estrella">Asesoria de imagen personal</div>
                   <div class= "des-estrella">Impartido por Nombre Instructor</div>
                 </div>
            </Collapsible> */}
              
                   
                

  <h2 className="title1"> Mis cursos</h2>
  
  <br></br>         
{/* <MenuModal/> */}
     
      
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


export default Course;

