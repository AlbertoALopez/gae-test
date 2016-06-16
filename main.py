import webapp2


form = """
<form method="post">
    What is your birthday?
    <label>
        Month
        <input type="text" name="month">
    </label>
    <label>
        Day
        <input type="text" name="day">
    </label>
    <label>
        Year
        <input type="text" name="year">
    </label>
    <br>
    <br>
    <input type="submit">
</form>
"""

months = ['January',
          'February',
          'March',
          'April',
          'May',
          'June',
          'July',
          'August',
          'September',
          'October',
          'November',
          'December']

months_abbrvs = dict((m[:3].lower(), m) for m in months)

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.write(form)

    def post(self):
        self.response.out.write("Thanks!")

    def valid_month(month):
        if month:
            short_month = month[:3].lower()
            return months_abbrvs.get(short_month)

    def valid_day(day):
        if day and day.isdigit():
            int_day = int(day)
            if 1 <= int_day <= 31:
                return day

    def valid_year(year):
        if year and year.isdigit():
            user_input = int(year)
            if 1900 <= user_input <= 2020:
                return int(year)

app = webapp2.WSGIApplication([('/', MainPage)], debug=True)
