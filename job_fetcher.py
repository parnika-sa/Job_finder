# =============================================
# job_fetcher.py - Adzuna API se jobs fetch karna
# =============================================

import requests
from config import APP_ID, APP_KEY, SEARCH_LOCATIONS, SEARCH_KEYWORDS, MAX_RESULTS_PER_SEARCH

def fetch_jobs():
    """
    Adzuna API se jobs fetch karta hai
    Returns: list of job dictionaries
    """
    all_jobs = []
    seen_ids = set()  # Duplicate jobs remove karne ke liye

    print("\n🔍 Jobs dhundh raha hun...")

    for keyword in SEARCH_KEYWORDS:
        for location in SEARCH_LOCATIONS:
            try:
                url = f"https://api.adzuna.com/v1/api/jobs/in/search/1"

                params = {
                    "app_id": APP_ID,
                    "app_key": APP_KEY,
                    "what": keyword,
                    "where": location,
                    "results_per_page": MAX_RESULTS_PER_SEARCH,
                    "content-type": "application/json"
                }

                response = requests.get(url, params=params, timeout=10)
                response.raise_for_status()

                data = response.json()
                jobs = data.get("results", [])

                print(f"  ✅ '{keyword}' in {location}: {len(jobs)} jobs mile")

                for job in jobs:
                    job_id = job.get("id", "")

                    # Duplicate check
                    if job_id in seen_ids:
                        continue
                    seen_ids.add(job_id)

                    # Clean job data
                    clean_job = {
                        "title": job.get("title", "N/A"),
                        "company": job.get("company", {}).get("display_name", "N/A"),
                        "location": job.get("location", {}).get("display_name", "N/A"),
                        "salary_min": job.get("salary_min", 0),
                        "salary_max": job.get("salary_max", 0),
                        "description": job.get("description", "")[:300] + "...",
                        "url": job.get("redirect_url", "#"),
                        "created": job.get("created", ""),
                        "keyword": keyword
                    }
                    all_jobs.append(clean_job)

            except requests.exceptions.ConnectionError:
                print(f"  ❌ Network error - Check internet connection")
            except requests.exceptions.Timeout:
                print(f"  ⏱️  Timeout for '{keyword}' in {location}")
            except requests.exceptions.HTTPError as e:
                print(f"  ❌ API Error: {e}")
            except Exception as e:
                print(f"  ❌ Unexpected error: {e}")

    print(f"\n📊 Total unique jobs mile: {len(all_jobs)}")
    return all_jobs


def format_salary(min_sal, max_sal):
    """Salary ko readable format mein convert karta hai"""
    if min_sal and max_sal:
        return f"₹{int(min_sal):,} - ₹{int(max_sal):,}"
    elif min_sal:
        return f"₹{int(min_sal):,}+"
    else:
        return "Salary not mentioned"
