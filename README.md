# Content Monitoring & Flagging System

## Overview

This project is a Django-based backend system that monitors external content against user-defined keywords, generates relevance flags, and supports a review workflow with suppression logic.

The system is designed to demonstrate clean backend architecture, API design, and business logic implementation.

---

## Features

* Add and manage keywords
* Import and store content items
* Keyword-based matching with scoring
* Flag generation for matched content
* Reviewer workflow (pending, relevant, irrelevant)
* Suppression logic for irrelevant content
* REST APIs for full interaction

---

## Matching Logic

The system uses a deterministic scoring mechanism:

| Condition                      | Score |
| ------------------------------ | ----- |
| Exact keyword match in title   | 100   |
| Partial keyword match in title | 70    |
| Keyword match in body          | 40    |

---

## Suppression Logic (Core Feature)

If a flag is marked as **irrelevant**, it will NOT be generated again in future scans unless:

* The content item is updated (`last_updated` changes)

This ensures:

* No duplicate noise
* Efficient review workflow
* Real-world applicability

---

## Tech Stack

* Python
* Django
* Django REST Framework
* SQLite

---

## Project Structure

```
content_monitoring/
│── content_monitoring/
│── core/
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   ├── services.py
│   ├── urls.py
│── manage.py
│── README.md
```

---

## Setup Instructions

```bash
git clone https://github.com/your-username/content-monitoring-system.git
cd content_monitoring
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

---

## API Endpoints

| Method | Endpoint       | Description          |
| ------ | -------------- | -------------------- |
| POST   | `/keywords/`   | Create a keyword     |
| POST   | `/scan/`       | Trigger content scan |
| GET    | `/flags/`      | Retrieve all flags   |
| PATCH  | `/flags/{id}/` | Update flag status   |

---

## Example Workflow

1. Add a keyword → `"django"`
2. Add content via admin panel
3. Trigger `/scan/`
4. System generates flags
5. Reviewer marks flag as `irrelevant`
6. Future scans suppress that flag unless content updates

---

## Assumptions

* Mock data used instead of external API
* Matching is case-insensitive
* Content updates are determined by `last_updated` field

---

## Future Improvements

* Background jobs using Celery
* NLP-based semantic matching
* Deduplication optimization
* Minimal frontend dashboard
* Automated tests

---

## Author

**Aditya Chauhan**

---

## Notes

This project focuses on correctness, clean architecture, and maintainability rather than over-engineering.
