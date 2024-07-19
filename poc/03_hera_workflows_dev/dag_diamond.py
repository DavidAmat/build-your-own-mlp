from hera.workflows import DAG, Resources, WorkflowTemplate, script
from hera.shared import global_config
import os

ARGO_HOST = "https://localhost:2746"
global_config.host = ARGO_HOST  # "https://<your-host-name>"


@script(resources=Resources(cpu_request=0.1, cpu_limit=0.5, memory_request="0.3Gi", memory_limit="0.5Gi"))
def echo(message: str):
    """
    Echoes the given message.

    Parameters
    ----------
    message : str
        The message to be echoed.

    Returns
    -------
    None
        This function does not return anything.
    """
    print(message)


def pipeline(inputs: dict) -> DAG:
    """
    Create a diamond-shaped DAG.

    Returns
    -------
    DAG
        The diamond-shaped DAG.

    Notes
    -----
    This function creates a DAG with 5 nodes (A, B, C, D, E) forming a diamond shape.
    The nodes are connected in the following way:
    - A is connected to both B and C
    - B and C are connected to D
    - D is connected to E
    """
    with DAG(name="diamond", inputs=inputs):
        A = echo(name="A", arguments={"message": "A"})
        B = echo(name="B", arguments={"message": "B"})
        C = echo(name="C", arguments={"message": "C"})
        D = echo(name="D", arguments={"message": "D"})
        E = echo(name="E", arguments={"message": "E"})

        A >> [B, C] >> D >> E


if __name__ == "__main__":
    with WorkflowTemplate(
        name="dag-diamond-",
        entrypoint="diamond",
        namespace="argo",
    ) as wt:
        pipeline(inputs={"test": 1})

    wt.create_as_workflow(generate_name="dag-diamond-")
