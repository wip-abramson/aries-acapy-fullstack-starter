from views import invite, check_active

def setup_routes(app):
    app.router.add_get('/connection/new', invite)
    app.router.add_get('/connection/{conn_id}/active', check_active)