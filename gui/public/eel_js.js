export const eel = window["eel"];

eel.expose(showModal);
function showModal(x) {
  console.log(x);
}


eel.expose(map)
function map(val) {
  console.log("here: ")
  console.log(val)
}