# bachelor_thesis_proposal
The proposal to the bachelor thesis of Andreas Schaufelbühl

Setup: 

    1.)Install Latex: http://www.howtotex.com/howto/
    
    2.) Install Latex-program e.g. TeXstudio: http://www.texstudio.org/
    
    3.) Open schaufelbuehl_bachelor.tex
      

High level Steps of the Thesis:

1) Build a framework (with IDE) able to:
   - download data from different (at least two) apple stores (Google Play, Apple Store, etc.)
     related to user reviews, user rating,  source code changes and their releases.
   - visualize some statistics of an app:
     -> How many releases they have;
     -> How many user reviews are reported;
     -> How many of user reviews suggest new "feature requests", to "fix a bug" etc.
        (using the tool ARdoc available at "http://www.ifi.uzh.ch/seal/people/panichella/tools/ARdoc.html")
     -> Etc. 


2) Handle one of the following challenges:
   a) Traceability: design and implement a tool able to
      - Linking reviews to specific versions;
      - Linking user requests to source code (or source code changes).
        Once linked source code to user reviews, compute some statistics
        on how many "user requests/feedback" are already answered
        and how many of them need a fix. 
        Suggest which "features" of  "bugs" need to be (still) addressed and 
        prioritize them (i.e. make the more important at the top).
      - Conceive a mechanism which uses reviews data to check feeling of users about new
        releases (in according to features implementes and bugs fixed by developers). (OPTIONAL);
      - (Future work) Update and improve requirements using information contained in reviews (OPTIONAL);
      - (Future work) Linking requirements from reviews to source code (OPTIONAL);
 
   b) Predict the right price of an application:
      - Linking app store metadata (price, rating, etc.) to source code;
      - Conceive a mechanism that suggest for new app the appropriate price.
      
      
# research questions:

    1) To what extend is it possible to cluster/group app reviews user feedback and link them to source code entities?
    2) To what extend developers of mobile apps address users requests?
      2.1) Sub-Research question:-> What kinds of feedback are usually  addressed by developers?
      2.2)Sub-Research question:-> What kind of feedback are usually not addressed by developers?

