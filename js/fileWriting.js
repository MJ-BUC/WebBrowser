function Append(content) {
    
    const fs = require('fs');

    fs.appendFile('C:\\Users\\lunke\\OneDrive\\Documents\\Github\\WebBrowser\\webdata.txt', content + "\n", err => {
        if (err) {
            console.err;
            return;
        }
    });
}

// debugging for js file
// Append("Cheese" + "\n");


// function WriteToFile(passForm) { 
 
//     var fso = CreateObject("Scripting.FileSystemObject");  
//     var s = fso.CreateTextFile("C:\\Users\\lunke\\OneDrive\\Documents\\Github\\WebBrowser\\webdata.txt", True); 
 
//     var firstName = document.getElementById('FirstName'); 
//     var lastName = document.getElementById('lastName'); 
 
//     s.writeline("First Name :" + firstName); 
//     s.writeline("Last Name :" + lastName); 
 
//     s.writeline("-----------------------------"); 
//     s.Close(); 
//  }


// testing for js
// function Hello() {
//     alert("Hello, World");
//  }