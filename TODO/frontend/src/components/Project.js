import React from 'react'


const ProjectItem = ({project}) => {
    return (
        <tr>
            <td>{project.name}</td>
            <td>{project.link}</td>
            <td>{project.description}</td>
            <td>{project.users}</td>
        </tr>
    )
}

const ProjectList = ({projects}) => {
    return (
        <table>
            <tr>
                <th>Name</th>
                <th>Link</th>
                <th>Description</th>
                <th>Users</th>
            </tr>
            {projects.map((project) => <ProjectItem project={project} />)}
        </table>
    )
}

export default ProjectList