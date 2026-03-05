pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'develop',
                url: 'https://github.com/thisisyashvanth/Task-Management.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run App Test') {
            steps {
                bat 'python -m pytest'
            }
        }
    }
}
