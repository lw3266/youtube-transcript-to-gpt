# YouTube Transcript to GPT
The purpose of this tool is to 1) help rip transcript from YouTube without api (no need for signin to reduce some data tracking), 2) accelerate learning with LLM.

Disclaimer: might contain LLM generated code; this project is for fun and experimental, and favors data privacy over reliability. 

## Using the tool

### Setup

Paste your OpenAI api key in `config.json`.

Open any YouTube video with transcript available, inspect the page and go to the network tab. 

Then in the video description click the `Show transcript' button. From there, you should see a "get_transcipt" query in the list of network requests. Find that query and click on the payload.

Now you will copy the entire payload to the notepad, and exact the information according to the following instructions.

The entire payload will contain two copies of the video url and the `params` at the end. Those has been extracted automatically by the code, you will copy and paste the rest according to what is missing in `transcript_extract.py`. This will only need to be done once, and will work for different video urls unless YouTube changes its methods in the future.

In `transcript_extract.py`, look for the `payload` variable. Simply copy from the start of the payload until the first mentioning of the url, paste that into the first empty string. Repeat the same until the second url. Omit the actual params in the end.


Lastly, create a virtual env if needed, and install OpenAI api.

> pip install openai

### Running the code
Simply run `transcript_extract.py`

> python3 src/transcript_extract.py

Paste the url when prompted. If transcript has been successfully received, then wait some time for ChatGPT to respond.
