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
                    bat "pytest --alluredir=./allure_results -m %PYTEST_MARKER%"
                }
            }
            post {
                always {
                    allure includeProperties: false, jdk: '', results: [[path: './allure-results']]
                }
            }
        }
    }
}