package main

import (
    "os"
    "fmt"
    "net/http"
    "github.com/gorilla/mux"
    "html/template"
)

type PageValues struct {
    Value string
}

func pageHandler(w http.ResponseWriter, r *http.Request) {
    
    t, err := template.ParseFiles("/home/ubuntu/workspace/src/github.com/gavincabbage/kodekata/app/templates/base.html")
    if err != nil {
        w.Write([]byte("Error while parsing template"))
    }
    
    val := "HELLO_I_AM_A_TEST_VALUE"
    vals := PageValues{Value: val}
    t.Execute(w, vals)
}

func stubHandler(w http.ResponseWriter, r *http.Request) {
  
    vars := mux.Vars(r)
    lang, kata := vars["language"], vars["kata"]
    
    d := "Hit stubHandler, lang = <" + lang + ">, kata = <" + kata + ">"
    fmt.Println(d)
    w.Write([]byte(d))
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
      
    r.HandleFunc("/stubs/{language}/kata/{kata}", stubHandler).
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


// package main

// import (
//   "encoding/json"
//   "net/http"
// )

// func main() {
//   http.HandleFunc("/foo", foo)
//   http.HandleFunc("/bar", bar)
//   http.ListenAndServe(":3000", nil)
// }

// func foo(w http.ResponseWriter, r *http.Request) {
//   w.Header().Set("Server", "A Go Web Server")
//   w.WriteHeader(200)
// }

// type Profile struct {
//   Name    string
//   Hobbies []string
// }

// func bar(w http.ResponseWriter, r *http.Request) {
//   profile := Profile{"Alex", []string{"snowboarding", "programming"}}

//   js, err := json.Marshal(profile)
//   if err != nil {
//     http.Error(w, err.Error(), http.StatusInternalServerError)
//     return
//   }

//   w.Header().Set("Content-Type", "application/json")
//   w.Write(js)
// }