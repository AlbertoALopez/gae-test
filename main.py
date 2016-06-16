import webapp2
import cgi


form = """
<form method="post">
    What is your birthday?
    <br>
    <label>Month <input type="text" name="month" value="%(month)s"></label>
    <label>Day <input type="text" name="day" value="%(day)s"></label>
    <label>Year <input type="text" name="year" value="%(year)s"></label>
    <div style="color: red">%(error)s</div>
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
    def write_form(self, error="", month="", day="", year=""):
        self.response.out.write(form % {"error": error,
                                        "month": self.escape_html(month),
                                        "day": self.escape_html(day),
                                        "year": self.escape_html(year)})

    def get(self):
        self.write_form(form)

    def post(self):
        user_month = self.request.get('month')
        user_day = self.request.get('day')
        user_year = self.request.get('year')

        month = self.valid_month(user_month)
        day = self.valid_day(user_day)
        year = self.valid_year(user_year)

        if not (month and day and year):
            self.write_form("Please enter valid text.",
                            user_month, user_day, user_year)
        else:
            self.response.out.write("Thanks!")

    def valid_month(self, month):
        if month:
            short_month = month[:3].lower()
            return months_abbrvs.get(short_month)

    def valid_day(self, day):
        if day and day.isdigit():
            int_day = int(day)
            if 1 <= int_day <= 31:
                return day

    def valid_year(self, year):
        if year and year.isdigit():
            user_input = int(year)
            if 1900 <= user_input <= 2020:
                return int(year)

    def escape_html(self, s):
        return cgi.escape(s, quote=True)

app = webapp2.WSGIApplication([('/', MainPage)], debug=True)
