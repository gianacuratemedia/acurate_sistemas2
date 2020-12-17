import React, {useState, Component} from 'react'
import * as RiIcons from "react-icons/ri";
import { Link } from 'react-router-dom';
import { MenuData } from './MenuData'
import './Course2.css'
import imagenes from '../../assets/img/imagenes';
import axios, {post} from 'axios';
import API from "../../services/api";

class UploadFiles extends Component{

    constructor(props){
        super(props);
        this.state = {
            image: ''
        }
    }

    onChange(e){
        let files = e.target.files;
        
        let reader = new FileReader();
        reader.readAsDataURL(files[0]);

        reader.onload=(e)=>{
            //console.warn("img data", e.target.result)


            const url = "http://165.227.62.217/service/api"

            const formData = {file:e.target.result}
            return post(url, formData)
            .then(response=>console.warn("result", response))
        }

    }

    render(){
        
        return(
            <>
        
            <div className= 'agregar-tarea'>

            <RiIcons.RiFileUploadLine onClick="#" className="icono-upload"/>

            <div className='Titulo3'> 
                Agregar tarea  
            </div>

            <div className='Titulo4'> 
                Descripción Descripción Descripción Descripción   
            </div>            

            <div onSubmit={this.onFormSubmit}>
            <input type="file" className="agregar2" placeholder="Seleccionar archivos" onChange={(e) => this.onChange(e)}/> 
            </div>

            <div className='desc1'> 
                Cuando subes un video estas aceptando los terminos y condiciones
                de knowtured. En cuanto tu video sea aceptado y editado nos pondremos 
                al contacto   
            </div> 
 
            </div> 

        </>
        )
    }


}


export default UploadFiles;
