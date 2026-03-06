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
                bat 'python -m pip install -r requirements.txt'
            }
        }
        
        stage('Run FastAPI') {
            steps {
                bat 'uvicorn main:app --host 0.0.0.0 --port 8000'
            }
        }
    }
}
