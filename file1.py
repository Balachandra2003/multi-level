from elasticsearch import Elasticsearch

# Connect to Elasticsearch
es = Elasticsearch("http://localhost:9200")

# Static project data
project_data = [
    {
        "project_id": 1,
        "project_name": "Alpha",
        "total_bugs": 30,
        "solved_bugs": 15,
        "progress": 40
    },
    {
        "project_id": 2,
        "project_name": "Beta",
        "total_bugs": 10,
        "solved_bugs": 13,
        "progress": 22
    },
    {
        "project_id": 3,
        "project_name": "Gamma",
        "total_bugs": 25,
        "solved_bugs": 11,
        "progress": 27
    },
    {
        "project_id": 4,
        "project_name": "Delta",
        "total_bugs": 19,
        "solved_bugs": 7,
        "progress": 30
    },
    {
        "project_id": 5,
        "project_name": "Epsilon",
        "total_bugs": 8,
        "solved_bugs": 3,
        "progress": 40
    }
]

# Upload data to Elasticsearch
def upload_to_elasticsearch():
    for project in project_data:
        # Use project_id to avoid duplicates (overwrite if exists)
        es.index(index="project-daily-update1", id=project["project_id"], document=project)

    print("Project data uploaded successfully.")

# Run the upload once
if __name__ == "__main__":
    upload_to_elasticsearch()
