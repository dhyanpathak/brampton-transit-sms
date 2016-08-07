import mechanize
from BeautifulSoup import BeautifulSoup

message = ""

def schedule(stop):
    """(string) -> string

    Return route names with its corresponding arrival times. Parameter must be a Brampton Transit stop number

    >> schedule('2302')
    Route 5 to Bovaird EB - 5A: 02:06 PM
    Route 30 to Airport Road SB: 02:07 PM

    """
    global message
    url = "http://nextride.brampton.ca/mob/SearchBy.aspx"
    # emulate browser, ignore robots, and disable handle refreshes to prevent browser hanging, add headers
    br = mechanize.Browser()
    br.set_handle_robots(False)
    br.set_handle_refresh(False)
    br.addheaders = [
        ('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
        ('Origin', 'http://www.nextride.brampton.ca'),
        ('User-Agent',
         'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.17 (KHTML, like Gecko)  Chrome/24.0.1312.57 Safari/537.17'),
        ('Content-Type', 'application/x-www-form-urlencoded'),
        ('Referer', 'http://nextride.brampton.ca/mob/SearchBy.aspx'),
        ('Accept-Encoding', 'gzip, deflate'),
        ('Accept-Language', 'en-US,en;q=0.5')
    ]
    # i know these comments suck but python is literally plain english.
    # open the browser, select the form and enter requested stop number. submit form and fetch results
    br.open(url)
    response = br.response().read()
    br.select_form(nr=0)
    br['ctl00$mainPanel$searchbyStop$txtStop'] = stop
    html = br.submit(name='ctl00$mainPanel$btnGetRealtimeSchedule').read()
    soup = BeautifulSoup(html)
    error = soup.body.findAll(text='No stop found for given stop code.')
    if len(error) > 0:
        # error handling
        message = "Stop is either invalid or an error has occured."
    else:
        # scrape through requested table
        # apply string functions to get route names along with arrival times and output that
        table = soup.findAll('table')[1]
        rows = table.findAll('td')
        list = []
        for cell in rows:
            cell = (str(cell))[4:-5]
            list.append(cell)
        i = 0
        while i < (len(list) - 1):
            message += (list[i] + ': ' + list[i + 1] + '\n')
            i += 2
        return message