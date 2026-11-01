import form
import order_search
import preprocessor
while True:
    sizes=["xs", "s", "m", "l", "xl"]
    responses = preprocessor.clean_data(form.responses)
    search=input(f"""pick a choice: {preprocessor.p} or {", ".join(sizes)}--> """).lower()
    shirtscol = order_search.filter_by_color(responses, search)
    shirtsize = order_search.filter_by_size(responses, search)
    
    
    if search in sizes:
        print(f"{len(shirtsize)} total {search.upper()} shirts.")
        for c in preprocessor.p.split(", "):
            size_shirts_in_color = order_search.filter_by_color(shirtsize, c)
            print(f"Order {len(size_shirts_in_color)} {search.upper()} {c} shirts.")
        print("")
        
    else:
        print(f"{len(shirtscol)} total {search.upper()} shirts.")
        for size in sizes:
            green_shirts_in_size = order_search.filter_by_size(shirtscol, size)
            print(f"Order {len(green_shirts_in_size)} {size.upper()} {search.upper()} shirts.")
        print("")
