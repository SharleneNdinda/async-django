# 🍒 This application implements Asynchronous Task Processing with Django Q 🍒

```
Asynchronous processing is whereby a system does not wait for an execution step to be completed before moving on to the next step.
It allows systems calling external apis or resources to execute much faster than a normal synchronous call would.
```

### Running the Django server shows the task has been queued for processing.

![alt text](async_django/img/Screenshot%20from%202023-05-24%2008-51-08.png "Log one")

### The Django-Q server receives the task and executes after a 10 second delay

![alt text](async_django/img/Screenshot%20from%202023-05-24%2008-51-50.png "Log two")

```
The application immediately returns a response once the endpoint is called forwarding the task to th
django-q server this helps in offloading long running tasks that slow down the server.
```
