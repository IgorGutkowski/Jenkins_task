pipeline {
    agent none  // This specifies that no global agent will be used
    stages {
        stage('Build') {
            agent {
                docker { 
                    image 'python:3.10' 
                    args '-v /var/run/docker.sock:/var/run/docker.sock' // This is crucial if you need Docker commands within the Docker agent
                }
            }
            steps {
                sh 'python --version'
                sh 'docker --version'  // To check if docker command can be run
            }
        }
    }
}
