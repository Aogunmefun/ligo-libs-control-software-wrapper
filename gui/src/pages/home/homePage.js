import React, { useState, useContext, useEffect } from "react";
import "./homePage.css"
import Laser from "../../components/laser/laser";
// import { eel } from "../../eel.js"
import Measurement from "../../components/measurement/measurement";
import Connect from "../../components/connect/connect";

function HomePage() {

    const [connected, setConnected] = useState({
        spectrometer: false,
        pdg: false,
        laser: false,
        robot:false
    })

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
            <Measurement connected={connected} />

            <Laser />
            
        </div>
    )
}

export default HomePage