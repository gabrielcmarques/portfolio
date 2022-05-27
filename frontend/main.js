// EXEMPLO DE COMO FICARIA A IMPLEMENTAÇÃO DA API EM FRONTEND

let loginBtn = document.getElementById('login-btn')
let logoutBtn = document.getElementById('logout-btn')

let token = localStorage.getItem('token')

if (token) {
    loginBtn.remove()
} else {
    logoutBtn.remove()
}

logoutBtn.addEventListener('click', (e) => {
    e.preventDefault()
    localStorage.removeItem('token')
    window.location = 'file:///D:/Gabriel/Desktop/portfolio_gabrielcmarques/frontend/login.html'
})

let projectsUrl = 'http://127.0.0.1:8000/api/projetos/'

let getProjects = () => {

    fetch(projectsUrl)
        .then(response => response.json())
        .then(data => {
            console.log(data)
            buildProjects(data)
    })
}

let buildProjects = (projects) => {
    let projectsWrapper = document.getElementById('projects--wrapper')

    for (let i = 0; projects.length > i; i++) {
        let project = projects[i]
        
        let projectCard = `
                <div class="project--card">
                    <img src="http://127.0.0.1:8000${project.thumbnail}" />
                    <div>
                        <div class="card--header">
                            <h3>${project.nome}</h3>
                            <strong class="vote--option" data-vote="up" data-project="${project.id}" ></strong>
                            <strong class="vote--option" data-vote="down" data-project="${project.id}"  ></strong>
                        </div>                    
                        <p>${project.descricao.substring(0, 150)}</p>
                    </div>
                </div>
        `
        projectsWrapper.innerHTML += projectCard

    }
}

getProjects()