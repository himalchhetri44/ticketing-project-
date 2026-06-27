from app.repository.user_repo import get_all_events, search_events


def get_home_events(query='', category=''):
    if query or category:
        return search_events(query, category)
    return get_all_events()
