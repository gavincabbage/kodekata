var codeEditor;
var testEditor;

function setupEditors() {
    codeEditor = ace.edit("codeEditor");
    codeEditor.setTheme("ace/theme/twilight");
    codeEditor.getSession().setMode("ace/mode/python");
    
    testEditor = ace.edit("testEditor");
    testEditor.setTheme("ace/theme/twilight");
    testEditor.getSession().setMode("ace/mode/python");   
}

function writeToConsole(text) {
    textarea = document.getElementById("console-text");
    text += "\n";
    textarea.value += text;
    textarea.scrollTop = textarea.scrollHeight;
}

function runTests() {
    writeToConsole("Clicked <Run Tests> Button");
}

function updateCodeStubs() {
    // Note: this bombs if nothing is selected, probably just make sure
    // the first thing is selected when I implement list population
    
    var kataSelect = document.getElementById("kata-select");
    var selectedKata = kataSelect.options[kataSelect.selectedIndex].value
    
    var languageSelect = document.getElementById("language-select");
    var selectedLanguage = languageSelect.options[languageSelect.selectedIndex].value
    
    writeToConsole(
        "Clicked <Update> Button, kata=" + selectedKata + 
        ", lang=" + selectedLanguage
    );
    
    var xmlhttp;
    if (window.XMLHttpRequest) {
        xmlhttp=new XMLHttpRequest();
    }
    else {
        xmlhttp=new ActiveXObject("Microsoft.XMLHTTP"); // for IE6, IE5
    }
    
    xmlhttp.onreadystatechange = function() {
        if (xmlhttp.readyState==4 && xmlhttp.status==200) {
            var response = JSON.parse(xmlhttp.responseText);
            codeEditor.setValue(response.code);
            testEditor.setValue(response.code);
        }
    }
    
    var url = "/kata/" + selectedKata + "/lang/" + selectedLanguage;
    xmlhttp.open("GET", url, true);
    xmlhttp.send();
}

setupEditors();
writeToConsole("Welcome to KodeKata!");
codeEditor.setValue("# This is the code editor. Code goes here.", 1);
testEditor.setValue("# And this is the test editor. Tests go here.", 1);


function loadXMLDoc()
{
    if (window.XMLHttpRequest)
    {// code for IE7+, Firefox, Chrome, Opera, Safari
        xmlhttp=new XMLHttpRequest();
    }
    else
    {// code for IE6, IE5
        xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
    }
    
    xmlhttp.onreadystatechange=function()
    {
        if (xmlhttp.readyState==4 && xmlhttp.status==200)
        {
            document.getElementById("myDiv").innerHTML=xmlhttp.responseText;
        }
    }
    
    xmlhttp.open("GET","ajax_info.txt",true);
    xmlhttp.send();
}


// EX: AJAX
// http://stackoverflow.com/questions/4677146/post-without-redirecting-page
// if (window.XMLHttpRequest) {
//     xmlhttp = new XMLHttpRequest();
// } else {
//     xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
// }
// var url = "/kodekata/{{language}}";
// xmlhttp.open("POST", url, false);
// xmlhttp.send(editor1.getValue() + editor2.getValue());
// var respo= xmlhttp.responseText;
// document.getElementById("console-text").value = xmlhttp.responseText;

// EX: Populate select list
// window.onload = function() {
//     var select = document.getElementById("MyList");
//     var options = ["1", "2", "3", "4", "5"];
//     for (var i = 0; i < options.length; i++) {
//         var opt = options[i];
//         var el = document.createElement("option");
//         el.textContent = opt;
//         el.value = opt;
//         select.appendChild(el);
//     }
// }

// EX: Clear select list
// http://stackoverflow.com/questions/3364493/how-do-i-clear-all-options-in-a-dropdown-box
// function removeOptions(selectbox)
// {
//     var i;
//     for(i=selectbox.options.length-1;i>=0;i--)
//     {
//         selectbox.remove(i);
//     }
// }
// //using the function:
// removeOptions(document.getElementById("mySelectObject"));