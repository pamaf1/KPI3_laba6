from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    wait_time = between(5, 20)
    host = 'https://reqres.in/api'


    @task(10)
    def addUser(self):
        self.client.post("/users", json={
            "name": "Alyosha",
            "job": "study"
        })

    @task(9)
    def registerNewUser(self):
        self.client.post("/register", json={
            "email": "eve.holt@reqres.in",
            "password": "pistol"
        })

    @task(8)
    def loginUser(self):
        self.client.post("/login", json={
            "email": "eve.holt@reqres.in",
            "password": "cityslicka"
        })

    @task(5)
    def getListOfUsers(self):
        self.client.get("/users?page=1")

    @task(5)
    def getById(self):
        self.client.get("/users/2")

    @task(6)
    def updateUser(self):
        self.client.put("/users/1", json={
            "name": "Mikola",
            "job": "watching"
        })
