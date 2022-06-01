import React from 'react';
import './App.css';
import UserList from './components/User.js'
import axios from 'axios'
import Menu from './components/Menu.js'
import Footer from './components/Footer.js'
/* import {HashRouter, Route} from 'react-router-dom' */


class App extends React.Component {

    constructor(props) {
        super(props)
        this.state = {
            'users': [],
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
    }


    render () {
        return (
            <div>
                <Menu />
                <UserList users={this.state.users} />
                <Footer />
            </div>

        )
    }
}


export default App;