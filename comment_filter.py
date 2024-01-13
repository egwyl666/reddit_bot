excluded_keywords = ["Warning", "do not comment", "you will be banned"]


def should_comment(submission_text):
    #   Function that determines whether to comment on a post, excluding keywords
    for keyword in excluded_keywords:
        if keyword.lower() in submission_text.lower():
            return False
    return True
