import React, {useState, Component} from 'react';
//import {Text} from 'react-naive';
import imagenes from '../../assets/img/imagenes';
//import {link} from "react-router";

import './PlanSelection.css';

import Label from './Components/Label Plan/LabelPlan';
import Input from './Components/Input Plan/InputPlan'; 


const PlanSelection = () => {

    //Estados
    const [user, setUser] = useState(''); //Buscar
    //const [nombreUsuario, setUser] = useState(''); //Buscar
    const [password, setPassword] = useState(''); //Buscar
    const [passwordError, setPasswordError]=useState(false);

    function handleChange(name, value){ //Si es el ingreso (en text box) de usuario tomar info, si es el de contraseña no
        if(name === 'usuario'){
            setUser(value)
        } 
        else{ 
            if(value.length < 6){ //Solo de tamaño seran mas de 6 caracteres
                setPasswordError(true);
            }
            else{
                setPasswordError(false);
                setPassword(value)
            }
        } 
    };

    function handleSubmit(){ 
        let account = {user, password} //Armar una variable llamada account que estara compuesto por user y password
        if(account){
            //Aqui en base de datos 
            console.log('account:', account)

        }
    };

    return (
        <div className= 'plancont'>

            <div className="section-right">
            <div className="headerSection">
            <img className="logo" src= {imagenes.logoazul}/>
            </div>

            <div className='comienza'> 
                Comienza 15 días gratis   
            </div>

            <div className='compromiso'> 
                Sin compromiso. Cancela cuando quieras.  
            </div>

            <div className='plan'> 
                Selecciona tu plan  
            </div>
            

            <div class="container-gratis">
                <div class="titulo-plan">Prueba Gratis</div>
                <div class= "desc-plan"><strong>$0.00</strong> / al mes</div>
          
                <a className="boton-conviertete" href="#">
                    ¡Conviértete en Premium!
                </a>
            </div>

            <div class="container-mensual">
                <div class="titulo-plan">Prueba mensual</div>
                <div class= "desc-plan"><strong>$9.00</strong> / al mes</div>

                <a className="boton-conviertete" href="#">
                    ¡Conviértete en Premium!
                </a>
            </div>

            <div class="container-anual">
                <div class="titulo-plan">Prueba anual</div>
                <div class= "desc-plan"><strong>$79.00</strong> / al mes</div>

                <a className="boton-conviertete" href="#">
                    ¡Conviértete en Premium!
                </a>
            </div>


            <Label text='Selecciona tu forma de pago'> </Label> 
            <div>
                <input type="radio" value="credito" name="pago" /> Crédito o débito
                <input type="radio" value="paypal" name="pago" /> PayPal
            </div>

            <Label text='Número de tarjeta'> </Label> 
            <div className='inputTarjeta'>
            <Input
            attribute={{ //Apartado usuario
                id: 'numTarjeta',
                name: 'numTarjeta',
                type: 'text'
            }}
            handleChange={handleChange}
            >
            </Input>
            </div>

            <Label text='Expiración'> </Label> 
            <div className='inputExpiracion'>
            <Input
            attribute={{ //Apartado usuario
                id: 'numExpiracion',
                name: 'numExpiracion',
                type: 'text',
                placeholder: 'MM/YY'
            }}
            handleChange={handleChange}
            >
            </Input>
            </div>
            
            <Label text='Código de seguridad'> </Label> 
            <div className='inputCodigo'>
            <Input
            attribute={{ //Apartado usuario
                id: 'numCodigo',
                name: 'numCodigo',
                type: 'text'
            }}
            handleChange={handleChange}
            >
            </Input>
            </div>
            
            
            <Label text='Ingresa cupón de descuento'> </Label> 
            <div className='boton-continuar-container'> 
            <button onClick={handleSubmit} className='boton-continuar-seleccion'> 
                {/*<link to={"/register"}> Enlace a pagina*/}
                Continuar
                {/*</link>*/}
            </button>
            </div> 
            </div>

            <a className='inicia' href="#example"> 
                Inicia Sesión  
            </a> 

                
        </div> 
    )
};

export default PlanSelection;
