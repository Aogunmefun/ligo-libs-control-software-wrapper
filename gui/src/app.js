import React, { useState, useEffect, useContext } from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import './App.css';
import HomePage from "./pages/home/homePage";
// import { eel } from "./eel_js"

export const Context = React.createContext()
export const eel = window.eel
eel.set_host( 'ws://localhost:8000/eel?page=index.html' )

eel.expose(showModal);
  function showModal(x) {
    
    
    console.log(x);
    
  }



function App() {

  const [grid, setGrid] = useState(Array(720).fill(0))
  const [index, setIndex] = useState(0)

  eel.expose(map)
  function map(val) {
    let temp = grid
    if (val < 0) val = 0
    // console.log("here: ")
    console.log("raw value", val)
    temp[index] = (val-0.061)/1.5
    setGrid([...temp])
    setIndex(index+1)
  }

  useEffect(()=>{
    // app.eel.set_host("ws://localhost:8000/eel?page=index.html")
    console.log(app.eel)
    
  },[])

  const app = {
    eel:eel,
    grid:grid,
    setGrid:setGrid,
    index: index,
    setIndex: setIndex

    
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
