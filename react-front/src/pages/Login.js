import { useContext } from "react"
import AuthContext from "../context/AuthContext"

export default function Login(){
    let {login} = useContext(AuthContext)

    return <div>
        <form onSubmit={login}>
            <input type="text" name="username" placeholder="Username"></input>
            <input type="password" name="password" placeholder="Password"></input>
            <input type="submit" value="Login"></input>
        </form>
    </div>
}