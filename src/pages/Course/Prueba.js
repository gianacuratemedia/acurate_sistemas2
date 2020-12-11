import React, {Component} from 'react';
import Calendar from 'react-calendar';

import 'react-calendar/dist/Calendar.css';


export default class Prueba extends Component{
    state ={
        date : new Date()
    }

    onChange = date => {
        this.setState({
            date :date
        })
    }

    render(){
        return(
            <div>
                <Calendar
                onChange={this.onChange}
                />
            </div>
        )
    }


}



/* export default function Prueba() {
      state = {
          date : new Date()
    }
    
    onChange = date =>{
        this.setState({
            date:date
        })
    }

    return(
        <div >
         <Calendar />
        </div>
    )
} */