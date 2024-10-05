def remove_duplicate_links(file_path):
    try:
        # Read all lines (links) from the file
        with open(file_path, 'r') as file:
            links = file.readlines()

        # Remove any leading/trailing whitespace from each link and remove duplicates
        unique_links = list(set(link.strip() for link in links))

        # Sort the links (optional, if you want to keep them in order)
        unique_links.sort()

        # Write the unique links back to the file
        with open(file_path, 'w') as file:
            for link in unique_links:
                file.write(link + '\n')

        print(f"Duplicates removed. {len(links) - len(unique_links)} duplicate(s) found.")
    
    except Exception as e:
        print(f"An error occurred: {e}")

# Replace 'links.txt' with the path to your .txt file
file_path = '/home/aiobc/Desktop/projects/testing/datascraping/all_hrefs.txt'
remove_duplicate_links(file_path)
