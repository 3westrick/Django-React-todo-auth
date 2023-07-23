import { Link } from "react-router-dom";
import { useContext } from "react";
import AuthContext from "../context/AuthContext";

export default function Header({auth}){
    let {user, logout} = useContext(AuthContext)
    return <div>
        <Link to="/">Home</Link>
        <span> | </span>
        {user ? (
            <a onClick={logout} href="#">Logout</a>
        ):
        (
            <Link to="/login">Login</Link>
        )}
        <span> | </span>
        <Link to="/todos">Todos</Link>
        {user && <p>Hello {user.username}</p>}
        <hr></hr>
    </div>
}