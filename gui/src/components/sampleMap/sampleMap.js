import React, { useState, useContext, useEffect } from "react";
import "./sampleMap.css"
import { Context } from "../../app";


function SampleMap(props) {
    
    const app = useContext(Context)

    useEffect(()=>{
        console.log("State updated")
    })

    return(
        <div className="sampleMap">
            <div className="holder">
                {
                    app.grid.map((value,index)=>{
                        {/* console.log(value) */}
                        return(
                            <div onClick={()=>app.eel.plot(index)} style={{backgroundColor:`${value>1?"rgb(255, 0, 0)":`${index===app.index?"green":`rgb(255, ${255-(value*255)}, ${255-(value*255)})`}`}`}} className="frame">
                                
                            </div>
                        )
                    })
                }
            </div>
        </div>
    )
}

export default SampleMap