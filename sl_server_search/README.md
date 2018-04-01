# Softlayer Server Search

For the purpuse of speeding up the search of necessary hardware during provisions, as searching through 
the web interface takes forever and the trasaction page does not take into account priority items to swap.  Example,
it could very well recommed a server that needs a proc swap, rather than one that just need new drives.

## Prerequisites

Must first Export CSV from SL Hardware Search page with at least the following seach parameters, you are free to add more:
*Location: [Whatever DC and server room provision will be at]
*Hardware Status: Inventory
*Hardware Function: Web Server

Must also have python installed.
