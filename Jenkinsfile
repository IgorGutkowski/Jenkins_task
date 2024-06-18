pipeline {
    agent any

    // Trigger the build when changes are committed to the repository
    triggers {
        pollSCMR('H/5 * * * *')  // Polls every 5 minutes; adjust as needed
    }

    stages {
        stage('Setup Environment') {
            steps {
                script {
                    // Check if Python3 is installed and install it if not
                    sh '''
                    if ! command -v python3 &> /dev/null; then
                        echo "Installing Python 3..."
                        sudo apt-get update
                        sudo apt-get install -y python3
                        sudo ln -sf /usr/bin/python3 /usr/bin/python
                    fi
                    python --version
                    '''
                }
            }
        }

        stage('Run Tests') {
            steps {
                // Run tests using Python
                sh 'python -m unittest test_calculator.py'
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
