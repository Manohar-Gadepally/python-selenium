pipeline {
    agent any
    parameters {
        string(name: 'PYTEST_MARKER', defaultValue: 'smoke', description: 'smoke tests')
    }
    stages {
        stage('Setup') {
            steps {
                script {
                    echo 'Setting up Python virtual environment...'
                    sh '''
                        python3 -m venv venv
                        source venv/bin/activate
                    '''
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    echo 'Installing dependencies...'
                    sh '''
                        source venv/bin/activate
                        pip install -r requirements.txt
                    '''
                }
            }
        }

        stage('Run Pytest') {
            steps {
                script {
                    echo 'Running Pytest...'
                    sh '''
                        source venv/bin/activate
                        pytest -m ${env.PYTEST_MARKER}
                    '''
                }
            }
        }
    }
}
