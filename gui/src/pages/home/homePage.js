import React, { useState, useContext, useEffect } from "react";
import "./homePage.css"
import Laser from "../../components/laser/laser";
import { eel } from "../../eel.js"


function HomePage() {

    const [msmName, setMsmName] = useState("")
    const [frames, setFrames] = useState("")
    const [period, setPeriod] = useState("")

    useEffect(()=>{
        // const script = document.createElement('script');
        // script.src = "http://localhost:8888/eel.js";
        // script.async = true;
        // // const eel = eel;
        // console.log(eel)
        eel.set_host("ws://localhost:8888");
        eel.showModal("yo");
    }, [])

    
    

    const changeMsmName = (ev)=>{
        setMsmName(ev.target.value)
    }

    const changeFrames = (ev)=>{
        setFrames(ev.target.value)
    }

    const changePeriod = (ev)=>{
        // if (typeof ev.target.value === "string") return
        setPeriod(ev.target.value)
    }

    const showModal = (txt) =>{
        console.log("clicked")
        eel.showModal(txt)
    }
    

    return(
        <div className="homePage">
            <button onClick={()=>window.dispatchEvent(new CustomEvent('startRoutine'))}>Start Routine</button>
            <div className="msmSection">
                <p style={{fontSize:"18px", color:"var(--primaryColor)"}}>Measurement Config</p>
                <form className="msmForm" >
                    <div className="msmName">   
                        <input type="text" placeholder="Measurement Name" value={msmName} onChange={changeMsmName} />
                        {/* <i className="material-icons">check</i> */}
                    </div>
                    {/* <label htmlFor="frames">Frame Number:</label> */}
                    <input id="frames" type="number" placeholder="Enter numer of frames" value={frames} onChange={changeFrames}  />
                    <input type="number" placeholder="PDG Period" value={period} onChange={changePeriod} />
                </form>
            </div>

            <Laser />
            
        </div>
    )
}

export default HomePage