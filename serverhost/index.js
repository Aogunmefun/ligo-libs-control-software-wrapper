const express = require('express')
const http = require('http')
// const { Server } = require('socket.io')


const app = express()
// app.use(
//     cors({
//         origin: ["http://localhost:3000","http://localhost:8080", "http://localhost:5500"]
//     })
// )
const server = http.createServer(app) 
// const io = new Server(server)
const io = require('socket.io')(server, {
    cors: {
      origin: '*',
    }
  });

app.get('/', (req,res)=>{
    console.log("Got request", req.body)
    res.end("hello")
})

// io.on('connection', (socket)=>{
//     console.log("user connected")
//     socket.on('disconnect', ()=>{
//         console.log("user disconnected")
//     })
//     socket.on("routine started", (msg)=>{
//         console.log(msg)
//     })
// })




server.listen(3000, ()=>{
    console.log("listening of port 3000...")
})