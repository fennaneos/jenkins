
###### hp@hp-HP-EliteBook-830-G5:~/jenkins$ which python3
/opt/intel/oneapi/intelpython/latest/bin/python3
###### hp@hp-HP-EliteBook-830-G5:~/jenkins$ python3 -m venv venv
###### hp@hp-HP-EliteBook-830-G5:~/jenkins$ source venv/bin/activate
###### (venv) hp@hp-HP-EliteBook-830-G5:~/jenkins$ which python
/home/hp/jenkins/venv/bin/python
###### (venv) hp@hp-HP-EliteBook-830-G5:~/jenkins$ which pip
/home/hp/jenkins/venv/bin/pip
###### (venv) hp@hp-HP-EliteBook-830-G5:~/jenkins$ pip freeze > requirements.txt
###### (venv) hp@hp-HP-EliteBook-830-G5:~/jenkins$ cat requirements.txt
###### (venv) hp@hp-HP-EliteBook-830-G5:~/jenkins$ pip install python-jenkins
Collecting python-jenkins
  Using cached python_jenkins-1.8.2-py3-none-any.whl (29 kB)
Collecting multi-key-dict
  Using cached multi_key_dict-2.0.3.tar.gz (8.4 kB)
Collecting requests
  Using cached requests-2.31.0-py3-none-any.whl (62 kB)
Collecting six>=1.3.0
  Using cached six-1.16.0-py2.py3-none-any.whl (11 kB)
Collecting pbr>=0.8.2
  Using cached pbr-6.0.0-py2.py3-none-any.whl (107 kB)
Collecting certifi>=2017.4.17
  Using cached certifi-2023.7.22-py3-none-any.whl (158 kB)
Collecting charset-normalizer<4,>=2
  Using cached charset_normalizer-3.3.2-cp37-cp37m-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (136 kB)
Collecting urllib3<3,>=1.21.1
  Using cached urllib3-2.0.7-py3-none-any.whl (124 kB)
Collecting idna<4,>=2.5
  Using cached idna-3.4-py3-none-any.whl (61 kB)
Using legacy setup.py install for multi-key-dict, since package 'wheel' is not installed.
Installing collected packages: multi-key-dict, certifi, charset-normalizer, urllib3, idna, requests, six, pbr, python-jenkins
    Running setup.py install for multi-key-dict ... done
Successfully installed certifi-2023.7.22 charset-normalizer-3.3.2 idna-3.4 multi-key-dict-2.0.3 pbr-6.0.0 python-jenkins-1.8.2 requests-2.31.0 six-1.16.0 urllib3-2.0.7
###### (venv) (base) hp@hp-HP-EliteBook-830-G5:~/jenkins$ pip freeze > requirements.txt 
###### (venv) (base) hp@hp-HP-EliteBook-830-G5:~/jenkins$ cat requirements.txt 
certifi==2023.7.22
charset-normalizer==3.3.2
idna==3.4
multi-key-dict==2.0.3
pbr==6.0.0
python-jenkins==1.8.2
requests==2.31.0
six==1.16.0
urllib3==2.0.7


## output main.py
(venv) (base) hp@hp-HP-EliteBook-830-G5:~/jenkins$ python main.py 
Hello Fennane Oussama from Jenkins 2.414.3

## output create_empty_job.py
(venv) (base) hp@hp-HP-EliteBook-830-G5:~/jenkins$ python create_empty_job.py 
[{'_class': 'hudson.model.FreeStyleProject', 'name': 'hello-world', 'url': 'http://localhost:8080/job/hello-world/', 'color': 'blue', 'fullname': 'hello-world'}, {'_class': 'hudson.model.FreeStyleProject', 'name': 'job1', 'url': 'http://localhost:8080/job/job1/', 'color': 'notbuilt', 'fullname': 'job1'}]


## output create_job_from_xml.py
[{'_class': 'hudson.model.FreeStyleProject', 'name': 'hello-world', 'url': 'http://localhost:8080/job/hello-world/', 'color': 'blue', 'fullname': 'hello-world'}, {'_class': 'hudson.model.FreeStyleProject', 'name': 'job1', 'url': 'http://localhost:8080/job/job1/', 'color': 'notbuilt', 'fullname': 'job1'}, {'_class': 'hudson.model.FreeStyleProject', 'name': 'job2', 'url': 'http://localhost:8080/job/job2/', 'color': 'notbuilt', 'fullname': 'job2'}]

# jenkins
