"""Entry point for our twitter app flask app."""

from .sp_search_track_app import create_app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
