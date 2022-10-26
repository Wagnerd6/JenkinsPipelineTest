/* Requires the Docker Pipeline plugin */ 
node {
    checkout scm
    
    stage('Build') {
        echo "Build stage"
        // Set up python
        sh 'sudo apt --yes install python3'
        sh 'python3 --version'
        sh 'sudo apt --yes install python3-pip' 
    }
    stage('Test') {
        echo "Test stage"
    }
    stage('Deploy') {
        echo "Deploy stage"
    }
}
