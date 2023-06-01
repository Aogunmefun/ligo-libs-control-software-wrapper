import React, { useState, useContext, useEffect } from "react";
import "./homePage.css"
import Laser from "../../components/laser/laser";
// import { eel } from "../../eel.js"
import Measurement from "../../components/measurement/measurement";
import Connect from "../../components/connect/connect";
import Graph from "../../components/graph/graph";
import Camera from "../../components/camera/camera";
import SampleMap from "../../components/sampleMap/sampleMap";
import { Context } from "../../app";


function HomePage() {

    const [connected, setConnected] = useState({
        spectrometer: false,
        pdg: false,
        laser: false,
        robot:false
    })
    const app = useContext(Context)

    useEffect(()=>{
        // const script = document.createElement('script');
        // script.src = "http://localhost:8888/eel.js";
        // script.async = true;
        // // const eel = eel;
        // console.log(eel)
        // eel.set_host("ws://localhost:8000");
        // eel.showModal();
    }, [])

    
    

    

    const showModal = (txt) =>{
        console.log("clicked")
        // eel.showModal(txt)
    }
    

    return(
        <div className="homePage">
            {/* <button onClick={()=>eel.showModal()}>Run</button> */}
            
            <Connect connected={connected} setConnected={setConnected} />

            <div className="measurementInfo">
                {/* <Measurement connected={connected} /> */}
                {/* <Camera /> */}
                {/* <SampleMap /> */}
                <button onClick={()=>app.eel.beginRoutine(1,2)}>1</button>
                <button onClick={()=>app.eel.beginRoutine(7,2)}>7</button>
            </div>
            {/* <button onClick={()=>{

                app.setGrid(Array(720).fill(0))
                app.setIndex(0)
            }}>Clear</button> */}
            

            {/* <Laser /> */}

            
        </div>
    )
}

export default HomePage