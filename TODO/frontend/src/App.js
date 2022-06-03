import React from 'react';
import './App.css';
import UserList from './components/User.js'
import ProjectList from './components/Project';
import TODOList from './components/TODO';
import axios from 'axios'
import Menu from './components/Menu.js'
import Footer from './components/Footer.js'
import {BrowserRouter, Routes, Route} from 'react-router-dom'


class App extends React.Component {

    constructor(props) {
        super(props)
        this.state = {
            'users': [],
            'projects': [],
            'TODOs': []
        }
        console.log(this.state)
    }

    componentDidMount() {
        axios.get('http://127.0.0.1:8000/views/api-view')
            .then(response => {
                const users = response.data.results
                    this.setState(
                    {
                        'users': users
                    }
                )
            }).catch(error => console.log(error))
        
        axios.get('http://127.0.0.1:8000/api/Project')
            .then(response => {
                const projects = response.data.results
                    this.setState(
                    {
                        'projects': projects
                    }
                )
            }).catch(error => console.log(error))
        
        axios.get('http://127.0.0.1:8000/api/TODO')
            .then(response => {
                const TODOs = response.data.results
                    this.setState(
                    {
                        'TODOs': TODOs
                    }
                )
            }).catch(error => console.log(error))    
    }


    render () {
        return (
            <div className='App'>
                <BrowserRouter>
                    <Menu />
                        <Routes>
                            <Route path='/' element={<UserList users={this.state.users} />
                            } />
                            <Route path='/projects' element={<ProjectList projects={this.state.projects} />
                            } />
                            <Route path='/TODOs' element={<TODOList TODOs={this.state.TODOs} />
                            } />
                        </Routes>   
                    <Footer />     
                </BrowserRouter>
            </div>
        )
    }
}


export default App;