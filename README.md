# A Simple Python Flask Backend app on Cloud Foundry
This is a simple backend Flask application that shows how apps on CloudFoundry works.

## Prerequisites
Apply for an Cloud Foundry account by signing up for a free trial at  [Pivotal Web Services](http://run.pivotal.io).

Install the [CF CLI](https://console.run.pivotal.io/tools) according to the OS you're using.

## Files

The Python buildpack requires extra configuration files below:
*   Procfile

	This file specifies the command to start the app.

*   requirements.txt

	This file illustrates the additional python packages not included by the buildpack by default.

*   runtime.txt

	This file is to specify the python runtime, eg, python-2.7.10. 

## How to deploy the python web apps
Open the command prompt and login the CF 
```bash
cf login -a api.run.pivotal.io 
```
Download the sample project
```bash
git clone https://github.com/ichbinblau/cf-flask-test.git
```
Upload the project to CF. I was unable to use the auto detected python buildpack provided by CF here thereby specifying another working buildpack by -b.   
```bash
cd cf-flask-test
cf push flask-test-theresa -b https://github.com/cloudfoundry/cf-buildpack-python.git -m 128m -i 1  
```
At the end of the execution, you will see messages below and are able to access the app by the url [flask-test-theresa.cfapps.io](http://flask-test-theresa.cfapps.io)
```bash
requested state: started
instances: 1/1
usage: 128M x 1 instances
urls: flask-test-theresa.cfapps.io
last uploaded: Thu Nov 12 05:21:11 UTC 2015
stack: cflinuxfs2
buildpack: https://github.com/cloudfoundry/cf-buildpack-python.git
```
If the upload fails, you may check the error the command:
```bash
cf logs flask-test-theresa --recent
```

## How to scale it?
You may scale the app horizontally by simply increasing the number of instances. Incoming requests to your application are automatically load balanced across all instances of your application, and each instance handles tasks in parallel with every other instance.
```bash
cf scale flask-test-theresa -i 6
```
Check the app health status, and you will see that there are 6 instances are up and running now. 
```bash
cf app flask-test-theresa
```

## Create and bind mysql database
Run the below commands to create a cf db service and bind it with the web app
```bash
cf create-service cleardb spark flask-test-db   // creates a ClearDB MySQL service
cf bind-service flask-test-theresa flask-test-db
```

## Test the database connection
Add database operation logics in hello.py, and test by accessing [flask-test-theresa.cfapps.io/users](http://flask-test-theresa.cfapps.io/users)
```python
def get_user():
    initial_db()
    u = User('theresa', 'theresa.shan@xxx.com')
    db_session.add(u)
    db_session.commit()
    return 'The first user is ' + db_session.query(User).first().name
```

## Reference
https://docs.cloudfoundry.org/devguide/deploy-apps/cf-scale.html





