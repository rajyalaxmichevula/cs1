pipeline {
    agent any

    environment {
        // Optional: specify Python version or virtual environment
        VENV_DIR = "venv"
    }

    stages {
        stage('Setup') {
            steps {
                echo "Setting up Python environment..."
                // Create virtual environment
                sh 'python3 -m venv $VENV_DIR'
                // Activate venv and upgrade pip
                sh '''
                source $VENV_DIR/bin/activate
                pip install --upgrade pip
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                echo "Installing Python dependencies..."
                sh '''
                source $VENV_DIR/bin/activate
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                echo "Running unit tests..."
                sh '''
                source $VENV_DIR/bin/activate
                python -m unittest discover tests
                '''
            }
        }

        stage('Run Application') {
            steps {
                echo "Starting Flask app..."
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
            echo "Build succeeded!"
        }
        failure {
            echo "Build failed."
        }
    }
}
