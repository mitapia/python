# Softlayer Server Search

For the purpuse of speeding up the search of necessary hardware during provisions, as searching through 
the web interface takes forever and the trasaction page does not take into account priority items to swap.  Example,
it could very well recommed a server that needs a proc swap, rather than one that just need new drives.

## Prerequisites

Must first Export CSV from SL Hardware Search page with at least the following seach parameters, you are free to add more:
* Location: [Whatever DC and server room provision will be at]

Must also have python installed.

### How to run
In the cammand line run:
`python run_server_search.py location_of_file.csv`
The csv file is required to run.

Oncre runing it will ask first to select 1U, 2U, or 4U, must only input integer NO 'U'.
Next it will as for a proccessor, this does not have to be the full name, partials work just fine.
For the next couple of steps it will be present you with all the options avalable componen by component in the followin order:
* Proc
* Drive Controller
* Ram
* Drives

If only one option is availabe it will automaticly be selected.

At the end it will open the Edit Hardware page on your default browser.
