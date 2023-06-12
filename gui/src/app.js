import React, { useState, useEffect, useContext } from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import './App.css';
import HomePage from "./pages/home/homePage";
import predictions from "./predict.json"
// import { eel } from "./eel_js"

export const Context = React.createContext()
export const eel = window.eel
eel.set_host( 'ws://localhost:8000/eel?page=index.html' )

eel.expose(showModal);
  function showModal(x) {
    
    
    console.log(x);
    
  }



function App() {

  // const [grid, setGrid] = useState(Array(720).fill(0))
  const [grid, setGrid] = useState(predictions)
  // const [index, setIndex] = useState(0)
  const [index, setIndex] = useState([0,0])
  const [data, setData] = useState([
    // {libs: 1, assay: 2, id:111},
    // {libs: 2, assay:4, id: 222},
    // {libs: 3, assay: 6, id: 333},
    // {libs: 4, assay:8, id: 444}
  ])

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

  eel.expose(currSample)
  function currSample(row, comp) {
    setIndex([row, comp])
  }

  eel.expose(graph)
  function graph(point) {
    console.log(point)
    setData([...data, {libs: point[0], assay: point[1], id: point[2]}])
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
    setIndex: setIndex,
    samples: [
      
  ],
    data:data,
    setData: setData
    
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
