import React, { useEffect } from "react";
import "./pulldown.css"
import Graph from "../graph/graph";

function PullDown(props) {
    
    return(
        <div onClick={()=>props.setShow(!props.show)} style={{height: `${props.show?"500px":"20px"}`}} className="pulldown">
            <div className="arrowPullDown"><i
                style={{transform:`${!props.show?"rotate(0)":"rotate(180deg)"}`}}
                className="material-icons">arrow_drop_down</i>
            </div>
            <Graph />
        </div>
    )
}

export default PullDown