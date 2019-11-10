# YouTube Video Downloader Application
---
## List of the technologies to be used in this project
---
- Python django framework rest-framework.
- sqlite3 database
- Python youtube api
- React 
- axios

## List of all the things that i want to do in the applicaton.
---
- Create a cool front end for the website
    - Navigation bar for changing between url input component and the downloads component.
    - home
        - input prompt to collect url
    - downloads
        - card layout to show download component


- Capable of downloading single youtube video

- Capable of downloading playlist
    - This will be a download component that can be extended to show all the individual downloads.
    
    - This will show the general progress bar for all individual video downloads.

- Has a place to show the queued downloads
    - This will be a dashboard holding all the downloads.

    - It will show list of all the videos queued under a playlist.

- Ability to remove downloading item from the queue
    - This will be contained in the download-item component.

- Ability to pause and play downloads
    - This will be on the download-item component and will be alternated.



## React components and their features

- ### App Component
    - This will hold the whole site.

- ### Navigation
    - This will contain the Nav-items(home, downloads)

- ### Home Component
    - This will contain form input (for collecting youtube url)
    
    - It will also contain a submit button from placing request to the backend.

    - It will have a selection bar to adjust the quality of the video to be downloaded.

- ### Downloads Component
    - This will contain a dashboard holding all pending downloads.

    - The dashboard will have downloads components
        - thumbnail of video or playlist
        - delete button
        - pause / play button
        - name of the video
