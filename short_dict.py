def main():
    # spacecraft = {'name': 'Voyager 1','distance': 14.0}
    spacecraft = {"name": "Jupiter Webb Space Telescope"}
    spacecraft["distance"] = 1.0

    report = create_report(spacecraft)
    print(report)

    report = create_report_v1(spacecraft)
    print(report)
    

def create_report(spacecraft):
    return f"""
    ==== REPORT ====

    Name: {spacecraft['name']}
    Distance: {spacecraft['distance']} AU

    ================
    """

def create_report_v1(spacecraft):
    return f"""
    ==== REPORT ====

    Name: {spacecraft['name']}
    Distance: {spacecraft['distance']} AU

    ================
    """

if __name__ == "__main__":
    main()