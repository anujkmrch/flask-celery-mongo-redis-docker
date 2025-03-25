from app import celery, create_app
app = create_app()

if __name__ == "__main__":
    with app.app_context():
        worker = celery.worker_main(argv=['worker', '--loglevel=info'])