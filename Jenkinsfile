pipeline {
    agent {
        docker {
            image 'python:3.10'  
        }
    }

    triggers {
        pollSCM('H/15 * * * *')  
    }

    stages {
        stage('Run Tests') {
            steps {
                sh 'python -m unittest test_calculator.py'  
            }
        }
    }

    post {
        success {
            echo 'Build succeeded.'
        }
        failure {
            echo 'Build failed.'
        }
    }
}
