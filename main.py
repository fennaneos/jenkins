import jenkins


server = jenkins.Jenkins("http://localhost:8080", username="fennaneo", password="*********")

user = server.get_whoami()

version = server.get_version()

print("Hello %s from Jenkins %s" % (user['fullName'], version))