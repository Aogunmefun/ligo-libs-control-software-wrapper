import React, { useState, useEffect, useContext } from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import './App.css';
import HomePage from "./pages/home/homePage";

export const Context = React.createContext()

function App() {


  useEffect(()=>{
    
  })

  const app = {

  }

  return (
    
    <BrowserRouter>
      <Context.Provider value={app} >
        <Routes>
          <Route path="/" element={<HomePage />} />
        </Routes>
      </Context.Provider>
    </BrowserRouter>

  );
}

export default App;
