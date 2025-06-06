def normalize_job(job, source):
    return {
        "title": job.get("title", ""),
        "company": job.get("company", ""),
        "location": job.get("location", ""),
        "link": job.get("link", ""),
        "post_date": job.get("post_date", ""),
        "source": source
    }

def normalize_jobs(jobs, source):
    return [normalize_job(job, source) for job in jobs]