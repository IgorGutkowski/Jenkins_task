pipeline {
    agent any

    triggers {
        pollSCM('H/5 * * * *') 
    }

    stages {
        stage('Setup Environment') {
            steps {
                script {
                
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
