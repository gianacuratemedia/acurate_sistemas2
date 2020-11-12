import React from "react";
import { BrowserRouter, Route, Switch } from "react-router-dom";
import "./assets/css/App.css";

// components
import index from "./pages/IndexLayout/indexLayout";
import Login from "./pages/Login/Login";
import Register from "./pages/Register/Register";
import PlanSelection from "./pages/Plan Selection/PlanSelection";
import User from "./pages/User/User";
import UserProfile from "./pages/User/UserProfile";
import UserCourses from "./pages/User/UserCourses";
import Menu from "./pages/User/Components/Menu";


function App() {
  return (
    <BrowserRouter>
      <Switch>
        <Route exact path="/" component={index} />
        <Route exact path="/login" component={Login} />
        <Route exact path="/register" component={Register} />
        <Route exact path="/planselection" component={PlanSelection} />
        <Menu />
        <Route exact path="/User" component={User} />
        <Route exact path="/User/UserProfile" component={UserProfile} />
        <Route exact path="/User/UserCourses" component={UserCourses} />
      </Switch>
    </BrowserRouter>
  );
}

export default App;


