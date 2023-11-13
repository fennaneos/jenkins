import jenkins


server = jenkins.Jenkins("http://localhost:8080", username="fennaneo", password="*********")

server.create_job("job1", jenkins.EMPTY_CONFIG_XML)

jobs = server.get_jobs()

print(jobs)