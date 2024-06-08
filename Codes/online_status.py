def online_count(status_dict):
    total_online = 0
    for name in status_dict:
        if status_dict[name] == "online":
            total_online += 1
    return total_online
