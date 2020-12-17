#!groovy
import groovy.json.JsonSlurper
 /* Production Improvement: Run with Jenkins master slave configuration and run in a docker cluster. Specify agent for the docker slave. Multibranch pipeline in Jenkins*/
 /* Production Improvement: Run Jenkins with SSD backed storage */
 /* Production Improvement: Durability vs Performance trade off. Can enable Pipeline Speed/Durability setting in Jenkins. */
 /* Production Improvement: Use latest version of plugins. Used short python scripts for complex processes. Use garbage collection tuning options. */
pipeline {
  
  /* Production Improvement: Specify Options as buildDiscarder(logRotator(numToKeepStr: '30', artifactNumToKeepStr: '30')) to discard old builds*/
  agent any

  parameters {
    /* The below 3 parameters are of type booleanParm instead of Checkbox as it is not a multi option parameter. These are just yes/no type. 
    If Checkbox is needed, we can use Custom Checkbox Parameter Plugin, and configure Jenkins as 
    (checkboxParameter name:'my-checkbox', format:'JSON' , ## Provide Key value pairs in Json fomat)
    */
    booleanParam(
      name: 'Static_Check',
      defaultValue: false,
      description: 'Static_Check'
    )
    booleanParam(
      name: 'QA',
      defaultValue: false,
      description: 'QA'
    )
    booleanParam(
      name: 'Unit_Test',
      defaultValue: false,
      description: 'Unit_Test'
    )
    string(
      name: 'Success_Email',
      defaultValue: 'xyz@gmail.com',
      description: 'Success Email'
    )
    string(
      name: 'Failure_Email',
      defaultValue: 'xyz@gmail.com',
      description: 'Failure Email'
    )
    
  }

  stages {

    stage('Git Pull') {
            steps {
              checkout scm: [
                        $class: 'GitSCM',
                        branches: scm.branches,
                        doGenerateSubmoduleConfigurations: false,
                        extensions: [[$class: 'SubmoduleOption',
                                      disableSubmodules: false,
                                      parentCredentials: false,
                                      recursiveSubmodules: true,
                                      reference: '',
                                      trackingSubmodules: false]],
                        submoduleCfg: [],
                        userRemoteConfigs: scm.userRemoteConfigs
                ]
               
            }
        }  

    stage('Is the run required?') {
            steps{
               script {  
                /* In this code, the Rest call and subsequent actions are abstracted in a python script. If the REST call has to be made using a plugin,
                  we can use HTTP Request plugin and make call as below,
                  def response = httpRequest "https://calendarific.com/api/v2/holidays?&api_key=758f54db8c52c2b500c928282fe83af1b1aa2be8&country=IN&year=2020"
                  println('Status: '+response.status)
                  println('Response: '+response.content)
                   */ 
                echo 'Deciding if today is a holiday'
                is_holiday = sh(script: 'python3 run.py', returnStdout: true)
                is_holiday = is_holiday.toBoolean()
                  }
                }
            }
          

    stage('Build') {
            when {
                  expression { is_holiday  } 
               }            
            steps{
               script {     
                   /* Production Improvement: Stash files instead of archiving. If these are artifacts, better to store it in jfrog artifactory or Nexus */
                 echo 'Started Build stage'
                 sh "python3 build.py"
                 flag = false
                 flag = flag.toBoolean()
                 }
               }
            }
    
   stage('Quality'){
     parallel{  
       stage('QualityCheck'){
          stages{
            stage('Static_Check') {
               when {
                  expression { params.Static_Check  &&  is_holiday } 
               }                
                   steps{
                      script {  
                        /* Production Improvement: Stash files instead of archiving. If these are artifacts, better to store it in jfrog artifactory or Nexus */
                        echo 'Started Static Check stage'
                        sh "python3 quality.py"  
                        flag = true
                        flag = flag.toBoolean()
                        
                        }
                      }
                   }

          stage('QA') {
              when {
                  expression { params.QA  &&  is_holiday && flag } 
               }                                
                   steps{
                      script {     
                      /* Production Improvement: Stash files instead of archiving. If these are artifacts, better to store it in jfrog artifactory or Nexus */ 
                        echo 'Started QA stage'
                        sh "python3 quality.py" 
                        }
                      }
                   }
               }
           }
      stage('Unit_Test') {
            when {
                  expression { params.Unit_Test  &&  is_holiday } 
               }           
               steps{
                  script {     
                    /* Production Improvement: Stash files instead of archiving. If these are artifacts, better to store it in jfrog artifactory or Nexus */
                    echo 'Started Unit test stage'
                    sh "python3 quality.py"   
                     }
                  }
               }
         }
     }

    stage('Summary') {
            
            steps{
               script {     
                 //Have enabled Stage view plugin to give a better visualization of which stages are executed based on checkboxes enabled.
                 /* Production Improvement: For code coverage, test results better to use a tool like SonarQube and send reports of junit, jacoco to it.*/  
                  /* Production Improvement: Limit amount of data written to logs */
                 echo 'Summary with Stage view and logs of what file is copied is displayed on clicking the specific stage' 
                 }
               }
            }
   }

    post {
        always {
            echo 'Jenkins job finished'
        }
        success {
           /* Production Improvement: Detailed mail here listing out Job details in body of email */
            mail to: "${Success_Email}", subject: 'The Pipeline failed', body: "<b>Example</b><br>Project: ${env.JOB_NAME} <br>Build Number: ${env.BUILD_NUMBER} <br> URL de build: ${env.BUILD_URL}"
        }
        failure {
            mail to: "${Failure_Email}", subject: 'The Pipeline succeded', body: "<b>Example</b><br>Project: ${env.JOB_NAME} <br>Build Number: ${env.BUILD_NUMBER} <br> URL de build: ${env.BUILD_URL}"
        }
    }


         
    
  }
