from google.adk.agents import Agent
import requests

def get_path(path: str) -> dict:
    """Retrieves data from whereami based on the path indicated by the user.

    Args:
        path (str): The name of the path to retrieve from the whereami service.

    Returns:
        dict: status and result or error msg.
    """

    url = "https://frontend.endpoints.e2m-private-test-01.cloud.goog"

    try:
        response = requests.get(url + "/" + path)
        response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)
        return {
            "status": "success",
            "report": (
                response.text
            ),
        }
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return {
            "status": "error",
            "error_message": f"Path information for '{path}' is not available.",
        }

root_agent = Agent(
    name="whereami_agent",
    model="gemini-2.0-flash",
    description=(
        "Agent to answer questions about the whereami service in terms of path."
    ),
    instruction=(
        "You are a helpful agent who can answer user questions about the whereami service."
    ),
    tools=[get_path],
)