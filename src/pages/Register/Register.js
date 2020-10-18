import React, {useState, Component} from 'react';
//import {Text} from 'react-naive';
import imagenes from '../../assets/img/imagenes';
//import {link} from "react-router";

import './Register.css';

import Title from './Components/Title/Title';
import Label from './Components/Label/Label';
import Input from './Components/Input/Input'; 


const Register = () => {

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
        <div className= 'regcont'>

            <Title text= 'Knowture'> </Title>
            <div className='aprende'> ¡Aprende donde sea! </div>
            <div className='inscribete'> Inscribete y comienza a aprender  </div>
            <br></br>
            
            <Label text='Nombre de usuario'> </Label> 
            <Input
            attribute={{ //Apartado usuario
                id: 'nombreUsuario',
                name: 'nombreUsuario',
                type: 'text',
                placeholder: 'Nombre de Usuario'
            }}
            handleChange={handleChange}
            >
            </Input>

            <Label text='Correo electrónico'> </Label> 
            <Input
            attribute={{ //Apartado usuario
                id: 'usuario',
                name: 'usuario',
                type: 'text',
                placeholder: 'nombreusuario@hotmail.com'
            }}
            handleChange={handleChange}
            >
            </Input>


            <Label text='Contraseña'> </Label>
            <Input
            attribute={{ //Apartado contraseña
                id: 'contraseña',
                name: 'contraseña',
                type: 'password',
                placeholder: 'Ingrese su contraseña'
            }}
            handleChange={handleChange}
            param={passwordError}
            >
            </Input>
            
            <div className='boton-inicio-container'> 
            <button onClick={handleSubmit} className='boton-inicio-sesion'> 
                {/*<link to={"/register"}> Enlace a pagina*/}
                Registrate
                {/*</link>*/}
            </button>
            </div> 

            <div className='cuenta'> 
                ¿Ya tienes una cuenta?   
            </div>

            <a className='inicia' href="#example"> 
                Inicia Sesión  
            </a> 

            <img className="registro" src= {imagenes.registro}/>
                
        </div> 
    )
};

export default Register;

/* 
//Recibir el evento y se ejecuta la funcion handle submit
    <button onClick={handleSubmit}> //Va a esperar una funcion, definida a arriba 
        Ingresar
        
    </button> 
*/