import React from 'react'


const TODOItem = ({TODO}) => {
    return (
        <tr>
            <td>{TODO.description}</td>
            <td>{TODO.created}</td>
            <td>{TODO.updated}</td>
            <td>{TODO.project}</td>
            <td>{TODO.user}</td>
            <td>{TODO.is_active}</td>
        </tr>
    )
}

const TODOList = ({TODOs}) => {
    return (
        <table>
            <tr>
                <th>Description</th>
                <th>Created</th>
                <th>Updated</th>
                <th>Project</th>
                <th>User</th>
                <th>Is_active</th>
            </tr>
            {TODOs.map((TODO) => <TODOItem TODO={TODO} />)}
        </table>
    )
}

export default TODOList