import React from 'react'
import './App.css'
import UserList from './components/User.js'
import ProjectList from './components/Project'
import TODOList from './components/TODO'
import axios from 'axios'
import Menu from './components/Menu.js'
import Footer from './components/Footer.js'
import LoginForm from './components/Auth.js'
import {BrowserRouter, Routes, Route, Link} from 'react-router-dom'
import Cookies from 'universal-cookie'


const client = axios.create(
    {baseURL: 'http://127.0.0.1:8000/api/'}
)

class App extends React.Component {

    constructor(props) {
        super(props)
        this.state = {
            'users': [],
            'projects': [],
            'TODOs': [],
            'token': ''
        }
    }

    set_token(token) {
        const cookies = new Cookies()
        cookies.set('token', token)
        this.setState({ 'token': token }, () => this.load_data())
    }

    is_authenticated() {
        return this.state.token !== ''
    }

    logout() {
        this.set_token('')
    }

    get_token_from_storage() {
        const cookies = new Cookies()
        const token = cookies.get('token')
        this.setState({ 'token': token }, () => this.load_data())
    }

    get_token(username, password) {
        axios.post('http://127.0.0.1:8000/api-token-auth/', { username: username, password: password }).then(response => {
            this.set_token(response.data.token)
            // console.log(response.data)
        }).catch(error => alert('Неверный логин или пароль!'))
    }

    get_headers() {
        let headers = {
            'Content-Type': 'application/json'
        }
        if (this.is_authenticated()) {
            headers['Authorization'] = 'Token' + this.state.token
        }
        return headers
    }

    load_data() {

        const headers = this.get_headers()
        axios.get('http://127.0.0.1:8000/views/api-view/', { headers })
            .then(response => {
                this.setState({ users: response.data })
            }).catch(error => console.log(error))
        
        client.get('Project/', { headers })
            .then(response => {
                this.setState({ projects: response.data })
            }).catch(error => console.log(error))    
        
        client.get('TODO/', { headers })
            .then(response => {
                this.setState({ TODOs: response.data })
            }).catch(error => console.log(error))    
    }

    componentDidMount() {
        this.get_token_from_storage()
    }


    render () {
        return (
            <div className='App'>
                <BrowserRouter>
                    <Menu />
                    <nav>
                        <ul>
                            <li>
                                <Link to='/'>Users</Link>
                            </li>
                            <li>
                                <Link to='/projects'>Projects</Link>
                            </li>
                            <li>
                                <Link to='/TODOs'>TODOs</Link>
                            </li>
                            <li>
                                {this.is_authenticated() ? <button onClick={() => this.logout()}>Logout</button> :
                                <Link to='/login'>Login</Link>}
                            </li>
                        </ul>
                    </nav>
                        <Routes>
                            <Route path='/' element={<UserList users={this.state.users} />
                            } />
                            <Route path='/projects' element={<ProjectList projects={this.state.projects} />
                            } />
                            <Route path='/TODOs' element={<TODOList TODOs={this.state.TODOs} />
                            } />
                            <Route path='/login' element={<LoginForm get_token={(username, password) => this.get_token(username, password)} /> 
                            } />
                        </Routes> 
                    <Footer />     
                </BrowserRouter>
            </div>
        )
    }
}


export default App;