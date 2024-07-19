from hera.workflows import Steps, Workflow, script
from hera.shared import global_config

global_config.host = "https://localhost:2746"
global_config.token = ""  # Copy token value after "Bearer" from the `argo auth token` command
global_config.image = "python:3.12.4-slim"  # Set the image if you cannot access "python:3.8" via Docker Hub
global_config.verify_ssl = False  # Set to False if you are using a self-signed certificate


@script()
def echo(message: str):
    print(message)


with Workflow(
    generate_name="hello-world-verify-ssl-false-",
    entrypoint="steps",
    namespace="argo",
) as w:
    with Steps(name="steps"):
        echo(arguments={"message": "Hello world!"})


if __name__ == "__main__":

    w.create()
