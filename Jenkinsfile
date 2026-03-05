pipeline {
    agent any

    stages {

        stage('Check Python') {
            steps {
                bat 'python --version'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'python -m pip install --upgrade pip'
                bat 'python -m pip install -r requirements.txt'
            }
        }

        stage('Run Python Test') {
            steps {
                bat 'python -c "print(\'Jenkins Python works\')"'
            }
        }

        stage('Run App Tests') {
            steps {
                bat 'python -m pytest'
            }
        }

    }
}
