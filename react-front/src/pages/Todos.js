import { useContext, useEffect, useState } from "react";
import { Link, Navigate, redirect } from "react-router-dom";
import AuthContext from "../context/AuthContext";
import jwt_decode from "jwt-decode";

export default function Todos(){
    let {user, token, logout} = useContext(AuthContext)
    const [todos, setTodos] = useState([])

    useEffect(()=>{
        if (user)
            get_todos()
    },[])
    async function get_todos(){
        let response = await fetch('http://127.0.0.1:8000/api/v1/todos/', {
            method:'GET',
            headers:{
                'Content-Type': 'application/json',
                'Authorization' : `Bearer ${String(token.access)}`  
            }
        })
        let data = await response.json()
        if (response.status == 200)
        setTodos(data)
        else logout()
    }

    async function toggle_done(todo){
        let res = await fetch(`http://127.0.0.1:8000/api/v1/todos/${todo.id}/update/`, {
            method:'PUT',
            headers:{
                'Content-Type': 'application/json',
                'Authorization' : `Bearer ${String(token.access)}`  
            },
            body: JSON.stringify({
                'done': ! todo.done
            })
            
        })
        if (res.status == 200)
        get_todos()
    }

    if (user)
    return <div>
        <h1>Todos</h1>
        <ul>
            {todos.map(todo => <li key={todo.id}><span>{todo.title}</span> <button onClick={()=>toggle_done(todo)}>{todo.done? 'undone' : 'done'}</button></li>)}
        </ul>
        </div>
    return <Navigate to="/login"/>
}