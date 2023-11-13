import jenkins


server = jenkins.Jenkins("http://localhost:8080", username="fennaneo", password="*********")

job2_xml = open("hello-world.xml", mode='r', encoding='utf-8').read()
server.create_job("job2", job2_xml)

jobs = server.get_jobs()

print(jobs)
