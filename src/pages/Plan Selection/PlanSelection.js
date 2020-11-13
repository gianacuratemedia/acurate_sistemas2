import React from 'react';
import imagenes from '../../assets/img/imagenes';


import './PlanSelection.css';


const PlanSelection = () => {

    
    return (
    <div className= 'plancont'>

        <div className="headerSection">
            <img className="logo" src= {imagenes.logoazul}/>
        </div>

        <div className="section-left">
            

        
            <div className='comienza'> 
                Comienza 15 días gratis   
            </div>

            <div className='compromiso'> 
                Sin compromiso. Cancela cuando quieras.  
            </div>

            <div className='plan'> 
                Selecciona tu plan  
            </div>
            

            <div class="cont-gratis">
                <div class="tit-plan">Prueba Gratis</div>
                <div class= "des-plan"><strong>$0.00</strong> / al mes</div>
          
                <a className="boton-convierte" href="#">
                    ¡Conviértete en Premium!
                </a>
            </div>

            <div class="cont-mensual">
                <div class="tit-plan">Prueba mensual</div>
                <div class= "des-plan"><strong>$9.00</strong> / al mes</div>

                <a className="boton-convierte" href="#">
                    ¡Conviértete en Premium!
                </a>
            </div>

            <div class="cont-anual">
                <div class="tit-plan">Prueba anual</div>
                <div class= "des-plan"><strong>$79.00</strong> / al mes</div>

                <a className="boton-convierte" href="#">
                    ¡Conviértete en Premium!
                </a>
            </div>


            <div className="forma-pago"> 
                Selecciona tu forma de pago
            </div>
            <a className='boton-paypal' href="#example"> 
                Paga con PayPal  
            </a> 

            <div className="cupon"> 
                Ingresa cupón de descuento
            </div>

            <a className='boton-continuar' href="#example"> 
                Continuar  
            </a> 


        </div>

        <div class="section-right">

            <div className="beneficio"> 
                Beneficios Premium
            </div>

            <div class="row container">

            <div class="cont-avanza">
            <img className="estrellas" src= {imagenes.estrellas}/>
            <div class="tit-estrella">+600 cursos en linea</div>
            <div class= "des-estrella">Encuentra tu curso ideal y aprende habilidades nuevas en menos de 2 horas</div>
            </div>

            <div class="cont-instruccion">
                <img className="estrellas" src= {imagenes.estrellas}/>
                <div class="tit-estrella">Avanza a tu propio ritmo</div>
                <div class= "des-estrella">Disfruta de acceso exclusivo a cursos en línea a tu propio horario y ritmo</div>
            </div>

            <div class="cont-mas">
            <img className="estrellas" src= {imagenes.estrellas}/>
            <div class="tit-estrella">Instrucción Experta</div>
            <div class= "des-estrella">Encuentra el instructor adecuado y aprende de los expertos de la industria</div>
            </div>

        </div>
      </div>
         
    </div> 
    )
};

export default PlanSelection;
