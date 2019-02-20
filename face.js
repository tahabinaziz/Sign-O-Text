
function  detect_faces(){
//alert("hi")

  var {PythonShell} = require('python-shell');
  var pyshell = new PythonShell('faces.py');
  
  pyshell.on('message', function (message) {
    console.log(message);
  });
  
  pyshell.send('hello');


}


detect_faces()


// function add_face(){
//   var python = require("python-shell")
//   var path = require("path")
//   var name = document.getElementById("person").value

//     var options = {
//     scriptPath : path.join(__dirname, '/../engine/'),
//     pythonPath : '/usr/local/bin/python3',
//     args : ["cam", name]
//   }

//   var face = new python("add_face.py", options);

//   face.end(function(err, code, message) {
//     swal("Face added!", "We can now recognize your face", "success")
//     document.getElementsById("add").innerHTML = "Add a new face";
//   })
// }
