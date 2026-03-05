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
                bat '"C:\\Users\\YashvanthVijayabalaj\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" -m pip install -r requirements.txt'
            }
        }

        stage('Python Test') {
            steps {
                bat '"C:\\Users\\YashvanthVijayabalaj\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" -c "print(\'Jenkins Python works\')"'
            }
        }

        stage('Run App Test') {
            steps {
                bat 'python -m pytest'
            }
        }

    }
}
