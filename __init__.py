"""Entry point for our twitter app flask app."""

from .sp_search_track_app import create_app

if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)
