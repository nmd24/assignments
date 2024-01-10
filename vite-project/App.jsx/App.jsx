import React, {Fragment} from "react"
import {useState} from "react"

function App(){
    const [title , setTitle] = useState("my name is nikhil");
    return(
    <div>
        <Header title = "nikhil1"></Header>
        <Header title = "nikhil2"></Header>
    </div>
    )
}

function Header({title}){
    return <div>
    {title}
    </div>
}

export default App