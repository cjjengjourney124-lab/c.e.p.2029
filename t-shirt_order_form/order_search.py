"""Filters t-shirt orders according to selected criteria for easy lookup."""

def filter_by_color(responses, color):
    """Returns only the responses that match the given shirt color."""
    filtered = []
    for response in responses:
        fields = response.split(",")
        if fields[3] == color:
            filtered.append(response)

    return filtered

def filter_by_size(responses, size):
    filterd=[]
    for response in responses:
        field=response.split(",")
        if field[2] == size:
            filterd.append(response)
    """Returns only the responses that match the given size."""
    return filterd
