pipeline {
    agent any

    stages {

        stage('Clone Repository') {
            steps {
                git branch: 'develop',
                git 'https://github.com/thisisyashvanth/Task-Management'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'python -m pip install --upgrade pip'
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run FastAPI Server') {
            steps {
                bat 'uvicorn main:app --host 127.0.0.1 --port 8000'
            }
        }

    }
}
