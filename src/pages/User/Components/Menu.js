import React, {useState} from 'react'
import * as FaIcons from 'react-icons/fa';
import * as AiIcons from 'react-icons/ai';
import { Link } from 'react-router-dom';
import { MenuData } from './MenuData'
import './Menu.css'


function Menu() {
    const [sidebar, setSidebar] = useState (false); /*No mostrar barra*/

    const showSidebar = () => setSidebar (!sidebar); /*Mostrar barra*/


    return (
        <>
        <div className='navbar'>
            <Link to='#' className='menu-bars'>
            <FaIcons.FaBars onClick={showSidebar}/> {/*Icono de barras de react*/}
            </Link>
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
                    )
                })}
            </ul>
        </nav>
        </>
    )
}

export default Menu;
