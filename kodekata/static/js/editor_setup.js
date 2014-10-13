var editor1 = ace.edit("editor1");
editor1.setTheme("ace/theme/chaos");
editor1.getSession().setMode("ace/mode/python");

var editor2 = ace.edit("editor2");
editor2.setTheme("ace/theme/chaos");
editor2.getSession().setMode("ace/mode/python");

function runTests() {
    // this code adapted from here:
    // http://stackoverflow.com/questions/4677146/post-without-redirecting-page
    if (window.XMLHttpRequest) {
        xmlhttp = new XMLHttpRequest();
    } else {
        xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
    }
    var url = "/kodekata/{{language}}";
    xmlhttp.open("POST", url, false);
    xmlhttp.send(editor1.getValue() + editor2.getValue());
    var respo= xmlhttp.responseText;
    document.getElementById("console-text").value = xmlhttp.responseText;
}