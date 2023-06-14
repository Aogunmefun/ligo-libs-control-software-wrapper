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
import PullDown from "../../components/pulldown/pulldown.js";
import Tray from "../../components/tray/tray"
import pic from "../../samplePicture.jpg"



function HomePage() {

    const [connected, setConnected] = useState({
        spectrometer: false,
        pdg: false,
        laser: false,
        robot:false
    })
    const app = useContext(Context)
    const [trays, setTrays] = useState([
        [18006027550,
            17502452100,
        18006038550,
        18006090550,
        18006084550,
        ],
            [18006035550,
        18006058550,
        17502436100,
        17001280550,
        17001365550,
        ],
            [17001273550,
        18005986550,
        17001282550,
        17001335550,
        17001284550
        ],
            [17001320550,
        17001293550,
        17507146550,
        17001292550,
        17507136550
        ],
            [17001315550,
        17502388100,
        17507191550,
        18006018550,
        18006041550
        ],
            [17001373550,
        17001354550,
        17502476100,
        18006063550,
        17001343550
        ],
            [17001316550,
        17502394100,
        17507193550,
        17001327550,
        17507199550
        ],
            [17502396100,
        17502421100,
        17502463100,
        17507126550,
        17507138550
        ],
            [17507106550,
        17001313550,
        17507099550,
        17507089550,
        17001355550
        ],
            [17001338550,
        17001308550,
        17001279550,
        17001366550,
        17507155550
        ]
    ])
    const [index, setIndex] = useState([0,0])
    const [file, setFile] = useState("")
    const [mode, setMode] = useState("statistical")
    const [showGraph, setShowGraph] = useState(false)

    useEffect(()=>{
        // const script = document.createElement('script');
        // script.src = "http://localhost:8888/eel.js";
        // script.async = true;
        // // const eel = eel;
        // console.log(eel)
        // eel.set_host("ws://localhost:8000");
        // eel.showModal();
        document.querySelector(".selectTrays")?.addEventListener("click",(ev)=>{
            console.log(ev.target.className)
            if (ev.target.className.includes("traySelected") || ev.target.className.includes("selectTrays")) {
                ev.target.classList.remove("traySelected")
            }
            else {
                ev.target.classList.add("traySelected")
            }
            // console.log(document.querySelector(".traySelected"))
            
        })
    }, [mode])

    
    

    

    const showModal = (txt) =>{
        console.log("clicked")
        // eel.showModal(txt)
    }

    const handleFile = (ev)=>{
        setFile(ev.target.value)
        console.log(ev.target.value)
    }

    const changeMode = (ev)=>{
        setMode(ev.target.value)
    }
    

    return(
        <div className="homePage">
            
            {/* <button onClick={()=>eel.showModal()}>Run</button> */}
            <PullDown show={showGraph} setShow={setShowGraph} />
            <Connect connected={connected} setConnected={setConnected} />
            {
                mode==="statistical"?
                <>
                <h3>Tower 1</h3>
                <div className="measurementInfo">
                    
                    {/* <Measurement connected={connected} /> */}
                    {/* <Camera /> */}
                    
                    <i className="material-icons">arrow_back_ios</i>
                    <div className="sampleLoader">
                        {
                            trays.map((tray, index)=>{
                                return(
                                <Tray key={"tray"+index} 
                                    index={index} 
                                    tray={tray}
                                    setIndex={setIndex} 
                                    current = {app.index[0]===index?true:false}
                                    sampleind = {app.index[1]}  
                                    />
                                )
                            })
                        }
                    </div>
                    <i className="material-icons">arrow_forward_ios</i>
                    
                </div>
                <button onClick={()=>app.eel.runAll()}>Run All</button>
                <div className="traySelection">
                    <button onClick={()=>{
                        let selectedIndexes = [] 
                        document.querySelectorAll(".trayOption").forEach((item,ind)=>{
                            // console.log(item.className)
                            if (item.className.includes("traySelected")) selectedIndexes.push(ind)
                        })
                        console.log("indexes", selectedIndexes)
                        app.eel.runSelected(selectedIndexes)
                    }}>Run Selected</button>
                    <div className="selectTrays">
                        <div className="trayOption">1</div>
                        <div className="trayOption">2</div>
                        <div className="trayOption">3</div>
                        <div className="trayOption">4</div>
                        <div className="trayOption">5</div>
                        <div className="trayOption">6</div>
                        <div className="trayOption">7</div>
                        <div className="trayOption">8</div>
                        <div className="trayOption">9</div>
                        <div className="trayOption">10</div>
                    </div>
                </div></>:
                <div className="mappingContainer">
                    <img src={pic} width="500px" alt="" />
                    <SampleMap />
                </div>

            }
            <div className="robotCommands">
                <h2>Robot Commands</h2>
                <button onClick={()=>app.eel.moveTower1()} className="btn--flat">Move Tower 1</button>
                <button onClick={()=>app.eel.gotoScanPosition()} className="btn--flat">Move scan position</button>
                <button onClick={()=>app.eel.release()} className="btn--flat">Unlock</button>
                <button onClick={()=>app.eel.lock()} className="btn--flat">Lock</button>
                <button className="btn--flat stop">Stop</button>
            </div>
            <div className="filePicker">
                <input type="file" name="file" id="file" onChange={handleFile} value={file} />
            </div>
            <div className="runMode">
                <h5>Mode Select:</h5>
                <select name="" id="" value={mode} onChange={changeMode}>
                    <option value="statistical">Statistical</option>
                    <option value="mapping">Mapping</option>
                </select>
            </div>
            <button onClick={()=>app.eel.beginRoutine()}>Start Mapping</button>

            {/* <button onClick={()=>{

                app.setGrid(Array(720).fill(0))
                app.setIndex(0)
            }}>Clear</button> */}
            

            {/* <Laser /> */}

            
        </div>
    )
}

export default HomePage