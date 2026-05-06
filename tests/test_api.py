import os
import json
import requests
from dotenv import load_dotenv
from src.utils.logger import get_logger

# Load environment variables from .env
load_dotenv()

logger = get_logger(__name__)


def test_jsearch_api_structure():
    logger.info("Starting JSearch API structure test...")

    # Read API key from environment
    api_key = os.getenv("JSEARCH_API_KEY")

    if not api_key:
        logger.error("RAPIDAPI_KEY was not found in the environment variables.")
        return

    # JSearch search endpoint
    url = "https://jsearch.p.rapidapi.com/search"

    # Required RapidAPI headers
    headers = {
        "X-RapidAPI-Key": api_key,
        "X-RapidAPI-Host": "jsearch.p.rapidapi.com"
    }

    # Query parameters
    params = {
        "query": "Data scientist",
        "page": "1",
        "num_pages": "1"
    }

    try:
        logger.info("Sending request to JSearch API...")
        response = requests.get(url, headers=headers, params=params, timeout=30)

        logger.info(f"Response status code: {response.status_code}")

        # Check if request succeeded
        if response.status_code != 200:
            logger.error(f"API request failed with status code {response.status_code}")
            logger.error(f"Response text: {response.text}")
            return

        # Convert response to JSON
        response_json = response.json()

        # Extract the data list
        jobs = response_json.get("data", [])

        if not jobs:
            logger.warning("No jobs were returned in the API response.")
            return

        # Get only the first job object
        first_job = jobs[0]

        logger.info("Successfully retrieved the first job object.")
        print(json.dumps(first_job, indent=4, ensure_ascii=False))

    except requests.exceptions.RequestException as e:
        logger.error(f"Request error while calling JSearch API: {e}")

    except ValueError as e:
        logger.error(f"Failed to parse JSON response: {e}")

    except Exception as e:
        logger.error(f"Unexpected error: {e}")


if __name__ == "__main__":
    test_jsearch_api_structure()