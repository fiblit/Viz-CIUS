Name: Dalton Hildreth
ID: 5117575
----
Part 6 Features:
    Each bar chart has their bars colored with a gradient according
    to their respective values. (white-ish = low, blue-ish = high)

    The axes are now crisp and clean looking.

    There is now an annual growth rate graph

    There are horizontal and sometimes vertical grid lines on each of
    the graphs. The choice of including vertical lines or not was based
    on visibility of the data.

    Mousing over a bar will highlight that bar and display a tooltip with
    all the data; specifically, highlighting the current chart's data.

    There is an intro animation for some aesthetic pleasure. (Note: don't
    mouseover the animation while it's playing, there's a bug that will
    freeze the height of the bars when you do that.)

    Further Note: the tooltips get squished if your screen is too thin.
    It kinda looks gross, but is easily fixed by making your screen wider.
    I could've made the CSS responsive, but I felt it was unnecessary for
    this assignment.

    Also, I organized my code to have less Ctrl-C / Ctrl-V going on. :P

    
-----
To run:
Either set the --allow-file-access-from-files in your chrome exe
  (PLEASE remember to turn it off before you go browsing the web again)

OR (my favorite since it is safe, and you get to have python :) )
  1. Install python (3, preferrably) if you don't already have it 
    https://www.python.org/
  2. If you're using python 2 type:
    python -m SimpleHttpServer
  3. If you're using python 3 type:
    python -m http.server
    or 
    python3 -m http.server
    depending on how you set up the paths.
  4. Goto this URL;
     http://localhost:8000/HW4_Starter.html

OR
    Open HW4_Starter.html in Mozilla Firefox:
    https://www.mozilla.org/en-US/firefox/products/
  