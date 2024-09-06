from dash import Dash, html

# Testing

app = Dash(__name__)
server = app.server

image_path = 'assets/logo-mmu.png'

app.layout = [html.H1('MCM7183 Exercise 3'), html.Img(src=image_path)]

if __name__ == '__main__':
    app.run(debug=True)
