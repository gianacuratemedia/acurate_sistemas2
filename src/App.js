import React from "react";
import { BrowserRouter, Route, Switch } from "react-router-dom";
import "./assets/css/App.css";


// components
import index from "./pages/IndexLayout/indexLayout";
import Login from "./pages/Login/Login";
import Register from "./pages/Register/Register";
import Pay from './pages/pay/pay';
import PlanSelection from "./pages/Plan Selection/PlanSelection";

function App() {
  return (
    <BrowserRouter>
      <Switch>
        <Route exact path="/" component={index} />
        <Route exact path="/login" component={Login} />
        <Route exact path="/register" component={Register} />
        <Route exact path="/pay" component={Pay}/>
        <Route exact path="/planselection" component={PlanSelection} />
      </Switch>
    </BrowserRouter>
  );
}

export default App;


