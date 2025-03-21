import requests
import re

from api import extract_and_explain

request_url = "https://www.youtube.com/youtubei/v1/get_transcript?prettyPrint=false"

def find_params(response):
    # Define the regular expression pattern to look for a string after the search string that ends with a "!"
    pattern = re.compile(rf'{re.escape("\"getTranscriptEndpoint\":{\"params\":\"")}\s*(\S.*?")', re.DOTALL)    
        
    match = pattern.search(response)

    if match:
        return match.group(1)
    else:
        raise "Warning: video might not have transcript available, need to check manually"
        return None
    
def store_transcript(response):
    pattern = re.compile(rf'{re.escape("\"text\":\"")}\s*(\S.*?")', re.DOTALL)
    
    # List to store all matched results
    transcript = []
        
    # Find all matches in the file content
    matches = pattern.findall(response)
    
    # Store the matches in the results list
    for match in matches:
        transcript.append(match[:-1])

    with open("transcript.txt", 'w') as out_file:
        for line in transcript:
            out_file.write(line + '\n')
    
def extract_transcript(video_url):
# Extract video ID from URL
    # video_id = video_url.split("v=")[1].split("&")[0]

    # URL to the YouTube video page
    # page_url = f"https://www.youtube.com/watch?v={video_id}"

    # Send a GET request to fetch the page content
    response = requests.get(video_url)

    if response.status_code != 200:
        raise f"Failed to retrieve the page. HTTP Status Code: {response.content}"

    params = find_params(response.text)

    if not params:
        raise f"Video probably does not have transcript"
    else:
        params = params[:-1]

    # print(params)

    payload = "" + "url" + "" + "url" + "" + params + "'}"

    # # Send the POST request
    response = requests.post(request_url, payload)
            
    if response.status_code != 200:
        raise f"Error: Received {response.content} from the YouTube API"
    print(f"Transcript received")

    store_transcript(response.text)

    return 

def main():
    video_url = input("Enter the YouTube video URL: ")
    
    extract_transcript(video_url)
    
    extract_and_explain()

if __name__ == "__main__":
    main()

