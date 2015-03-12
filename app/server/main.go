package main

import (
    "os"
    "fmt"
    "net/http"
    "github.com/gorilla/mux"
    "html/template"
    "encoding/json"
    "./structs"
)

func pageHandler(w http.ResponseWriter, r *http.Request) {
    
    t, err := template.ParseFiles("/home/ubuntu/workspace/src/github.com/gavincabbage/kodekata/app/templates/base.html")
    if err != nil {
        w.Write([]byte("Error while parsing template"))
    }
    
    mainTitleText := "KodeKata"
    vals := structs.MainPageValues{MainTitleText: mainTitleText}
    t.Execute(w, vals)
}

func stubHandler(w http.ResponseWriter, r *http.Request) {
  
    vars := mux.Vars(r)
    lang, kata := vars["language"], vars["kata"]
    
    d := "Hit stubHandler, lang = <" + lang + ">, kata = <" + kata + ">"
    fmt.Println(d)
    
    responseData := structs.StubResponse{
        Code: "You chose lang = " + lang,
        Tests: "You chose kata = " + kata}
        
    response, err := json.Marshal(responseData)
    if err != nil {
        fmt.Println("ERROR in json.Marshal")
    }
    w.Write([]byte(string(response)))
}

func runHandler(w http.ResponseWriter, r *http.Request) {
  
    lang := mux.Vars(r)["language"]
    
    d := "Hit runHandler, lang = <" + lang + ">"
    fmt.Println(d)
    w.Write([]byte(d))
}

func main() {
  
    r := mux.NewRouter()
    
    r.HandleFunc("/", pageHandler).
      Methods("GET")
      
    r.HandleFunc("/kata/{kata}/lang/{language}", stubHandler).
      Methods("GET")
      
    r.HandleFunc("/run/{language}", runHandler).
      Methods("POST")
     
    staticDir := "/home/ubuntu/workspace/src/github.com/gavincabbage/kodekata/app/static/"
    fileServer := http.FileServer(http.Dir(staticDir))
    r.PathPrefix("/static/").
      Handler(http.StripPrefix("/static/", fileServer))
    
    http.Handle("/", r)
    host := os.Getenv("IP") + ":" + os.Getenv("PORT")
    http.ListenAndServe(host, r)
}
