curl -I -k "https://api.github.com/repos/:owner/:repo/commits?per_page=1" | sed -n '/^[Ll]ink:/ s/.*"next".*page=\([0-9]*\).*"last".*/\1/p'

### And that's all !
# I saw many fighting with finding first commit SHA or similar fancy thing.
# Here we just rely on the GH API, asking commits at 1 per page and parsing the last page number in the header of the reply (whose body only holds the last commit !)
# So this is robust and bandwidth efficient. :)

# If one want the commit count of a specific SHA, just use :
curl -I -k "https://api.github.com/repos/:owner/:repo/commits?per_page=1&sha=:sha" | sed -n '/^[Ll]ink:/ s/.*"next".*page=\([0-9]*\).*"last".*/\1/p'

# And for a specific time (date using ISO 8601 format, 'Z' for UTC) :
curl -I -k "https://api.github.com/repos/:owner/:repo/commits?per_page=1&until=yyyy-MM-ddThh:mm:ssZ" | sed -n '/^[Ll]ink:/ s/.*"next".*page=\([0-9]*\).*"last".*/\1/p'