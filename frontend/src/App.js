import './App.css';
import React from 'react';
import {Routes, Route} from 'react-router-dom';
import Home from './components/Home';
import About from './components/About';
import Create from './components/Create';
import Navbar from './components/NavBar';
import Edit from './components/Edit';
import Delete from './components/Delete';
import IndecolLoad from './components/IndecolLoad';
import Person from './components/Person';
import Create_person from './components/Create_person';
import Edit_person from './components/Edit_person';
import Person_course from './components/Person_course';
import Delete_person from './components/Delete_person';
// import Person_activity from './components/Person_activity';
// import BarChart from './Charts/BarChart';


function App() {
  const myWidth = 220
  return (
    <div className="App">
      {/* <BarChart /> */}
      <Navbar drawerWidth={myWidth}
        content ={      
        <Routes>
          <Route path ="" element={<Home/>}/>
          <Route path ="/about" element={<About/>}/>
          <Route path ="/create" element={<Create/>}/>
          <Route path ="/edit/:id" element={<Edit/>}/>
          <Route path ="/person/edit_person/:id" element={<Edit_person/>}/>
          <Route path ="/delete/:id" element={<Delete/>}/>
          <Route path ="/person/delete_person/:id" element={<Delete_person/>}/>
          <Route path ="/indecolLoad" element={<IndecolLoad/>}/>
          <Route path ="/person" element={<Person/>}/>
          <Route path ="/create_person" element={<Create_person/>}/>
          <Route path ="/person_course" element={<Person_course/>}/>
          {/* <Route path ="/person_activity" element={<Person_activity/>}/> */}


       </Routes>
      }
      />
      


   

    </div>
  );
}

export default App;


