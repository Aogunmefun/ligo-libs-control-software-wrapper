import React, { useState, useContext } from "react";
import "./connect.css"
import { Context } from "../../app";
import Modal from "../modal/modal"

function Connect(props) {
    
    const [busy, setBusy] = useState("")
    const [modal, setModal] = useState({state:false, text:""})

    const app = useContext(Context)


    const connectSpectrometer = (val)=>{
        setBusy(true)
        app.eel.connectSpectrometer(val)((res)=>{
            setBusy(false)
            if(val) {
                if (res) {
                    props.setConnected({
                        ...props.connected,
                        spectrometer:val
                        })
                }
                else {
                    setModal({
                        state:true,
                        text:"Make sure that Both Channels of Spectrometer are connected"
                    })
                }
            }
            else {

            }
            
        })
    }

    const connectPDG = (val)=>{
        setBusy(true)
        app.eel.connectPDG(val)((res)=>{
            setBusy(false)
            if(val){
                if (res) {
                    props.setConnected({
                        ...props.connected,
                        pdg:true
                    })
                }
                else {
                    setModal({state:true, text:"Failed to Connect to PDG. Make sure USB is connected"})
                }
            }
            else {
                if(res) {
                    props.setConnected({
                        ...props.connected,
                        pdg:false
                    })
                }
                else {
                    setModal({state:true, text:"Failed to Close PDG connection"})
                }
            }
            
        })
    }

    const connectLaser = (val) =>{
        setBusy(false)
        props.setConnected({
            ...props.connected,
            laser:  val
        })
    }

    const connectRobot = (val)=>{
        setBusy(true)
        
        app.eel.connectRobot(val)((res)=>{
            setBusy(false)
            if(val) {
                if(res) {
                    props.setConnected({
                        ...props.connected,
                        robot: true
                    })
                }
                else {
                    setModal({state:true, text:"Failed to Connect to robot"})
                }
            }
            else {
                if (res) {
                    props.setConnected({
                        ...props.connected,
                        robot:false
                    })
                }
                else {
                    setModal({state:true, text:"Failed to disconnect from robot"})
                }
            }
            
        })
        

    }

    return(
        <div className="connect">
            <Modal close={true} modal={modal} setModal={setModal} />
            <div className="connectBoxes">
                <div className="connectBox">
                    <p>Spectrometer</p>
                    <div className="connectStatus">
                        Status: 
                        {/* {
                            props.connected.spectrometer?
                            <i className="material-icons">check</i>
                            : <i className="material-icons">close</i>
                        } */}
                        {props.connected.spectrometer?" Connected":" Not Connected"}
                    </div>
                    {props.connected.spectrometer?
                        <button className={`${busy?"disabled":""}`} onClick={()=>connectSpectrometer(false)}>Disconnect</button>
                        : <button className={`${busy?"disabled":""}`} onClick={()=>connectSpectrometer(true)}>Connect</button> }
                </div>
                <div className="connectBox">
                    <p>PDG</p>
                    <div className="connectStatus">
                        Status:
                        {props.connected.pdg?" Connected":" Not Connected"}
                    </div>
                    {
                        props.connected.pdg?
                        <button className={`${busy?"disabled":""}`} onClick={()=>connectPDG(false)}>Disconnect</button>
                        :<button className={`${busy?"disabled":""}`} onClick={()=>connectPDG(true)}>Connect</button>
                    }
                </div>
                <div className="connectBox">
                    <p>Laser</p>
                    <div className="connectStatus">
                        Status:
                        {props.connected.laser?" Connected":" Not Connected"}
                    </div>
                    {
                        props.connected.laser?
                        <button className={`${busy?"disabled":""}`} onClick={()=>connectLaser(false)} >Disconnect</button>
                        :<button className={`${busy?"disabled":""}`} onClick={()=>connectLaser(true)} >Connect</button>
                    }
                </div>
                <div className="connectBox">
                    <p>Robot</p>
                    <div className="connectStatus">
                        Status:
                        {props.connected.robot?" Connected":" Not Connected"}
                    </div>
                    {
                        props.connected.robot?
                        <button className={`${busy?"disabled":""}`} onClick={()=>connectRobot(false)}>Disconnect</button>
                        :<button className={`${busy?"disabled":""}`} onClick={()=>connectRobot(true)}>Connect</button>
                    }
                </div>
            </div>
        </div>
    )
}

export default Connect