import webbrowser
import os
import re
//update

#Styles and Scripting for Page
main_page_head = ' ' ' 
<!DOCTYPE html>
<html lang="en">
<head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <title>FilmPop</title>
        <meta name="FilmPop" content="Your one stop shop for current movie trailers streamed conviently to your tv!">
        <link rel="stylesheet" href="main.css"> 
    </head>
    <body>
        <div class="top_nav">
            <ul>
                <li><a href="#">Login</a></li>
                <li><a href="#">Register</a></li>
            </ul>
        </div>
        
        <div class ="header_main">
            <div class="headerContent">
            <a href="#"><img class="logo" src="images/filmpop_logo.png" width="auto" height="100" align="center" alt="FilmPop"/></a>
            
        <div class="headerNav">
            #Will probabaly Use Side Nav Here with Aside tag, instead of standard horizontal nav bar. Using list to determine different genres aswell as tv show trailers and incorporate
</html>
'''

# A single movie entry html template
movie_tile_content = '''
<div class = "col-md-6 col-lg-4 movie-tile text-center" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">
<img src="{poster_image_url}" width ="220" height="342">
<h2>{movie_title}</h2>
</div>
'''

def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = '''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+',movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(
        r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = (youtube_id_match.group(0)if youtube_id_match 
        else None)
        
        
        # Append the tile for the movie with its content filled in
        
        content += movie_tile_content.format(
            movie_title = movie.title,
            poster_image_url = movie.poster_image_url,
            trailer_youtube_id = trailer_youtube_id
        )
    return content

def open_movies_page(movies):
    # Create or overwrite the output file
    output_file = open('filmpop.html', 'w')
    
    # Replace the movie tiles placeholder generated content
    rendered_content = main_page_content.format(
    movie_tiles = create_movie_tiles_content(movies))
    
    # Output the file
    output_file.write(main_page_head + rendered_content)
    output_file.close()
    
    # Open the output file in the browser (in a new tab if possible)
    
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)
