from locust import HttpUser, task

class IrisApiUser(HttpUser):
    @task
    def health(self):
        self.client.get("/health")

