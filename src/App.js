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
import UserTeacher from "./pages/UserTeacher/UserTeacher";
import UserTeacherProfile from "./pages/UserTeacherProfile/UserTeacherProfile";
import UserTeacherCourse from "./pages/UserTeacherCourse/UserTeacherCourse";
import AdvancementLevel from "./pages/AdvancementLevel/AdvancementLevel";
import Chat from "./pages/Chat/Chat";
import UserTeacherResources from "./pages/UserTeacherResources/UserTeacherResources";
import UserTeacherResources2 from "./pages/UserTeacherResources/UserTeacherResources2";
import UserTeacherResources3 from "./pages/UserTeacherResources/UserTeacherResources3";
import UserTeacherResources4 from "./pages/UserTeacherResources/UserTeacherResources4";
import PasswordRcueperar from "./pages/RecuperarPassword/recuperarpass";
import Course from "./pages/Course/Course";
import CourseTeacherResources from "./pages/CourseTeacherResources/CourseTeacherResources";
import UploadFiles from "./pages/CourseTeacherResources/UploadFiles";
import RecuperarPass from "./pages/RecuperarPassword/recuperarpass";

function App() {
  return (
  
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
        <Route exact path="/UserTeacherProfile" component={UserTeacherProfile} />
        <Route exact path="/UserTeacherCourse" component={UserTeacherCourse} /> 
        <Route exact path="/AdvancementLevel" component={AdvancementLevel} /> 
        <Route exact path="/Chat" component={Chat} />
        <Route exact path="/UserTeacherResources" component={UserTeacherResources} /> 
        <Route exact path="/UserTeacherResources2" component={UserTeacherResources2} /> 
        <Route exact path="/UserTeacherResources3" component={UserTeacherResources3} /> 
        <Route exact path="/UserTeacherResources4" component={UserTeacherResources4} /> 
        <Route exact path="/recuperarPass" component={PasswordRcueperar} /> 
        <Route exact path="/Course" component={Course} />
        <Route exact path="/CourseTeacherResources" component={CourseTeacherResources} /> 
        <Route exact path="/UploadFiles" component={UploadFiles} /> 
        <Route exact path="/RecuperarPassword" component={RecuperarPass} /> 
      </Switch>
    </BrowserRouter>
  
  );
}



export default App;


