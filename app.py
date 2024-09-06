from dash import Dash, html

# Testing

app = Dash(__name__)
server = app.server

app.layout = html.H2('Hello MMU!')

if __name__ == '__main__':
    app.run(debug=True)
