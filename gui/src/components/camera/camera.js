import React, { useState, useContext, useEffect } from "react";
import "./camera.css"
import { Context } from "../../app"
import frame from "../../frame.png"

function Camera(props) {

    const [img, setImg] = useState(false)
    const app = useContext(Context)

    useEffect(()=>{
        let video = document.getElementById("camVideo"); // video is the id of video tag
        navigator.mediaDevices.getUserMedia({ video: true, audio: false })
            .then(function(stream) {
                video.srcObject = stream;
                video.play();
            })
            .catch(function(err) {
                console.log("An error occurred! " + err);
            });
    }, [])

    return(
        <div className="camera">
            <video id="camVideo" src="" width={"100%"}></video>
            
        </div>
    )
}
export default Camera