from dash import Dash, html

# Testing

app = Dash(__name__)
server = app.server

app.layout = html.H1('MCM7183 Exercise 3')

if __name__ == '__main__':
    app.run(debug=True)
