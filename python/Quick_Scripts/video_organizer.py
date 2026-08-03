import os

# Change this to where you want the system created
BASE_PATH = os.path.join(os.getcwd(), "Creator_OS")

folders = [

# CONTENT
"Content/00_Inbox_Raw_Footage/Camera_A",
"Content/00_Inbox_Raw_Footage/Camera_B",
"Content/00_Inbox_Raw_Footage/Screen_Recordings",
"Content/00_Inbox_Raw_Footage/Phone_Footage",

"Content/01_Project_Files/DaVinci_Resolve",
"Content/01_Project_Files/Graphics",
"Content/01_Project_Files/Thumbnails",

"Content/02_Assets/Music",
"Content/02_Assets/Sound_Effects",
"Content/02_Assets/Stock_Footage",
"Content/02_Assets/Logos",
"Content/02_Assets/Overlays",

"Content/03_Working_Edits/Rough_Cuts",
"Content/03_Working_Edits/Fine_Cuts",
"Content/03_Working_Edits/Final_Timeline",

"Content/04_Exports/YouTube_16x9",
"Content/04_Exports/TikTok_9x16",
"Content/04_Exports/Instagram_Reels",

"Content/05_Captions_Subtitles",
"Content/06_Thumbnails",

"Content/07_Archive/Completed_Projects",
"Content/07_Archive/Old_Raw_Footage",

# ASSETS LIBRARY
"Assets_Library/Music",
"Assets_Library/Sound_Effects",
"Assets_Library/Broll",
"Assets_Library/Transitions",
"Assets_Library/Lower_Thirds",
"Assets_Library/Stream_Alerts",
"Assets_Library/Overlay_Animations",

# EDITING PROJECTS
"Editing_Projects/DaVinci_Resolve_Databases",
"Editing_Projects/Templates",
"Editing_Projects/Active_Projects",

# EXPORTS
"Exports/YouTube",
"Exports/TikTok",
"Exports/Instagram",
"Exports/Shorts_Reels",

# UPLOAD PIPELINE
"Uploads/Ready_To_Upload",
"Uploads/Scheduled",
"Uploads/Published",

# CONTENT CALENDAR
"Content_Calendar/Planned",
"Content_Calendar/Filmed",
"Content_Calendar/Editing",
"Content_Calendar/Posted",

# ARCHIVE
"Archive/Completed_Videos",
"Archive/Old_Projects"
]


def create_structure():
    for folder in folders:
        path = os.path.join(BASE_PATH, folder)
        os.makedirs(path, exist_ok=True)
        print(f"Created: {path}")

    print("\n✅ Creator Video System Created Successfully!")


if __name__ == "__main__":
    create_structure()