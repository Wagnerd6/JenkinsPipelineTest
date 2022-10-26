node {
    checkout scm
    
    stage('Build') {
        echo "Build stage"
        // Set up python
        sh 'sudo apt --yes install python3'
        sh 'python3 --version'
        sh 'sudo apt --yes install python3-pip'
        sh 'pip3 install pytest'
    }
    stage('Test') {
        echo "Test stage"
        sh 'pwd' 
        //sh 'python3 -m pytest'
    }
    stage('Deploy') {
        echo "Deploy stage"
    }
}
