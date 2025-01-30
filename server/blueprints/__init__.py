def register_blueprints(app):
    from .mechanic import mechanic_bp
    from .service_ticket import service_ticket_bp

    app.register_blueprint(mechanic_bp, url_prefix='/mechanics')
    app.register_blueprint(service_ticket_bp, url_prefix='/service-tickets')