/* Requires the Docker Pipeline plugin */ 
node {
    checkout scm
    
    stage('Build') {
        echo "Build stage"
        sh 'python3 --version'
    }
    stage('Test') {
        echo "Test stage"
    }
    stage('Deploy') {
        echo "Deploy stage"
    }
}
