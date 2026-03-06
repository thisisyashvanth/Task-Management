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

        stage('Create Env File') {
            steps {
                bat '''
                echo DB_USER=root > .env
                echo DB_PASSWORD=this1sMeY%%40sh >> .env
                echo DB_HOST=localhost >> .env
                echo DB_PORT=3306 >> .env
                echo DB_NAME=tasks >> .env
                '''
            }
        }

        stage('Check App Imports') {
            steps {
                bat 'python -c "import main"'
            }
        }
        
        // stage('Run FastAPI') {
        //     steps {
        //         bat 'uvicorn main:app --host 0.0.0.0 --port 8000'
        //     }
        // }
    }
}
