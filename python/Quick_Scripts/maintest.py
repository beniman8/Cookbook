from builderpatern import HTMLPage, HTMLBuilder
from htmlviewer import HTMLViewer

def main() -> None:
    builder = HTMLBuilder()
    builder.add_title("My website").add_heading(
        "The heading of the website", 1
    ).add_paragraph("Paragraph is the best of the world").add_button(
        "cool world", onclick="https://www.google.com"
    ).add_metadata('google','cool')

    page = builder.build()
    
    file_path = "page.html"
    
    with open(file_path,"w") as f:
        f.write(page.render())

    print(page.render())

    HTMLViewer(filename=file_path).start()

if __name__ == "__main__":
    main()
