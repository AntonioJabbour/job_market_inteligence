import os
import requests
from dotenv import load_dotenv
from src.utils.logger import get_logger

load_dotenv()

logger = get_logger(__name__)


def fetch_jobs_from_api(search_query, page=1, num_pages=1):

    logger.info(f"Fetching jobs from JSearch API for query: {search_query}")

    api_key = os.getenv("JSEARCH_API_KEY")

    if not api_key:
        logger.error("JSEARCH_API_KEY was not found in the environment variables.")
        return []

    url = "https://jsearch.p.rapidapi.com/search"

    headers = {
        "X-RapidAPI-Key": api_key,
        "X-RapidAPI-Host": "jsearch.p.rapidapi.com"
    }

    params = {
        "query": search_query,
        "page": str(page),
        "num_pages": str(num_pages)
    }

    try:
        logger.info("Sending request to JSearch API...")
        response = requests.get(url, headers=headers, params=params, timeout=30)

        logger.info(f"Response status code: {response.status_code}")

        if response.status_code != 200:
            logger.error(f"API request failed with status code {response.status_code}")
            logger.error(f"Response text: {response.text}")
            return []

        response_json = response.json()
        jobs = response_json.get("data", [])

        if not jobs:
            logger.warning(f"No jobs were returned for query: {search_query}")
            return []

        logger.info(f"Successfully fetched {len(jobs)} job(s) for query: {search_query}")
        return jobs

    except requests.exceptions.RequestException as e:
        logger.error(f"Request error while calling JSearch API: {e}")
        return []

    except ValueError as e:
        logger.error(f"Failed to parse JSON response: {e}")
        return []

    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        return []