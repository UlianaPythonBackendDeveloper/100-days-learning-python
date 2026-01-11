def build_HTML_list(coll):
    parts = []
    for item in coll:
        parts.append(f"<li> {item} </li>")
        
        inner_value = "".join(parts)
        result = f"<ul>{inner_value} </ul>"
        return result

coll = ["milk","butter"]
build_HTML_list(coll)
print()