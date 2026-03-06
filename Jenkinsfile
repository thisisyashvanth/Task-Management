pipeline {
    agent any

    stages {

        stage('Install Dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }
        
        stage('Run FastAPI') {
            steps {
                bat 'uvicorn main:app --host 0.0.0.0 --port 8000'
            }
        }
    }
}
