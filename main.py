from pyscript import display, document

# Define club information using dictionaries
club_info = {
            "chess": {
                "name": "Chess Club",
                "description": "A club for chess enthusiasts of all skill levels.",
                "meeting_time": "Every Wednesday 3:30-5:00 PM",
                "location": "Room 405",
                "advisor": "Mr. Santos",
                "members": 20,
                "category": "Academic"
            },
            "drama": {
                "name": "Drama Club",
                "description": "For students interested in theater, acting, and stage production.",
                "meeting_time": "Every Monday and Thursday 4:00-6:00 PM",
                "location": "MM Hall",
                "advisor": "Ms. Evangelista",
                "members": 22,
                "category": "Arts"
            },
            "robotics": {
                "name": "Robotics Club",
                "description": "Design, build, and program robots for competitions.",
                "meeting_time": "Every Tuesday 3:45-5:30 PM",
                "location": "Computer Lab",
                "advisor": "Ms. Pasco",
                "members": 18,
                "category": "Academic"
            },
            "debate": {
                "name": "Debate Club",
                "description": "Develop public speaking and argumentation skills.",
                "meeting_time": "Every Friday 3:30-5:00 PM",
                "location": "Room 507",
                "advisor": "Ms. Carabot",
                "members": 12,
                "category": "Academic"
            },
            "art": {
                "name": "Art Club",
                "description": "Explore various art mediums and techniques.",
                "meeting_time": "Every Wednesday 3:45-5:15 PM",
                "location": "Art Room",
                "advisor": "Mr. Balajadia",
                "members": 20,
                "category": "Arts"
            },
            "": {
                "name": "",
                "description": "",
                "meeting_time": "",
                "location": "",
                "advisor": "",
                "members": "",
                "category": ""
            }
        }
        
def show_club_info(e):
    document.getElementById('club-info').innerHTML = " "
    selected_club = document.getElementById("club-select").value
    info = club_info.get(selected_club, club_info[""])
            
    output = f"""
            {info['name']}
            Description:{info['description']}
            Meeting Time: {info['meeting_time']}
            Location: {info['location']}
            Advisor: {info['advisor']}
            Number of Members: {info['members']}
            Category: {info['category']}
            """
    display(output, target="club-info")