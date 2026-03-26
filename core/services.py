from .models import Keyword, ContentItem, Flag


# 🔹 Scoring Logic
def calculate_score(keyword, content):
    keyword = keyword.lower()
    title = content.title.lower()
    body = content.body.lower()

    # Exact match in title
    if keyword == title:
        return 100

    # Partial match in title
    if keyword in title:
        return 70

    # Match in body
    if keyword in body:
        return 40

    return 0


# 🔹 Suppression Logic (MOST IMPORTANT)
def should_create_flag(existing_flag, content):
    if not existing_flag:
        return True

    # If previously marked irrelevant
    if existing_flag.status == 'irrelevant':
        # Only show again if content updated
        if existing_flag.reviewed_at:
            return content.last_updated > existing_flag.reviewed_at
        return False

    return True


# 🔹 Scan Function
def run_scan():
    keywords = Keyword.objects.all()
    contents = ContentItem.objects.all()

    for content in contents:
        for keyword in keywords:
            score = calculate_score(keyword.name, content)

            if score > 0:
                existing_flag = Flag.objects.filter(
                    keyword=keyword,
                    content_item=content
                ).first()

                if should_create_flag(existing_flag, content):
                    Flag.objects.update_or_create(
                        keyword=keyword,
                        content_item=content,
                        defaults={
                            'score': score,
                            'status': 'pending'
                        }
                    )