
import './App.css';
import { BrowserRouter as Router, Route, Routes, redirect } from 'react-router-dom';
import HomePage from './pages/HomePage';
import Login from './pages/Login';
import Header from './components/Header';
import NotFound from './pages/NotFound';
import Todos from './pages/Todos';
import { AuthProvidor } from './context/AuthContext';

function App() {
  const authenticated = false
  return (
    <>
    <AuthProvidor>
        <Header/>
        <Routes>
          <Route path='/' exact element={<HomePage/>} />
          <Route path='/login' element={<Login/>} />
          <Route auth={authenticated} path='/todos' element={<Todos/>} />
          <Route path='*' element={<NotFound/>} />
        </Routes>
    </AuthProvidor>

      </>
  );
}

export default App;
