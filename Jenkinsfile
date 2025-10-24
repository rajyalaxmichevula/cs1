pipeline {
    agent any

    environment {
        VENV_DIR = "venv"
        GIT_CREDENTIAL_ID = "github-token" // Replace with your actual Jenkins credential ID
    }

    stages {
        stage('Checkout Code') {
            steps {
                // Use credentials for private Git repo
                git url: 'https://github.com/your-username/pictionary-app.git', credentialsId: "${GIT_CREDENTIAL_ID}"
            }
        }

        stage('Setup Python Environment') {
            steps {
                echo "Creating virtual environment..."
                sh 'python3 -m venv $VENV_DIR'
                sh '''
                source $VENV_DIR/bin/activate
                pip install --upgrade pip
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                echo "Installing dependencies..."
                sh '''
                source $VENV_DIR/bin/activate
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Unit Tests') {
            steps {
                echo "Running unit tests..."
                sh '''
                source $VENV_DIR/bin/activate
                python -m unittest discover tests
                '''
            }
        }

        stage('Run Flask App') {
            steps {
                echo "Starting Flask application..."
                // Run Flask in background
                sh '''
                source $VENV_DIR/bin/activate
                nohup python app.py &
                '''
            }
        }
    }

    post {
        always {
            echo "Pipeline finished."
        }
        success {
            echo "Build and tests succeeded!"
        }
        failure {
            echo "Pipeline failed."
        }
    }
}
