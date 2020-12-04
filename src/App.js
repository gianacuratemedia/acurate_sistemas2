import React from "react";
import { BrowserRouter, Route, Switch } from "react-router-dom";
import "./assets/css/App.css";

// components
import index from "./pages/IndexLayout/indexLayout";
import Login from "./pages/Login/Login";
import Register from "./pages/Register/Register";
import Categorias from "./pages/Categorias/Categorias";
import PlanSelection from "./pages/Plan Selection/PlanSelection";
import User from "./pages/User/User";
import UserProfile from "./pages/UserProfile/UserProfile";
import UserCourses from "./pages/UserProfile/UserCourses";
import UserTeacher from "./pages/UserTeacher/UserTeacher";
import UserTeacherProfile from "./pages/UserTeacherProfile/UserTeacherProfile";
import UserTeacherCourses from "./pages/UserTeacherCourses/UserTeacherCourses";
import AdvancementLevel from "./pages/AdvancementLevel/AdvancementLevel";
import Chat from "./pages/Chat/Chat";
import UserTeacherResources from "./pages/UserTeacherResources/UserTeacherResources";
import UserTeacherResources2 from "./pages/UserTeacherResources/UserTeacherResources2";
import UserTeacherResources3 from "./pages/UserTeacherResources/UserTeacherResources3";
import UserTeacherResources4 from "./pages/UserTeacherResources/UserTeacherResources4";

function App() {
  return (
    <>
    <BrowserRouter>
      <Switch>
        <Route exact path="/" component={index} />
        <Route exact path="/login" component={Login} />
        <Route exact path="/register" component={Register} />
        <Route exact path="/Categorias" component={Categorias}/>
        <Route exact path="/planselection" component={PlanSelection} />
        <Route exact path="/UserTeacher" component={UserTeacher} />
        <Route exact path="/User" component={User} />
        <Route exact path="/UserProfile" component={UserProfile} />
        <Route exact path="/UserCourses" component={UserCourses} />
        <Route exact path="/UserTeacherProfile" component={UserTeacherProfile} />
        <Route exact path="/UserTeacherCourses" component={UserTeacherCourses} /> 
        <Route exact path="/AdvancementLevel" component={AdvancementLevel} /> 
        <Route exact path="/Chat" component={Chat} />
        <Route exact path="/UserTeacherResources" component={UserTeacherResources} /> 
        <Route exact path="/UserTeacherResources2" component={UserTeacherResources2} /> 
        <Route exact path="/UserTeacherResources3" component={UserTeacherResources3} /> 
        <Route exact path="/UserTeacherResources4" component={UserTeacherResources4} /> 
      </Switch>
    </BrowserRouter>
    </>
  );
}



export default App;


