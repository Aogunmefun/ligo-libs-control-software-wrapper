import React, { useState } from "react";
import "./laser.css"


function Laser(props) {
    

    return(
        <div className="laser">
            
            <div className="laserStatus">
                <p>Laser State</p>
                <div className="laserState">
                    <i className="material-icons">circle</i>
                    <p>Laser is ready for Emmision</p>
                </div>
                <div className="laserState">
                    <i className="material-icons">circle</i>
                    <p>Mission</p>
                </div>
                <div className="laserState">
                    <i className="material-icons">circle</i>
                    <p>24V Supply Good</p>
                </div>
                <div className="laserState">
                    <i className="material-icons">circle</i>
                    <p>Interlock Engaged</p>
                </div>
            </div>
            <div className="laserControl">
                <p>Laser control</p>
                <form className="laserControl" >
                    <label htmlFor="power">Output Power:</label>
                    <input type="range" id="power" min={0} max={100} step={25} list={"steplist"} />
                    <datalist id="steplist">
                        <option>0</option>
                        <option>25</option>
                        <option>50</option>
                        <option>75</option>
                        <option>100</option>
                    </datalist>
                    <button>Turn On</button>
                </form>
            </div>
        </div>
    )
}

export default Laser