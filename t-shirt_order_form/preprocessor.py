"""Preprocesses form responses to meet a standard format."""
p=""
monos=""
def clean_data(responses):
    """Returns a normalized, deduped version of the response data."""
    cleaned = []
    for response in responses:
        cleaned.append(normalize(response))

    return remove_duplicates(cleaned)

def normalize(response):
    """Returns a normalized version of the response for easy comparison."""
    fields = response.lower().split(",")

    # Cap monograms at three letters.
    fields[-2] = fields[-2][:3].upper()
    city=fields[1]
    date=fields[-1].split("-")
    for i in fields:
        if len(fields)<6:
            fields.insert(3,"green")
    if city.lower()=="atlanta":
        month=date[0]
        day=date[1]
        date[0]=day
        date[1]=month

        fields[-1]="-".join(date)

    return ",".join(fields)

def remove_duplicates(responses):
    global p
    fixed = []
    
    # Using a set to track (name, city) tuples together
    seen_combinations = set()
    
    for i in responses:
        name = i.split(",")[0].lower().strip()
        city = i.split(",")[1].lower().strip()
        colo = i.split(",")[3].lower().strip()
        
        # Check if this specific name-and-city combo has been seen yet
        if (name, city) not in seen_combinations:
            fixed.append(i)
            seen_combinations.add((name, city)) # Save the combo
            
            if colo not in p:
                if p == "":
                    p += colo
                else:
                    p += ", " + colo
    """Returns a new list that removes any responses with repeated names."""
    return fixed
