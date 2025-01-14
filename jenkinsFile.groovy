pipeline {
    agent any
    parameters {
        string(name: 'PYTEST_MARKER', defaultValue: 'smoke', description: 'Marker for pytest')
    }
    stages {
        stage('Setup') {
            steps {
                script {
                    echo 'Setting up Python virtual environment...'
                    bat "python -m venv venv"
                    echo 'Initializing venv...'
                    bat "venv\\Scripts\\activate.bat"
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    echo 'Initializing venv...'
                    bat "venv\\Scripts\\activate.bat"
                    echo 'Installing dependencies...'
                    bat "pip install -r requirements.txt"
                }
            }
        }

        stage('Run Pytest') {
            steps {
                script {
                    echo 'Initializing venv...'
                    bat "venv\\Scripts\\activate.bat"
                    echo 'Running Pytest...'
                    bat "pytest -m %PYTEST_MARKER%"
                }
            }
        }
    }
}