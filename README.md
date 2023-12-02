# aws-sam-pdf-compressor

A serverless solution to compress PDF files loss lessly. The compression doesn't reduces the file size significantly as PDF files are already compressed to an extent. 

This solution uses AWS SAM toolkit for ease and rapid deployments in a truely agile way.


## To Deploy
- Make sure the pre-requisites toolkits are installed for SAM projects.
    - https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/prerequisites.html
- Create a python3 virtual env
- install the python packages in the `requirements.txt`
- Execute `sam build`
- Finally `sam deploy --guided`. Guided deployment is for the first run. You will not be required to specify this in the subsequent runs
