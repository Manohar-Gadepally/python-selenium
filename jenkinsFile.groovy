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
                    bat '''
                        python -m venv venv
                        venv\\Scripts\\activate.bat
                    '''
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    echo 'Installing dependencies...'
                    bat '''
//                         venv\\Scripts\\activate.bat
                        pip install -r requirements.txt
                    '''
                }
            }
        }

        stage('Run Pytest') {
            steps {
                script {
                    echo 'Running Pytest...'
                    bat '''
//                         venv\\Scripts\\activate.bat
                        pytest
                    '''
                }
            }
        }
    }
}