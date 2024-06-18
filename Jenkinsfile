pipeline {
    agent any

    triggers {
        pollSCM('* * * * *')  // Polls SCM every minute; adjust as needed for less frequent checks.
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm  // Checks out source code from the configured SCM repository
            }
        }

        stage('Test') {
            steps {
                sh 'python3 -m unittest test_calculator.py'
            }
        }
    }

    post {
        always {
            echo 'This will always run'
        }
        success {
            echo 'Build was a success!'
        }
        failure {
            echo 'Build failed!'
        }
    }
}
